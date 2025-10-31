def get_book_text(FILE_PATH: str) -> str:
    with open(FILE_PATH) as file:
        file_contents = file.read()
    
    return file_contents

def word_count(text: str) -> int:
    return len(text.split())

def main():
    content = get_book_text("books/frankenstein.txt")
    count = word_count(content)
    print(f"Found {count} total words")

main()