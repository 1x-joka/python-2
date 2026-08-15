# ============== LIST AND DICTIONARY COMPREHENSIONS ==============
# -> A Comprehensions is a quick way to build a list or a dictionary from data you already have

def main():
    words = get_words("address.txt") # this function (get_words) just open up this file and returns to me a list of individual words found in this file
    lowercase_words = [word.lower() for word in words if (len(word)) > 4] # "i want a list, and this list will be composed of the word lower element for each word that I have in words" = I'm asking for every word that exists in my words list and returning me lower individually
    # if (len(word) > 4) = when size word is greater than 4

    counts = {word: words.count(word) for word in lowercase_words} # my key "word" goes corresponding value to be the number of times who this word appeared in file based on the list "lowercase_words"
    
    save_counts(counts)

main()