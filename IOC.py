
import numpy as np
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N_of_english_chars = 26
# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def decrypt(key, message):
    result = ""
    list = []
    for letter in message:
        if letter in letters: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (letters.find(letter) - key) % len(letters)

            result = result + letters[letter_index]
        else:
            result = result + letter

    list = result
    return list
#
# Python code to implement
# Vigenere Cipher

# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

def calculate_frequency(test):
    all_freq = {}
    for i in test:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    # printing result
    return all_freq
def sum_frequency(sum_frequency):
    calculate = 0
    N=0
    for key, value in sum_frequency.items():
        calculate += value * (value - 1)
        N +=value
    IC = calculate / (float(N) * (N - 1))
    return IC*26

def average_IC_return_number(length, text):
    split = [''] * length # string with empty spaces by key size
    sum = 0
    for n, letter in enumerate(text):
        split[n % length] += letter
    for i in range(length):
        sum += sum_frequency(calculate_frequency(split[i]))
    return sum / length,


def calc_ic_for_each_key():
    key_length = 1
    average = []
    for n in range(1, 15):
        average += average_IC_return_number(n, test_str)
    max = abs(1.73 - np.float_(average[0]))
    for n in range(len(average)):
        item = abs(1.73 - np.float_(average[n]))
        if max > item :
            max = item
            key_length = n+1 #array starts from 0 place
    print ("The key length is:" , key_length )
    return key_length

def split_string_return_string(length, text):
    split = [''] * length # string with empty spaces by key size
    sum = 0
    for n, letter in enumerate(text):
        split[n % length] += letter
    return split

def calculate_X_formula(key_frnq):
    x = 0
    lol = {k: v * key_frnq[k] for k, v in englishLetterFreq.items() if k in key_frnq}
    for key, value in lol.items():
        x += value
    return x

# Driver code
# string taken from https://en.wikipedia.org/wiki/Index_of_coincidence
if __name__ == "__main__":
    string = "MUSTCHANGEMEETINGLOCATIONFROMBRIDGETOUNDERPASSSINCEENEMYAGENTSAREBELIEVEDTOHAVEBEENASSIGNEDTOWATCHBRIDGESTOPMEETINGTIMEUNCHANGEDXX"
    keyword = "EVERY"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
          originalText(cipher_text, key))

# initializing string
# string taken from https://en.wikipedia.org/wiki/Index_of_coincidence
test_str = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"




key_length_was_found = calc_ic_for_each_key()

stirng_key_find = split_string_return_string(key_length_was_found, test_str)


max_x = 0
founded_key_letters = []
total_key= ""
for g in range(0,key_length_was_found):
    for i in range(0,N_of_english_chars):
        a = []
        a = decrypt(i,stirng_key_find[g])
        a_a = calculate_frequency(a)
        a_a_a = calculate_X_formula(a_a)
        if max_x < a_a_a:
            max_x = a_a_a
            founded_key_letters = letters[i]
    total_key += founded_key_letters
    max_x = 0

print "The 'KEY' is: ",total_key
new_key = generateKey(test_str,total_key)
print 'OriginalText is:' ,originalText(test_str,new_key)


