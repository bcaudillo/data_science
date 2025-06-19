def count_specific_word(paragraph, word):
    words = paragraph.split()
    count = 0
    i = 0

    while i < len(words):
        w = words[i]
        if w[-1] == ".":
            w = w[:-1]
        if w == word:
            count += 1
        i += 1

    return count

def identify_most_common_word(paragraph):
    if not paragraph:
        return None

    words = paragraph.split()
    word_counts = {}
    most_common = ""
    highest_count = 0

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        if word_counts[word] > highest_count:
            most_common = word
            highest_count = word_counts[word]

    return most_common


def calculate_average_word_length(paragraph):
    words = paragraph.split()
    if not words:
        return 0

    total_length = 0
    word_count = 0

    for word in words:
        if word[-1] in [".", ",", "!", "?"]:
            word = word[:-1]
        total_length += len(word)
        word_count += 1

    return total_length / word_count

def count_sentences(paragraph):
    if not paragraph:
        return 1  
    
    sentence_endings = [".", "!", "?"]
    count = 0
    for char in paragraph:
        if char in sentence_endings:
            count += 1
    return count

def count_paragraphs(paragraph):
    if not paragraph:
        return 1 
    
    paragraphs = paragraph.split("\n\n")
    count = 0
    for p in paragraphs:
        if p != "":
            count += 1
    return count

