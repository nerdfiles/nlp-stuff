import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

#str = '''through planted empowered consistent racial claims inverse fantasy builds monetary relations writer phenomenal wherein reminds rubric desiring suffering antagonisms ignored texualisation coercive absolutely morally anti-worker ontology despot-matrix annihilation antagonism hypothetical community repress brings pastime unreasonable anthropology single virtual forgotten predicated subjectivity generation question funda-dominance dissemination threat generating ideology desire life-saving formal constitutes purchase metaphors shards monetary relation crowded enforcement warehoused doggedly actually beyond diagnosis pedagogical superstructure non-being modern regulation strategy workers excuse self-awareness police capitalist violence economy present qualified include progressively construct apprenticeship formations unspeakable contains beginning assumes assume economy shipbuilding affairs faltering consistency analysis target acquiescent tautology destabilised invitations examines productivity treaties structured seemingly demanded perfected popular repress monument instantiates emancipatory except produced habits crevice racism structures'''
#str = '''insights of difference reinvigorated novel struggles within perils constituted to reveal allowancs for subjective states translated into places everywhere positioned from elaborate laboratory strategies, within which culinary mutilation possesses catalyst of reason without marked dimension to disarticulate berkeleyan expressivities for rhyming consideration now constructive under performative struggle along pastimes of anti-black warehouses of literature madness and masses traded regressive between a capitalist shipbuilding that eventually amasses the willing agriculture formation of fantasies totally universal in ontology of travel which reminds alcoholic suggestions that another possession of colonies maintain the extensional concentricity of ultimate participatory continuation before molecular gestures breed purpose'''
#str = '''consider metaphors industry transaction tautology existing bodies extend premeditated topics unflinching deprivation invitation reveals forces gaining interventions dynamics translated corroborates subordinated tional expression suggest rather lockdown releases appropriated deeply optimistic racism purpose exists rescues contain exploited pastime illustrates possess planted trans- possibility dismantles emancipatory organised represents explores nemesis spontaneous threat confronting ourselves prisoners contains purpose became derivative individual terrain life-saving mixture difficult gories divided minute qualitatively purposes raised sutured spiritual according calling wounds possessing interventions institutional ensues produce narrativised strata hegemonic extend branded future'''
#str = '''decadence deniable informative refutation idleness crafts bloody to-day compact examples spawned problems thematically insignificant desirable environing rendering purpose frames mistake strict undertakes emerging describes forefathers teleological dissertations romance discredit steered duties pretense proposes inject persistently farthest pertain rethinking industrial alienate curricular repeats preoccupation centrality stratification allows practitioner mountains manoeuver speaks mythical encyclopedic devaluation collectivity detracting corrective publicized dissecting paralyzing invites proven limiting preparations peculiar yellow reformed uncultivated daemonization science convey greater cohesion trends addressed reassuring signals erasures political nurture sharing functionality thousands exclusivity theorization comprised industrialists sexism appearance presumes presumably remain reservoir borders oracle inferior slightest indispensable answers nation-state weighted disposal content describes boldly appropriation transport zealous outlooks stigmatization horizons respectively automatically encounters vessels encased example detracting interrogate unnamed endowing'''

import sys

content = ''

#for line in sys.stdin:
    #content = sys.stdout.write(line)

try:
    content = sys.stdin.readline()
except KeyboardInterrupt:
    sys.stdout.flush()
    pass

doc = nlp(content)

displacy.serve(doc, style="dep")
