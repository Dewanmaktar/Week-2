
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet
if __name__ == "__main__":
    test_string = "The quick brown fox jumps over the lazy dog"
    print(is_pangram(test_string))
