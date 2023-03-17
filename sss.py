n = int(input())

# create a dictionary to store the frequency of each word
word_freq = {}

# iterate through the n words
for i in range(n):
    word = input().strip()
    
    # if the word is not in the dictionary, add it with frequency 1
    if word not in word_freq:
        word_freq[word] = 1
        
    # if the word is already in the dictionary, increment its frequency
    else:
        word_freq[word] += 1

# output the number of distinct words and their frequencies
print(len(word_freq))
for word in word_freq:
    print(word_freq[word], end=' ')
print()
