def fetch_words(filename, n_array):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) in n_array:
                words.append(word)
    return words