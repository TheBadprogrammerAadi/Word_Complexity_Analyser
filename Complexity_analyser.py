import syllapy
from collections import Counter
import nltk
from nltk.corpus import brown
import pandas as pd

# Download the Brown Corpus for frequency analysis
nltk.download('brown')

# Download the NLTK words corpus
nltk.download('words')

def calculate_complexity(word, word_freq):
    # Length of the word
    length = len(word)
    
    # Frequency of each letter
    letter_freq = Counter(word.lower())
    
    # Number of unique letters
    unique_letters = len(letter_freq)
    
    # Number of syllables
    syllable_count = syllapy.count(word)
    
    # Calculate reciprocal of word frequency
    if word_freq == 0:
        reciprocal_freq = 1  # To avoid division by zero
    else:
        reciprocal_freq = 1 / word_freq
    
    # Calculate complexity score
    complexity_score = (length + unique_letters + syllable_count) * reciprocal_freq
    
    return complexity_score

def main():
    # Get list of English words
    english_words = set(nltk.corpus.words.words())
    
    # Get words and their frequencies from the Brown Corpus
    words = brown.words()
    word_freq = nltk.FreqDist(w.lower() for w in words)
    
    # Create a list to store complexity information
    complexity_data = []
    
    # Iterate through each word and calculate its complexity
    for word, freq in word_freq.items():
        # Check if word is in the English dictionary
        if word.lower() in english_words:
            complexity_score = calculate_complexity(word, freq)
            complexity_data.append((word, freq, complexity_score))
    
    # Create a DataFrame to store the complexity data
    df = pd.DataFrame(complexity_data, columns=['Word', 'Frequency', 'Complexity Score'])
    
    # Sort DataFrame by the 'Word' column
    df.sort_values(by='Word', inplace=True)
    
    # Save DataFrame to an Excel file
    df.to_excel('C:/Users/aadi2/Desktop/Complexity finder/word_complexity_analysis.xlsx', index=False)
    print("Word complexity analysis saved to 'word_complexity_analysis.xlsx'.")

if __name__ == "__main__":
    main()
