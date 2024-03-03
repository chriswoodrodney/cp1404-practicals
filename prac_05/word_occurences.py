"""
name: CHRISWOOD RODNEY OKWIIRI
file: word_occurences
time estimate: 25-35 minutes
"""
def count_word_occurrences(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def main():
    user_input = input("Enter a string: ")
    word_counts = count_word_occurrences(user_input)

    # Sort the dictionary by keys
    sorted_word_counts = sorted(word_counts.items())

    # Find the longest word length for formatting
    max_word_length = max(len(word) for word, _ in sorted_word_counts)

    # Print word counts with aligned columns
    for word, count in sorted_word_counts:
        print(f"{word:{max_word_length}} : {count}")

if __name__ == "__main__":
    main()
