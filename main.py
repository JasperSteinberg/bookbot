from stats import word_count, char_count, sorted_dict

def get_book_text(FILE_PATH: str) -> str:
    with open(FILE_PATH) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    count = word_count(content)
    print(f"Found {count} total words")

    char_count_dict = char_count(content)

    print(sorted_dict(char_count_dict))

main()