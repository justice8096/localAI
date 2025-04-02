import xml.etree.ElementTree as ET
from fastcoref import spacy_component
import spacy

# Function to read and parse an XML file
def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)  # Parse the XML file
        root = tree.getroot()       # Get the root element
        print("Root = " + root.tag)
        return root
    except ET.ParseError as e:
        print("Error parsing XML:", e)
        return None

# Function to retrieve and display elements
def display_elements(nlp, root, outf):
    if root is not None:
        for book in root.findall("book"):
            outf.write("<book>\n")
            for chapter in book.findall("chapter"):
                p = coref(nlp, chapter.text)
                if p:
                    outf.write("<chapter>" + chapter.text + "</chapter>\n")
                    outf.write("<nlp stage=\"1\">" + coref(nlp, p) + "</nlp>\n")
            outf.write("</book>\n")
                

def coref(nlp, parag):
    if parag:
        print("parag is " + parag)
        doc = nlp(  parag, component_cfg={"fastcoref": {'resolve_text': True}})
        nlp = spacy.load("en_core_web_sm")
        return doc._.resolved_text

# Path to the XML file
file_path = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelanzy.xml"
coref_path = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelanzy.coref.xml"

# Tag to search for
tag_to_find = "chapter"

nlp = spacy.load("en_core_web_lg")
nlp.max_length = 4000000

nlp.add_pipe(
   "fastcoref", 
   config={'model_architecture': 'LingMessCoref', 'model_path': 'biu-nlp/lingmess-coref', 'device': 'cpu'}
)

# Parse the XML file and retrieve elements
root_element = parse_xml(file_path)
with open(coref_path, 'w', encoding='utf-8') as outf:
    outf.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" )
    outf.write("<books>\n")
    display_elements(nlp, root_element, outf)
    outf.write("</books>\n")
    