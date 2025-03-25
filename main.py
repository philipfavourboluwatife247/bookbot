from stats import get_num_words, get_number_characters, get_sorted_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_words = get_number_characters(text)
    sorted_dict = get_sorted_dict(char_words)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for character, count in sorted_dict.items():
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
