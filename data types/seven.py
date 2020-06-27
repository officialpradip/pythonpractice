'''7.	Write a Python function
 that takes a list of words and returns the length of the longest one'''

def longestword(wordslist):
    word_len = []
    for n in wordslist:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(longestword(["Pradip", "InsightWorkshop", "Hello world","Python"]))
