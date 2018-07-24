import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance
import sklearn.cluster
import sklearn.manifold
import sklearn.metrics.pairwise

# Load data and rename columns.
nlp_tb = pd.read_csv("firstpass_NLPparsed/hiv_nlp_output.csv")
assert np.all(nlp_tb.columns == ['nci_id', 'nct_id', 'official_title',
                                'inclusion_indicaInclusionor',
                                'description',
                                'Text',
                                'Boolean',
                                "{'negated_codes': [], 'possible_codes': [], 'text': u'description', 'affirmed_codes': []}"])
nlp_tb.columns = ['nci_id', 'nct_id', 'official_title',
                  'exclusion_inclusion',
                  'description',
                  'Text',
                  'Boolean',
                  'codes_repr']

# Parse the codes structure.
nlp_tb["codes_obj"] = [eval(c) for c in nlp_tb.codes_repr]
nlp_tb["has_codes"] = [(len(c["negated_codes"]) > 0) or 
                       (len(c["possible_codes"]) > 0) or 
                       (len(c["affirmed_codes"]) > 0) for c in nlp_tb["codes_obj"]]
nlp_tb["codes_text"] = [c["text"] for c in nlp_tb["codes_obj"]]

# Exclude objects with no codes.
print("Excluding {} of {} trials because they have no codes.".format(np.sum(nlp_tb.has_codes == False), nlp_tb.shape[0]))
nlp_tb = nlp_tb.loc[nlp_tb.has_codes == True,:]

# Set index and count trials.
nlp_tb = nlp_tb.set_index("nci_id")
num_trials = nlp_tb.shape[0]
print("Proceeding with {} trials.".format(num_trials))

# Determine features.
code_types = set()
for obj in nlp_tb.codes_obj:
  code_types.update(obj["negated_codes"])
  code_types.update(obj["possible_codes"])
  code_types.update(obj["affirmed_codes"])

# # Create code matrix. For trial i and code j, the entry at (i,j) is "negated",
# # "possible", or "affirmed" if code j is a negated, possible, or affirmed code
# # respectively for trial i.
# code_mat = pd.DataFrame(index=nlp_tb.index, columns=code_types, dtype=object)
# code_mat = code_mat.fillna("-")
# for nci_id in nlp_tb.index:
#   for label in ["negated", "possible", "affirmed"]:
#     for code in nlp_tb.codes_obj.loc[nci_id][label + "_codes"]:
#       code_mat.loc[nci_id,code] = label

# Create three indicator matrices, one for each label ("negated", "possible",
# "affirmed"). For trial i and code j, the entry at (i,j) is 1 if the code is
# in the appropriate list of codes (negated_codes, possible_codes, or
# affirmed_codes), and 0 otherwise.
code_mats = {}
for label in ["negated", "possible", "affirmed"]:
  mat = pd.DataFrame(index=nlp_tb.index, columns=code_types, dtype="float")
  mat = mat.fillna(0.0)
  for nci_id in nlp_tb.index:
    for code in nlp_tb.codes_obj.loc[nci_id][label + "_codes"]:
      mat.loc[nci_id,code] = 1.0
  code_mats[label] = mat

# Stack the indicator matrices next to each other, so there is one dimension
# for each "negated" code, a separate one for each "posible" code, and another
# separate one for each "affirmed" code.
m1, m2, m3 = code_mats["negated"], code_mats["possible"], code_mats["affirmed"]
m1.columns = ["negated_{}".format(c) for c in m1.columns]
m2.columns = ["possible_{}".format(c) for c in m2.columns]
m3.columns = ["affirmed{}".format(c) for c in m3.columns]
concatenated_mat = pd.concat((m1, m2, m3), axis=1)
assert concatenated_mat.shape[0] == num_trials

# # Compute distance measure.
# distance_measure = "cityblock"
# distance_mats = {label: scipy.spatial.distance.cdist(mat.as_matrix(),
#                                                      mat.as_matrix(),
#                                                      distance_measure)
#                  for label, mat in code_mats.items()}
# distance_mat = distance_mats["negated"] + distance_mats["possible"] + \
#                distance_mats["affirmed"]

# Compute distance measure.
distance_measure = "cosine"
#distance_measure = "cityblock"
distance_mat = scipy.spatial.distance.cdist(concatenated_mat.as_matrix(),
                                            concatenated_mat.as_matrix(),
                                            distance_measure)
distance_mat[np.where(distance_mat < 0)] = 0 # hack

# Run t-SNE using the precomputed distance matrix.
tsne = sklearn.manifold.TSNE(metric="precomputed")
embedded = tsne.fit_transform(distance_mat)

# Cluster.
#k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
ac_algo = sklearn.cluster.AgglomerativeClustering(n_clusters=5, affinity="precomputed", linkage="complete")
agglomerative_clustering = ac_algo.fit_predict(1-distance_mat)

# Plot t-SNE and clustering.
cmap = plt.cm.get_cmap("winter", 5)
plt.scatter(embedded[:,0], embedded[:,1], c=agglomerative_clustering, cmap=cmap)
plt.title("Trials in t-SNE space, colored by cluster")
plt.axis('tight')
plt.savefig("firstpass_NLPparsed_clustering.png")

# Make output.
output = pd.DataFrame(index=nlp_tb.index)
output["cluster_id"] = agglomerative_clustering
output["tsne_x"] = embedded[:,0]
output["tsne_y"] = embedded[:,1]
output["codes_text"] = nlp_tb["codes_text"]
output.to_csv("firstpass_NLPparsed_clustering.csv")
