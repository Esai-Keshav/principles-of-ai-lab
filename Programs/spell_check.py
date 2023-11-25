import nltk
from nltk.corpus import words

nltk.download("words")

# Load the NLTK words corpus as a set
english_words = set(words.words())


def spell_check(text):
    # Tokenize the input text
    words_to_check = nltk.word_tokenize(text)

    # Check each word in the text against the NLTK English words corpus
    misspelled_words = [
        word for word in words_to_check if word.lower() not in english_words
    ]

    return misspelled_words


# Input from the user
input_text = input("Enter a sentence for spell checking: ")

# Perform spell checking
misspelled_words = spell_check(input_text)

if len(misspelled_words) > 0:
    print("\nMisspelled words:")
    for word in misspelled_words:
        print(word)
else:
    print("\nNo misspelled words found.")
