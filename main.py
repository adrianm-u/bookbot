from stats import get_num_words, count_chars, sorted_dictionaries
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(): 
    #validate CLI args count
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_individual_chars = count_chars(text)
    sorted_num_chars = sorted_dictionaries(num_individual_chars)

    # output report
    print(f"{'='*12} BOOKBOT {'='*12}")
    print(f"{'-'*11} Word Count {'-'*11}")
    print(f"Found {num_words} total words")
    print(f"{'-'*9} Character Count {'-'*9}")
    for items in sorted_num_chars:
        if items["char"].isalpha() == True:
           print(f"{items['char']}: {items['num']}")  
    print(f"{'='*12} END {'='*12}")
    
        
main()


