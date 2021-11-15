import sys 
import spacy


# setup
nlp = spacy.load("en_core_web_sm")

# init
content = ''

# input
try:
    content = sys.stdin.readline()
except KeyboardInterrupt:
    sys.stdout.flush()
    pass

# str = '''through planted empowered consistent racial claims inverse fantasy builds 
# monetary relations writer phenomenal wherein reminds rubric desiring suffering 
# antagonisms ignored texualisation coercive absolutely morally anti-worker 
# ontology despot-matrix annihilation antagonism hypothetical community repress 
# brings pastime unreasonable anthropology single virtual forgotten predicated 
# subjectivity generation question funda-dominance dissemination threat 
# generating ideology desire life-saving formal constitutes purchase metaphors 
# shards monetary relation crowded enforcement warehoused doggedly actually 
# beyond diagnosis pedagogical superstructure non-being modern regulation 
# strategy workers excuse self-awareness police capitalist violence economy 
# present qualified include progressively construct apprenticeship formations 
# unspeakable contains beginning assumes assume economy shipbuilding affairs 
# faltering consistency analysis target acquiescent tautology destabilised 
# invitations examines productivity treaties structured seemingly demanded 
# perfected popular repress monument instantiates emancipatory except produced 
# habits crevice racism structures'''

str = '''
insights of difference reinvigorated novel struggles within perils constituted 
to reveal allowancs for subjective states translated into places everywhere 
positioned from elaborate laboratory strategies, within which culinary 
mutilation possesses catalyst of reason without marked dimension to 
disarticulate berkeleyan expressivities for rhyming consideration now 
constructive under performative struggle along pastimes of anti-black 
warehouses of literature madness and masses traded regressive between a 
capitalist shipbuilding that eventually amasses the willing agriculture 
formation of fantasies totally universal in ontology of travel which reminds 
alcoholic suggestions that another possession of colonies maintain the 
extensional concentricity of ultimate participatory continuation before 
molecular gestures breed purpose
'''

str = content
## etl
text = (str)
## proces
doc = nlp(text)

## output
print(doc)

#import pdb; pdb.set_trace()

## outcome
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

if __name__ == "__main__":
    for entity in doc.ents:
        print(entity.text, 'LABEL' + entity.label_)
