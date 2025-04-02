import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from fastcoref import spacy_component
import spacy

def read_epub(file_path):
    # Load the EPUB book
    content = []
    book = epub.read_epub(file_path)
    chapters_unordered = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            asst = item.get_content()
            al = asst.decode('utf-8').replace("\xe2\x80\x9c","")
            ae = BeautifulSoup(al, "html.parser").find_all("div")
            for sec in ae:  chapters_unordered.append(sec.text)
    chapters = chapters_unordered
    chapter_numbers = []
    chapter_numbers_dict = {}
    list_chapters = chapters_unordered
    return list_chapters

# Example usage
epub_file = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelazny_14401.epub"
# Replace with the path to your EPUB file
epub_content = [""]
epub_content = read_epub(epub_file)
# print(epub_content)
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 4000000


nlp.add_pipe(
   "fastcoref", 
   config={'model_architecture': 'LingMessCoref', 'model_path': 'biu-nlp/lingmess-coref', 'device': 'cpu'}
)

for parag in epub_content:
    if parag:
        print("parag is " + parag)
        doc = nlp(  parag, component_cfg={"fastcoref": {'resolve_text': True}})
        nlp = spacy.load("en_core_web_sm")
        print("corefed: " +doc._.resolved_text)
#nlp.add_pipe("fastcoref")

#doc = nlp(text)
#doc._.coref_clusters

#print(doc._.resolved_text)