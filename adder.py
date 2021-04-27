#!/usr/bin/env python3

def load_list():
    with open('wordlist.csv', 'r') as file:
        words = [word[:len(word)-2] for word in file.readlines()]
    return words


def add_loop(words: list):
    while True:
        inp = input('Enter word > ').strip()
        if inp == 'exit':
            break
        
        if inp in words:
            print(f'Word {inp} is already in list')
            continue
        
        words.append(inp)
    
    return words


def write_list(words):
    with open('wordlist.csv', 'w') as file:
        file.writelines([word + ',' for word in words])


def main():
    words = load_list()
    
    add_loop(words)   

    write_list(words)


if __name__ == "__main__":
    main()
