
sentence = input()

words = sentence.split()

# Preserve punctuation at the end of the sentence
punctuation = ""
if words and words[-1][-1] in ".!?":
    punctuation = words[-1][-1]
    words[-1] = words[-1][:-1]

# Reverse the order of words
reversed_words = words[::-1]

print(" ".join(reversed_words) + punctuation)
