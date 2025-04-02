import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from fastcoref import spacy_component
import spacy

def read_epub(file_path):
    # Load the EPUB book
    book = epub.read_epub(file_path)
    
    # Initialize an empty string to store the content
    content = ""

    # Iterate through the book's items
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Check if the item is of type 'text'
        
         # Append the item's content (decoded to a string) to 'content'
        soup = BeautifulSoup(item.get_content(), "html.parser")
        content += soup.get_text() + "\n"
            
    return content

# Example usage
epub_file = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelazny_14401.epub"
# Replace with the path to your EPUB file
epub_content = read_epub(epub_file)
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 4000000

nlp.add_pipe(
   "fastcoref", 
   config={'model_architecture': 'LingMessCoref', 'model_path': 'biu-nlp/lingmess-coref', 'device': 'cpu'}
)

doc = nlp(  epub_content, component_cfg={"fastcoref": {'resolve_text': True}})
nlp = spacy.load("en_core_web_sm")
#nlp.add_pipe("fastcoref")

#doc = nlp(text)
#doc._.coref_clusters

print(doc._.resolved_text)