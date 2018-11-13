from nltk import word_tokenize
from nltk.tag.stanford import StanfordPOSTagger
from nltk import pos_tag

print("-----------START-----------")
text = 'this is stanford postagger in nltk for python users'
tokens = word_tokenize(text)


############################################
## using NLTK lib
############################################

pos_tags = pos_tag(tokens)

print(pos_tags)


############################################
## using stanford library
############################################
model_path = '/home/sachin/lib_backup/stanford_libs/stanford-postagger/models/english-bidirectional-distsim.tagger'
jar_path = '/home/sachin/lib_backup/stanford_libs/stanford-postagger/stanford-postagger.jar'

english_postagger = StanfordPOSTagger(model_path, jar_path)

pos_tags = english_postagger.tag(tokens)

print(pos_tags)
############################################

print("-----------FINISH-----------")