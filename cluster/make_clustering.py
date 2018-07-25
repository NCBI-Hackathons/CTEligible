import argparse
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import scipy.cluster
import scipy.spatial.distance
import sklearn.cluster
import sklearn.feature_extraction
import sklearn.manifold
import sklearn.metrics.pairwise

if True:
  p = argparse.ArgumentParser()
  p.add_argument("--tag", required=True)
  args = p.parse_args()
  tag = args.tag
else:
  tag = "Hemoglobin_CTEP Trials_072018"
  #tag = "Platelets_CTEP Trials_072018"
  #tag = "WBC_CTEP Trials_072018"
  #tag = "HIV_CTEPTrials_072018"

input_tsv = "../nci_data/dataset1-trials/" + tag + ".tsv"
output_pdf = "./" + tag + ".clustering.pdf"
features_csv = "./" + tag + ".features.csv"
linkage_matrix_csv = "./" + tag + ".linkage_matrix.csv"

# Load data.
tb = pd.read_table(input_tsv)
num_rows_excluded = sum(pd.isnull(tb["Boolean"]))
num_rows_orig = tb.shape[0]
tb = tb.loc[~pd.isnull(tb["Boolean"]),:]
tb = tb.reset_index(drop=True)
num_rows = tb.shape[0]
print("Excluding %d of %d rows" % (num_rows_excluded, num_rows_orig))
print("After exclusion, %d rows remain" % num_rows)

# Parse boolean.
def f(b):
  b = re.sub(r"[()]", "", b)
  operators = [w for w in b.split() if w in ("OR", "AND")]
  as_ops = b.replace("OR", "OP").replace("AND", "OP")
  triples = [tuple(re.split(r'(>=|<=|>|<|==|=)', t.strip(), maxsplit=1)) for t in as_ops.split("OP")]
  triples = [tuple(ti.strip() for ti in t) for t in triples]
  for i, t in enumerate(triples):
    print(t)
    if len(t) == 2:
      new_triple = (t[0], t[1], "?")
      print("Warning: {} is not of length 3, replacing with {}".format(t, new_triple))
      triples[i] = new_triple
    if len(t) == 1:
      new_triple = (t[0], "?", "?")
      print("Warning: {} is not of length 3, replacing with {}".format(t, new_triple))
      triples[i] = new_triple
  return {"triples": triples, "operators": operators}
def g(b):
  if pd.isnull(b):
    return b
  else:
    return f(b)
tb["parsed"] = [g(b) for b in tb["Boolean"]]

triples = [x["triples"] for x in tb["parsed"] if x]
operators = [x["operators"] for x in tb["parsed"]]

# Make features.
feat = [collections.defaultdict(float) for i in range(tb.shape[0])]
for i, triple_list in enumerate(triples):
  for l, c, r in triple_list:
    # Add count of each element alone within each triple.
    feat[i]["l_count_%s" % l] += 1
    feat[i]["c_count_%s" % c] += 1
    feat[i]["r_count_%s" % r] += 1
    # Add count of each pair of elements within each triple.
    feat[i]["lc_count_(%s, %s)" % (l, c)] += 1
    feat[i]["lr_count_(%s, %s)" % (l, r)] += 1
    feat[i]["cr_count_(%s, %s)" % (c, r)] += 1
    # Add count of each triple.
    t1 = (l, c, r)
    feat[i]["triple_count_%s" % str(t1)] += 1
    # Add count of each pair of triples.
    for t2 in triple_list:
      feat[i]["triple_pair_count_%s_%s" % (str(t1), str(t2))] += 1
for i, operator_list in enumerate(operators):
  for o1 in operator_list:
    # Add count for each operator.
    feat[i]["operator_count_%s" % o1] += 1
    # Add count for each pair of operators.
    for o2 in operator_list:
      feat[i]["operator_pair_count_%s_%s" % (o1, o2)] += 1

# Make feature matrix.
feature_vectorizer = sklearn.feature_extraction.DictVectorizer(sparse=False)
X = feature_vectorizer.fit_transform(feat)

# Carry out hierarchical clustering.
#hc_linkage = scipy.cluster.hierarchy.linkage(X, method="ward", metric="euclidean")
hc_linkage = scipy.cluster.hierarchy.linkage(X, method="complete", metric="cosine")
#hc_linkage = scipy.cluster.hierarchy.linkage(X, method="average", metric="cosine")

# Plot clustering.
h = 25.0 * tb.shape[0] / 174
fig = plt.figure(figsize=(25, h))
leaf_labels = [x for x in tb["Boolean"]]
dn = scipy.cluster.hierarchy.dendrogram(hc_linkage, labels=leaf_labels, orientation="left")
plt.title("Hierarchical clustering of %s " % tag)
plt.axis('tight')
plt.subplots_adjust(right=0.45)
plt.savefig(output_pdf)
plt.close(fig)

# Save features used for clustering.
feature_colnames = ["feature_%s" % x for x in feature_vectorizer.get_feature_names()]
feature_tb = pd.DataFrame(X, index=tb.index, columns=feature_colnames)
feature_with_orig_tb = pd.concat((tb, feature_tb), axis=1)
feature_with_orig_tb.to_csv(features_csv)
assert feature_tb.shape[0] == feature_with_orig_tb.shape[0]

# Save clustering output.
linkage_matrix_tb = pd.DataFrame(hc_linkage, columns=["hc_1", "hc_2", "hc_3", "hc_4"])
linkage_matrix_tb.to_csv(linkage_matrix_csv)
