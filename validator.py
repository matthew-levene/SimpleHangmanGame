
def find_matches(letter, word, word_map):
    for index in range(len(word)):
        # If the letter is found at the given index
        if letter == word[index]:
            # For each key in the key set
            for key in word_map.keys():
                # If the letter matches a key in the set
                if letter == key:
                    # Get the index list and append the new index to it
                    index_list = list(word_map[key])
                    index_list.append(index)
                    word_map[key] = index_list