n = int(input())
words = []
freq = {}

# Iterate through the input and update the frequency dictionary
for i in range(n):
    word = input().strip()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        words.append(word)

# Output the number of distinct words and their frequencies
print(len(words))
for word in words:
    print(freq[word], end=" ")
print()
