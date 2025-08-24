from stats import get_num_words, get_num_char, sort_dic
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    content = get_book_text(sys.argv[1])
    result = get_num_char(content)
    result2 = sort_dic(result)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    print("--------- Character Count -------")
    for i in result2:
        print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")
    
    

if __name__ == "__main__":
    main()
