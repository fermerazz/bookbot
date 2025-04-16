
def counting_words(book):
    counter = 0
    book_words = book.split()
    for wor in book_words:
        counter  += 1
    return counter

def counting_characters(book):
    words_dict = {}
    for character in book:
        character = character.lower()
        if character in words_dict:
            words_dict[character] += 1
        else:
            words_dict[character] = 1
    return words_dict

def sort_on(data): 
    return data["count"]

def sort_dict(data):
     data.sort(reverse=True, key=sort_on)
     return data

def get_character_list(words_dict):
    character_list = [{"character": char, "count": count} for char, count in words_dict.items()]
    return character_list