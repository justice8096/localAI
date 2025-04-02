import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def extract_chapters(epub_file):
    # Open the EPUB file
    book = epub.read_epub(epub_file)
    
    chapters = []
    chapters.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" )
    chapters.append("<books>")
    # Iterate through all the items in the EPUB file
    for item in book.items:
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append("<book>")
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            # print("in = [" + item.get_content().decode('utf-8') + "]")
            # Find and extract all paragraph tags
            text = []
            for chapter in soup.find_all('span'):
                # print("text = [" + text + "]")
                new_text = chapter.get_text().strip()
                # print("past = [" + new_text + "]")
                if text != new_text:
                    text = new_text
                    print("new chapter")
                    chapters.append("<chapter>" + text + "</chapter>")
            chapters.append("</book>")
    chapters.append("</books>")    
    return chapters


def write_to_utf8(chapters, output_file):
    # Write the list of paragraphs to a UTF-8 encoded file
    with open(output_file, 'w', encoding='utf-8') as f:
        for chapter in chapters:
            f.write(chapter + '\n')


# Example usage
if __name__ == "__main__":
    epub_file = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelazny_14401.epub"  # Replace with your EPUB file path
    output_file = "C:\\Users\\justi\\Downloads\\The Great Book of Amber - Roger Zelanzy.xml"  # Replace with your desired output file path
    chapters = extract_chapters(epub_file)
    write_to_utf8(chapters, output_file)
    print(f"Extracted {len(chapters)} paragraphs and saved to {output_file}.")