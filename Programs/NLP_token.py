import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources if not already downloaded
nltk.download("punkt")
nltk.download("stopwords")

# Sample text for processing
text = "Natural language processing (NLP) is a subfield of artificial intelligence (AI) that deals with the interaction between computers and humans through natural language."

# Tokenization
tokens = word_tokenize(text)

# Stopwords removal
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Print the results
print("Original Text:")
print(text)

print("\nTokenized Text:")
print(tokens)

print("\nAfter Stopwords Removal:")
print(filtered_tokens)

print("\nAfter Stemming:")
print(stemmed_tokens)
