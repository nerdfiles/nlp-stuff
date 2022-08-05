import sys 
#import mingus
import spacy
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

def ret(name = "en_core_web_sm"):
    '''
    @usage 
    nlp = spacy.load("en_core_web_lg")
    '''

    nlp = spacy.load(name)
    return nlp

nlp = ret(name = "en_core_web_sm")

content = ''

try:
    content = sys.stdin.readline()
except KeyboardInterrupt:
    sys.stdout.flush()
    pass

text = (content)
DOC = nlp(text)

LABELS_LIST = {}
for ENTITY in DOC.ents:
    LABELS_LIST['LABEL/' + ENTITY.label_] = ENTITY.text

NOUNS = [TOKEN.lemma_ for TOKEN in DOC if TOKEN.pos_ == "NOUN"]
NOUN_PHRASES = [CHUNK.text for CHUNK in DOC.noun_chunks]
VERBS = [TOKEN.lemma_ for TOKEN in DOC if TOKEN.pos_ == "VERB"]

OUT = {
    "phrase": DOC,
    "Ns": NOUNS,
    "NPs": NOUN_PHRASES,
    "Vs": VERBS,
    "LABELs": LABELS_LIST
}

if __name__ == "__main__":
    pp.pprint(OUT)


