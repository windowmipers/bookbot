def main():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
    words = book_contents.split()
    letters = {}
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in alphabet:
        letters[letter] = 0
    for word in words:
        lowered = word.lower()
        for c in lowered:
            if c in alphabet:
                letters[c] += 1
    letter_list = chars_dict_to_list(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for s in letter_list:
        print(f"The '{s['char']}' character was found {s['num']} times")
    print("--- End report ---")

    # print(letters)
    # print(book_contents)
    # print(len(words))
def sort_on(d):
    return d["num"]
def chars_dict_to_list(dict):
    letters_list = []
    for ch in dict:
        letters_list.append({"char": ch, "num": dict[ch]})
        letters_list.sort(reverse=True, key=sort_on)
    return letters_list



        
        

main()