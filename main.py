from stats import counting_words, counting_characters, get_character_list, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text(file_path)
    num_words = counting_words(book)
    words_dict = counting_characters(book)
    character_list = get_character_list(words_dict)
    sorted_character_list = sort_dict(character_list)
   
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    

    for entry in sorted_character_list:
        char = entry["character"]
        count = entry["count"]
        if char.isalpha():  
            print(f"{char}: {count}")

    print("============= END ===============")

main()

