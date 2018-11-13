from nltk import word_tokenize
from nltk.tag.stanford import StanfordNERTagger
import spacy

print("-----------START-----------")
text = "Rami Eid is studying at Stony Brook University in NY"
tokens = word_tokenize(text)


############################################
## using SpaCy lib
############################################
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

print()
print()
############################################
## using stanford library
############################################
# 3 class:	Location, Person, Organization
# 4 class:	Location, Person, Organization, Misc
# 7 class:	Time, Location, Organization, Person, Money, Percent, Date

model_path = '/home/sachin/lib_backup/stanford_libs/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar_path = '/home/sachin/lib_backup/stanford_libs/stanford-ner/stanford-ner.jar'

english_nertagger = StanfordNERTagger(model_path, jar_path)

ner_tags = english_nertagger.tag(tokens)

print(ner_tags)
############################################

print("-----------FINISH-----------")