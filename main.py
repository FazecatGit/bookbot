import sys
from stats import word_counter, count_char, cleaner

def get_book_text(filepath):
    with open(filepath) as f:
        frank_contents = f.read()
    return frank_contents

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_words = word_counter(book_text)
    char_counts = count_char(book_text)
    clean = cleaner(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print(f"Found {num_words} total words")

    for item in clean:
        print(f"{item['char']}: {item['num']}")

main()