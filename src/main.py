import sys
import re

def find_coincidences(word, plate):
    pattern = "[a-zA-Z]*" + plate[0] + "[a-zA-Z]*" + plate[1] + "[a-zA-Z]*" + plate[2] + "[a-zA-Z]*"
    if re.match(pattern, word):
        return True
    return False


def main():
    fo = open("../dict/words", 'r')
    words = fo.read()
    words = words.split("\n")

    for arg in sys.argv[1:]:
        print(arg)
        results = list(filter(lambda word: find_coincidences(word, arg), words))
        if len(results) > 0:
            print(results)
        else:
            print("No results")
        print("-----------------------------")


if __name__ == "__main__":
    main()
