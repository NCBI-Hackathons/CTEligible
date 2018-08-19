import sys

i_wordCounts=dict()
whole_phraseCounts=dict()
ngram_counts=dict()
text_field=0

lineCount=0

with open('../nci_data/dataset1-trials/Hemoglobin_CTEP Trials_072018.tsv', encoding="utf8", errors='ignore') as in_file1:
	for line in in_file1:
		if line.strip()=="":
			break
		fields=line.strip().split("\t")
		if lineCount == 0:
			for i, f in enumerate(fields):
				if f.strip()=="description":
					text_field=i
		lineCount+=1
		if len(fields)<=text_field:
			continue
		words=fields[text_field].lstrip("True:").lstrip("False:").strip().split()
		if tuple(words) in whole_phraseCounts:
			whole_phraseCounts[tuple(words)]+=1
		else:
			whole_phraseCounts[tuple(words)]=1
		max_len=len(words)+1
		study_set=set()
		for i,w in enumerate(words):
			if w.strip() in i_wordCounts:
				i_wordCounts[w.strip()]+=1
			else:
				i_wordCounts[w.strip()]=1
			for x in range(i, max_len):
				if len(words[i:x])<=1:
					continue
				if len(words[i:x])==len(words):
					continue
				study_set.add(tuple(words[i:x]))

			for x in range(0, i):
				if x==i:
					continue
				if len(words[x:i])<=1:
					continue
				study_set.add(tuple(words[x:i]))
		for x in study_set:
			if x in ngram_counts:
				ngram_counts[x]+=1
			else:
				ngram_counts[x]=1

for i,x in enumerate(whole_phraseCounts.keys()):
	score=0
	for y in x:
		score+=i_wordCounts[y]
	print (str(i) +"\t" + " ".join(x) + "\t"+ str(((score/len(x)+whole_phraseCounts[x]))))
