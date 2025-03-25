def get_num_words(text):
    words = text.split()
    return len(words)

def get_number_characters(text):
    text = text.lower()
    no_duplicate = set(text)
    dict_each_char = {char: text.count(char) for char in no_duplicate}
    return dict_each_char

def get_sorted_dict(characters):
    return dict(sorted(characters.items(), key=lambda character: character[1], reverse=True))
