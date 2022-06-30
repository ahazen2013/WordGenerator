import random

WORD_LIST = 'new_list.txt'
BAN_LIST = ['.', '-', '/', '&', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
VOWELS = ['a', 'e', 'i', 'o', 'u']
# initial word list from: https://github.com/dwyl/english-words/blob/master/words_alpha.txt


# class variables include the letter that an instance represents,
# and the frequency with which each letter follows it
class Letter:
    key = ''

    def __init__(self, k):
        self.followers = {}
        for i in range(26):
            self.followers[chr(97+i)] = 0
        self.key = k

    def add_follower(self, follower):
        self.followers[follower] += 1

    def __str__(self):
        return self.key + ': ' + str(self.followers)


# removes proper nouns, words containing numbers and symbols, and very long words from the data set
def process_text(text):
    i = 0
    while i != len(text):
        word = text[i]
        if '.' in word or '-' in word or "'" in word or '&' in word or '/' in word or\
                '0' in word or '1' in word or '2' in word or '3' in word or '4' in word or\
                '5' in word or '6' in word or '7' in word or '8' in word or '9' in word:
            text.remove(word)
        elif ord(word[0]) < 97:
            text.remove(word)
        elif len(word) > 10:
            text.remove(word)
        else:
            i += 1


# analyzes how frequently each letter appears in the word list, as
# well as how frequently each letter immediately follows any given letter
def frequency_analysis(text, lets) -> dict:
    letter_frequency = {}
    for i in range(26):
        letter_frequency[chr(97+i)] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for word in text:
        word = word.strip().lower()
        for letter in range(len(word)):
            if letter == 0:
                pass
            else:
                lets[ord(word[letter-1])-97].add_follower(word[letter])
            letter_frequency[word[letter]][letter] += 1
            letter_frequency[word[letter]][9] += 1
    return letter_frequency


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = open(WORD_LIST)
    words = obj.readlines()
    obj.close()

    # process_text(words)       # only necessary when running the program the first time
    # fp = open(r'new_list.txt', 'w')
    # for i in words:
        # fp.write(i)
    # words = fp.readlines()
    # fp.close()

    letters = []
    for i in range(26):
        letters.append(Letter(chr(97+i)))

    letter_frequency = frequency_analysis(words, letters)
    letter_totals = [0, 0]
    for i in letter_frequency.keys():
        for j in range(2):
            letter_totals[j] += letter_frequency[i][j]
    for i in range(2):
        total = 0
        for j in letter_frequency.keys():
            total += letter_frequency[j][i]
            letter_frequency[j][i] = total

    retur = []
    for p in range(10):
        ret = ''
        for i in range(random.randint(4, 7)):
            if i == 0:
                number = random.randint(1, letter_totals[i])
                for j in letter_frequency.keys():
                    if number <= letter_frequency[j][i]:
                        ret += j
                        break
            else:
                followers = letters[ord(ret[-1])-97].followers.copy()
                total = 0
                for j in followers.keys():
                    followers[j] = followers[j] * letter_frequency[j][i]
                    total += followers[j]
                number = random.randint(1, total)
                total = 0
                for j in followers.keys():
                    total += followers[j]
                    if number <= total:
                        ret += j
                        break
        retur.append(ret)
    for i in retur:
        print(i)
