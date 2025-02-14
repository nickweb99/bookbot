
def read(book):
    with open(book) as f:
      file_contents = f.read()
    return file_contents

def count(contents):
    return len(contents.split())

def letters(contents):
    proper = contents.lower()
    groups = {}
    for char in proper:
        if char in groups:
            groups[char] += 1
        else:
            groups[char] = 1
    return groups


book = "books/frankenstein.txt"
def main():
    contents = read(book)
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{count(contents)} words found in the document")
    chars = letters(contents)
    for char in chars:
        if char.isalpha() == True:
            print(f"The '{char}' character was found '{chars[char]}' times")

main()



