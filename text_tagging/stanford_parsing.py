from nltk.parse.stanford import StanfordParser


print("-----------START-----------")
#text = "Rami Eid is studying at Stony Brook University in NY"
#text = 'Is there a career Advisor I can speak with ?'
text = 'where do I go to change my password'
############################################
## using stanford library
############################################

model_path = '/home/sachin/lib_backup/stanford_libs/stanford-parser/stanford-parser-3.9.2-models.jar'
jar_path = '/home/sachin/lib_backup/stanford_libs/stanford-parser/stanford-parser.jar'

english_parser = StanfordParser(model_path, jar_path)

parse_tags = english_parser.raw_parse(text)

parse_tree = parse_tags.__next__()

for i in parse_tags:
	print (i)
#tag = str()
#tag = parse_tree[0].label()
#print (tag[:10])
#if tag == 'SBARQ' or tag == 'SQ':
#	print("True")
#else:
#	print("False")
############################################

