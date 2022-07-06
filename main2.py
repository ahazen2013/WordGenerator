import random

WORD_LIST = 'Phonetic Word List.txt'
BAN_LIST = ['.', '-', '/', '&', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
VOWELS = ['a', 'e', 'i', 'o', 'u']
# initial word list from: https://github.com/Alexir/CMUdict/blob/master/cmudict-0.7b

# removes proper nouns, words containing numbers and symbols, and very long words from the data set
def process_text(text):
    i = 0
    while i != len(text):
        word = text[i]
        if '.' in word or '-' in word or "'" in word or '&' in word or '/' in word:
            text.remove(word)
        elif len(word) > 10:
            text.remove(word)
        else:
            i += 1


# analyzes how frequently each letter appears in the word list, as
# well as how frequently each letter immediately follows any given letter
# text is the .txt file, separated into readlines
# lets is the list of Letters
def frequency_analysis(text, lets) -> dict:
    letter_frequency = {}
    for word in text:
        word = word.split()[1:10]
        for letter in range(0, len(word)):
            if word[letter] not in lets.keys():
                lets[word[letter]] = {}
            if letter == 0:
                pass
            else:
                if word[letter] not in lets[word[letter-1]].keys():
                    lets[word[letter - 1]][word[letter]] = 0
                lets[word[letter-1]][word[letter]] += 1
            if word[letter] not in letter_frequency.keys():
                letter_frequency[word[letter]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            letter_frequency[word[letter]][letter] += 1
            letter_frequency[word[letter]][9] += 1
    return letter_frequency


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

    letters = {}

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
        ret = []
        for i in range(random.randint(4, 7)):
            if i == 0:
                number = random.randint(1, letter_totals[i])
                for j in letter_frequency.keys():
                    if number <= letter_frequency[j][i]:
                        ret.append(j)
                        break
            else:
                followers = letters[ret[-1]].copy()
                total = 0
                for j in followers.keys():
                    followers[j] = followers[j] * letter_frequency[j][i]
                    total += followers[j]
                number = random.randint(1, total)
                total = 0
                for j in followers.keys():
                    total += followers[j]
                    if number <= total:
                        ret.append(j)
                        break
        retur.append(ret)
    for i in retur:
        print(i)
        r = ''
        for j in i:
            if len(j) > 2:
                j = j[0:2]
            if j == 'AA':
                r += 'aw (odd) '
            elif j == 'AE':
                r += 'ah (at) '
            elif j == 'AH':
                r += 'uh (hut) '
            elif j == 'AO':
                r += 'oh (boat) '
            elif j == 'AW':
                r += 'ow (cow) '
            elif j == 'AY':
                r += 'eye (hide) '
            elif j == 'DH':
                r += 'th (thee) '
            elif j == 'ER':
                r += 'ur (hurt) '
            elif j == 'IY':
                r += 'ee (eat) '
            else:
                r += j.lower() + ' '
        print(r)

