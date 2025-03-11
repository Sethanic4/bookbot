from stats import get_num_words
from stats import letter_count
from stats import clean_print
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    newdict = clean_print(letter_count(get_book_text(sys.argv[1])))
    for item in newdict:
        print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")
main()