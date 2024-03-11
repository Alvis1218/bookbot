def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    report(book_text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text = text.lower()
    letter_totals = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,"h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}
    for character in text:
        if character in letter_totals:
            letter_totals[character] += 1
    return letter_totals

def sort_on(dict):
    return dict["num"]

def report(text, path):
    letters = []
    word_sum = word_count(text)
    letter_sum = letter_count(text)
    for letter in letter_sum:
        letters.append({"letter" : letter, "num" : letter_sum[letter]})
    letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---\n{word_sum} words found in the document\n")
    for entry in letters:
        print(f"The '{entry["letter"]}' character was found {entry["num"]} times")
    print("--- End report ---")

main()