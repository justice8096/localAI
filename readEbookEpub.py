import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

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
print(epub_content[13000:16000])