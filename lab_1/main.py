def calculate_frequences(text) :
    if not isinstance(text, str):
        return {}
    work_text = ''
    for el in str(text):
        if el.isalpha() or el == ' ' or el == '\n':
            work_text += el.lower()
    words = work_text.split()
    dictionary = {}
    for key in words:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary

def filter_stop_words(dictionary, stopwords):
    if dictionary and stopwords is not None:
        filtered_dictionary = dictionary.copy()
        for key in dictionary:
            if not isinstance(key, str):
                del filtered_dictionary[key]
        for word in stopwords:
            if word in filtered_dictionary:
                del filtered_dictionary[word]
        return filtered_dictionary
    return {}

def get_top_n (dictionary, top_n):
    list_dictionary = list(dictionary.items())
    list_dictionary.sort(key=lambda i: i[1], reverse=True)
    index = 0
    toped_dictionary = list()
    for el in list_dictionary:
        if index < top_n:
            toped_dictionary.append(list_dictionary[index])
            index += 1
    toped_dictionary = tuple(list_dictionary[:top_n])
    return toped_dictionary

def read_from_file (path_to_file, lines_limit):
    file = open(path_to_file, 'r')
    n = 0
    text = ''
    for line in file:
        if n < lines_limit:
            text += str(line)
            n += 1
    file.close()
    return text

def write_to_file (path_to_file, content):
    file = open(path_to_file, 'w')
    for el in content:
        file.write(el)
        file.write('\n')
    file.close()
