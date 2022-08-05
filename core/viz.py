import spacy
from spacy import displacy
from pprint import pprint

nlp = spacy.load("en_core_web_sm")

import sys

l = sys.argv
file_name = str('./') + str(l[1:2][0])

print(file_name)

# f = open(file_name, "a")
# print(f)
# f.close()


#for line in sys.stdin:
    #content = sys.stdout.write(line)

# try:
#     content = sys.stdin.readline()
# except KeyboardInterrupt:
#     sys.stdout.flush()
#     pass

f = open(file_name)
content = f.readlines()
label = content[0:][0]
pprint(label)
doc = nlp(label)
displacy.serve(doc, style="dep")
f.close()
