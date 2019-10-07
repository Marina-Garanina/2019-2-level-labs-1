def calculate_frequences(text) :
    dictionary = {}
    text = "".join(word for word in text if word not in ('!', '.', ':', ',', '“', '”', '"', '?', '?!'))
    words = text.split()
    for key in words:
        key = key.lower()
        if key in dictionary:
            value = dictionary[key]
            dictionary[key]=value+1
        else:
            dictionary[key]=1
    return dictionary

def filter_stop_words(dictionary, stopwords):
    filtered_dictionary = dictionary
    for key in list(filtered_dictionary.keys()):
        if key in stopwords:
            del filtered_dictionary[key]
    return filtered_dictionary

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
