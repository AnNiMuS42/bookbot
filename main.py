from stats import word_count, char_count, gen_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return(f.read())

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = word_count(text)
    chars = char_count(text)
    print(f"Found {words} total words")
    gen_report(text)

main()