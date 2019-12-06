"""
Basic Sentiment Analysis Project.
sentimentanalysis(s,t,u) takes in a txt file as 's'
takes in the positive words file as 't'
takes in the negative words file as 'u'
"""

def sentimentanalysis(s,t,u):
	N = set()
	P = set()
	with open(u, 'r', errors = 'ignore') as h:
		for line in h:
			line = line.replace("\n", "")
			N.add(line)
	with open(t, 'r', errors = 'ignore') as g:
		for line in g:
			line = line.replace("\n", "")
			P.add(line)
	with open(s, 'r', errors = 'ignore') as f:
		text = f.read()
		text = text.replace("?",".")
		text = text.replace("!",".")
		text = text.replace(",","")
		sentences = text.split(".")

	Negative = 0
	Positive = 0
	Neutral = 0

	for sent in sentences:
		words = set(sent.split(" "))
		negativecnt = len(words.intersection(N))
		positivecnt = len(words.intersection(P))
		if negativecnt > positivecnt:
			Negative += 1
		elif positivecnt > negativecnt:
			Positive += 1
		else:
			Neutral += 1

	print("Positive:", Positive) #prints the number of positive words
	print("Negative:", Negative) #prints the number of negative words
	print("Neutral :", Neutral) #prints the number of neutral words

def main():
	sentimentanalysis("thehoundofthebaskervilles.txt","positivesentimentwords.txt","negativesentimentwords.txt")

main()
