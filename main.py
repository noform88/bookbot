with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)

def count_letter():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        text = file_contents.lower()
        letter_dict = {}
        for char in text:
            letter_dict.setdefault(char, 0)
            letter_dict[char] += 1
        return letter_dict
    return(count_letter())

ldict = count_letter()
itemlist = list(ldict.items())
letter_filter = [x for x in itemlist if x[0].isalpha()]
letter_filter = sorted(letter_filter)

def report(letter_filter):
    listx = ""
    for x in letter_filter:      
        listx += (f"The {x[0]} character was found {x[1]} times\n")
    return print(listx)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print("")
report(letter_filter)
