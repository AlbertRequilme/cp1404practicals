"""
Word Occurrences
Estimated time: ~20 minutes
Actual Time: 22 minutes
"""


def main():
    """This function will ask for the user's input and print the text counting each word."""
    text = input("Text: ")
    word_count = count_words(text)
    sort_words(word_count)


def count_words(text):
    """This function will count the words by placing them in an empty dictionary"""
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def sort_words(word_counts):
    """This function will sort and align the words neatly"""
    max_word_length = max(len(word) for word in word_counts)
    sorted_words = sorted(word_counts.keys())
    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")


main()
