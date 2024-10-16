## 45. find the number of palindrome words in a Given String = "dad mom child dad";
# Find all the palindrome words If there are palindrome words , 
# print the word whose occurrence is more than 1(sentence palindrome)


def is_palindrome(word):
    return word == word[::-1]

def find_palindrome_words(input_string):
    words = input_string.split()
    palindrome_words = {}
    
    for word in words:
        if is_palindrome(word):
            if word in palindrome_words:
                palindrome_words[word] += 1
            else:
                palindrome_words[word] = 1
    print(palindrome_words)
    return palindrome_words

input_string = "dad mom child dad"
palindromes = find_palindrome_words(input_string)

# Print the palindromes that occur more than once
for word, count in palindromes.items():
    if count > 1:
        print(word)
