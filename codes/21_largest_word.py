def largest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    cleaned_words = []

    for word in words:
        cleaned = ""

        for char in word:
            if char.isalnum():
                cleaned += char

        if cleaned:
            cleaned_words.append(cleaned)

    if not cleaned_words:
        return ""

    largest = cleaned_words[0]

    for word in cleaned_words:
        if len(word) > len(largest):
            largest = word

    return largest