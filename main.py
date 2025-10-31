from stats import word_count, char_count, sorted_dict
import sys

def get_book_text(FILE_PATH: str) -> str:
    with open(FILE_PATH) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    BOOK_PATH = sys.argv[1]
    content = get_book_text(BOOK_PATH)

    count = word_count(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    list_of_dicts = sorted_dict(char_count(content))
    

    for dictionary in list_of_dicts:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")


main()