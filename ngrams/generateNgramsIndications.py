import sys
#from nltk.stem import WordNetLemmatizer
#import nltk
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math

#stop_words = set(stopwords.words('english'))


#raw_word_count=dict()
#lemma_word_count=dict()
#lemma_raw_connect=dict()
id_uniqueWords=dict()
ngram_counts=dict()

gram2_count=0
gram3_count=0
gram4_count=0
gram5_count=0
gram6_count=0
gram7_count=0
gram7_count=0
gram9_count=0
gram10_count=0

id_count=0



with open(sys.argv[1], encoding="utf8", errors='ignore') as in_file:
	for line in in_file:
		if line.strip()=="":
			break
		id_count+=1
		id_key=line.split("\t")[0]
		fields=line.split("\t")[1:]
		id_uniqueWords[id_key]=set([])
		for f in fields:
			#id_uniqueWords[fields[0]].add(set(word_tokenize(f.strip("True:").strip("False:"))))
			words=word_tokenize(f.lstrip("True:").lstrip("False:").lower())
			max_len=len(words)
			for i,w in enumerate(words):
				if i+1<max_len:
					gram2=tuple([w,words[i+1]])
					gram2_count+=1
					if gram2 in ngram_counts:
						ngram_counts[gram2]+=1
					else:
						ngram_counts[gram2]=1
				if i+2<max_len:
					gram3=tuple([w,words[i+1],words[i+2]])
					gram3_count+=1
					if gram3 in ngram_counts:
						ngram_counts[gram3]+=1
					else:
						ngram_counts[gram3]=1
				if i+3<max_len:
					gram4=tuple([w,words[i+1],words[i+2],words[i+3]])
					gram4_count+=1
					if gram4 in ngram_counts:
						ngram_counts[gram4]+=1
					else:
						ngram_counts[gram4]=1
				if i+4<max_len:
					gram5=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4]])
					gram5_count+=1
					if gram5 in ngram_counts:
						ngram_counts[gram5]+=1
					else:
						ngram_counts[gram5]=1
				if i+5<max_len:
					gram6=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4],words[i+5]])
					gram6_count+=1
					if gram6 in ngram_counts:
						ngram_counts[gram6]+=1
					else:
						ngram_counts[gram6]=1
				if i+6<max_len:
					gram7=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4],words[i+5],words[i+6]])
					gram7_count+=1
					if gram6 in ngram_counts:
						ngram_counts[gram7]+=1
					else:
						ngram_counts[gram7]=1
				if i+7<max_len:
					gram8=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4],words[i+5],words[i+6],words[i+7]])
					gram8_count+=1
					if gram8 in ngram_counts:
						ngram_counts[gram8]+=1
					else:
						ngram_counts[gram8]=1

for k,v in ngram_counts.items():
	if v>1:
		print (str(math.ceil(float(v)/id_count))+"\t"+"\t".join(k))
	else:
		continue
	#if len(k)==2:
		#print ("\t".join(k)+"\t"+str(math.ceil(float(v)/gram2_count)))
		#print (str(math.ceil(float(v)/gram2_count))+"\t" +"\t".join(k))
	#elif len(k)==3:
		#print ("\t".join(k)+"\t"+str(math.ceil(float(v)/gram3_count)))
		#print (str(math.ceil(float(v)/gram2_count))+"\t" +"\t".join(k))
	#elif len(k)==4:
		#print ("\t".join(k)+"\t"+str(math.ceil(float(v)/gram4_count)))
		#print (str(math.ceil(float(v)/gram2_count))+"\t" +"\t".join(k))
	#elif len(k)==5:
		#print ("\t".join(k)+"\t"+str(math.ceil(float(v)/gram5_count)))
		#print (str(math.ceil(float(v)/gram2_count))+"\t" +"\t".join(k))
	#elif len(k)==6:
		#print ("\t".join(k)+"\t"+str(math.ceil(float(v)/gram6_count)))
		#print (str(math.ceil(float(v)/gram2_count))+"\t" +"\t".join(k))



exit()
print ("id\t"+"\t".join(id_uniqueWords.keys()))
for k1,v1 in id_uniqueWords.items():
	avg_list=[]
	for k2,v2 in id_uniqueWords.items():
		avg=(len(v1)+len(v2))/2.0

		avg_list.append(str(int(100*(len(v1.intersection(v2))/avg))))
	print (k2+"\t".join(avg_list))
