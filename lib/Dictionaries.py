import string

def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

sentence = "My name is Wayne."
result = word_frequency(sentence)
print(result)