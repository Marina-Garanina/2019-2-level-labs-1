f = open('data.txt', 'r')
text = f.read().strip()
text = "".join(word for word in text if word not in ('!','.',':', ',', '“', '”', '"', '?', '?!'))

stopwords = ('the', 'a', 'an', 'or', 'and', 'to', 'are', 'is',)
top_n = 6
path_to_file = 'report.txt'

def calculate_frequences(text) :
    dictionary = {}
    words = text.split()
    for key in words:
        key = key.lower()
        if key in dictionary:
            value = dictionary[key]
            dictionary[key]=value+1
        else:
            dictionary[key]=1
    return dictionary
dictionary = calculate_frequences(text)
print (dictionary)

def filter_stop_words(dictionary, stopwords):
    filtered_dictionary = dictionary
    for key in list(filtered_dictionary.keys()):
        if key in stopwords:
            del filtered_dictionary[key]
    return filtered_dictionary
filtered_dictionary = filter_stop_words(dictionary, stopwords)
print (filtered_dictionary)

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
content = get_top_n (dictionary, top_n)
print (content)

def write_to_file (path_to_file, content):
    with open('report.txt', 'w') as file:
        print(content, file=file, sep='\n')

write_to_file (path_to_file, content)
