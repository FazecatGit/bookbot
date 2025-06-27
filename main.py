def get_book_text(filepath):
    with open(filepath) as f:
        frank_contents = f.read()
    return frank_contents

def word_counter(text):
    words = text.split()
    return len(words)
    


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_text)
    print (f"{num_words} words found in the document")

main()