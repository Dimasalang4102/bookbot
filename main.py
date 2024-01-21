def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    words = file_contents.split()
    count = len(words)
    chars = {}
    for letter in file_contents.lower():
        if letter not in chars:
            chars[letter] = 1
        else:
            chars[letter] += 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document.\n")
    for char in chars:
        print(f"The \'{char}\' character was found {chars[char]} times")
    print("--- End report ---")
        
main()
