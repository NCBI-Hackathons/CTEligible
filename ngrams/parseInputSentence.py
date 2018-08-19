import sys
#from nltk.stem import WordNetLemmatizer
#import nltk
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

userInput_ngram=set()
dict_ngrams_score=dict()
sub_ngrams_link=dict()


with open("./HIV_ngrams.tsv", encoding="utf8", errors='ignore') as in_file1:
	for line in in_file1:
		if line.strip()=="":
			break
		fields=line.strip().split("\t")
		dict_ngrams_score[tuple(fields[1:])]=int(fields[0])
		if len(fields[1:])>2:
			sub_ngrams_link[tuple(fields[1:][1:])]=tuple([fields[1:]])
			sub_ngrams_link[tuple(fields[1:][:-1])]=tuple([fields[1:]])

if sys.argv[1].strip()=="":
	exit()
words=word_tokenize(sys.argv[1].strip().lower())
max_len=len(words)
for i,w in enumerate(words):
	if i+1<max_len:
		gram2=tuple([w,words[i+1]])
		userInput_ngram.add(gram2)
	if i+2<max_len:
		gram3=tuple([w,words[i+1],words[i+2]])
		userInput_ngram.add(gram3)
	if i+3<max_len:
		gram4=tuple([w,words[i+1],words[i+2],words[i+3]])
		userInput_ngram.add(gram4)
	if i+4<max_len:
		gram5=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4]])
		userInput_ngram.add(gram5)
	if i+5<max_len:
		gram6=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4],words[i+5]])
		userInput_ngram.add(gram5)
	if i+6<max_len:
		gram7=tuple([w,words[i+1],words[i+2],words[i+3],words[i+4],words[i+5],words[i+6]])
		userInput_ngram.add(gram7)

scroredSentence=userInput_ngram.intersection(dict_ngrams_score.keys())
#print (userInput_ngram)
#print (dict_ngrams_score.keys())
score=0
for i in scroredSentence:
	score+=dict_ngrams_score[i]

print (score)

#plus1gram=userInput_ngram.intersection(sub_ngrams_link.keys())

#for gram in plus1gram:
#	print ("\t".join(gram)+"\t:\t"+"\t".join(sub_ngrams_link[gram])+"\t:\t"+"\t".join(dict_ngrams_score[sub_ngrams_link[gram]])
