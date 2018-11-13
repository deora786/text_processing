from nltk.parse.stanford import StanfordDependencyParser
import spacy

print("-----------START-----------")
text = "reset my password"

############################################
## using SpaCy lib
############################################
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])

print()
print()
############################################
## using stanford library
############################################

path_to_models_jar = '/home/sachin/lib_backup/stanford_libs/stanford-parser/stanford-parser-3.9.2-models.jar'
path_to_jar = '/home/sachin/lib_backup/stanford_libs/stanford-parser/stanford-parser.jar'
#model_path = '/home/sachin/lib_backup/stanford_libs/stanford-coreNLP-english/edu/stanford/nlp/models/lexparser/englishRNN.ser.gz'


english_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

parse_tags = english_parser.raw_parse(text)

#print(parse_tags.tree())
dep = parse_tags.__next__()

dep_tags = list(dep.triples())

print (dep_tags)

############################################

print("-----------FINISH-----------")