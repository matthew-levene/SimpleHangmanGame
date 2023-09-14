
def sort_map(word_map):
    sorted_list = []
    for key in word_map:
        index_list = list(word_map[key])
        for index in index_list:
            sorted_list.insert(index, key)

    return sorted_list
