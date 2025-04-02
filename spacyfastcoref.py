from fastcoref import spacy_component
import spacy


text = 'Alice goes down the rabbit hole. Where she would discover a new reality beyond her expectations.'

nlp = spacy.load("en_core_web_sm")
#nlp.add_pipe("fastcoref")

#doc = nlp(text)
#doc._.coref_clusters

nlp.add_pipe(
   "fastcoref", 
   config={'model_architecture': 'LingMessCoref', 'model_path': 'biu-nlp/lingmess-coref', 'device': 'cpu'}
)

doc = nlp(      # for multiple texts use nlp.pipe
   text, 
   component_cfg={"fastcoref": {'resolve_text': True}}
)
nlp = spacy.load("en_core_web_sm")
#nlp.add_pipe("fastcoref")

#doc = nlp(text)
#doc._.coref_clusters

nlp.add_pipe(
   "fastcoref", 
   config={'model_architecture': 'LingMessCoref', 'model_path': 'biu-nlp/lingmess-coref', 'device': 'cpu'}
)

doc = nlp(      # for multiple texts use nlp.pipe
   text, 
   component_cfg={"fastcoref": {'resolve_text': True}}
)

print(doc._.resolved_text)
# > "Alice goes down the rabbit hole. Where Alice would discover a new reality beyond Alice's expectations."