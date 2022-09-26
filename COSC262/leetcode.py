import string
def checkIfPangram(sentence):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    sentence = list(sentence)
    for i in range(len(sentence)):
        try:
            alphabet_list.remove(sentence[i])
        except:
            continue
    return len(alphabet_list) < 1
print(checkIfPangram("leetcode"))