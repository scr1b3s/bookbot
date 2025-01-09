letter_dict = {}

def count_shit(path: str = 'books/frankenstein.txt', letters: dict = letter_dict) -> int:
    n_words = 0
    
    with open(path) as f:
        for line in f:
            n_words += len(line.split())
            for letter in line:
                ctx = letter.lower()
                if (ctx.isalpha()):
                    letters[ctx] = letters.get(ctx, 0) + 1

    return (n_words, letters)

if __name__ == '__main__':
    path = input("Enter path for data: ")
    
    if path == '':
        path = 'books/frankenstein.txt'
    
    word_num, letter_dict = count_shit(path)
    print(f"--- Begin report of {path} ---")
    print(f"{word_num} words found in the document\n")
    
    for key, val in letter_dict.items():
        print(f"The '{key}' character was found {val} times")