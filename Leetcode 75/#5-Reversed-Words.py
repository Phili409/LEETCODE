sentence1 = "the sky is blue"
sentence2 = "  hello world  "

def reversed_words(sentence:str):
    ss = sentence.strip().split()
    return " ".join(ss[::-1])

print(reversed_words(sentence1))
print(reversed_words(sentence2))
