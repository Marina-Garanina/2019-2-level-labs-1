import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if not self.storage:
            self.storage[word] = 0
        elif word not in self.storage:
            self.storage[word] = max(self.storage.values()) + 1
        return self.storage[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.storage:
            return -1
        return self.storage.get(word)


    def get_original_by(self, id: int) -> str:
        if isinstance(id, int):
            for key, value in self.storage.items():
                if value == id:
                    return key
        else:
            return 'UNK'
        if id not in self.storage.values():
            return 'UNK'



    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            for elem in corpus:
                self.put(elem)
            return self.storage


class NGramTrie:
    def __init__(self, n):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if isinstance(sentence, tuple):
            new_sent = list(sentence)
            for i, n in enumerate(new_sent[:-self.size + 1]):
                n_gram = []
                identif = 0
                while identif < self.size:
                    n_gram.append(new_sent[i + identif])
                    identif += 1
                n_gram = tuple(n_gram)
                if n_gram in self.gram_frequencies.keys():
                    self.gram_frequencies[n_gram] += 1
                else:
                    self.gram_frequencies[n_gram] = 1
            return 'OK'
        else:
            return 'ERROR'

    def calculate_log_probabilities(self):
        for pair in self.gram_frequencies:
            wanted = pair[0:self.size - 1]
            count = 0
            for key in self.gram_frequencies:
                if wanted == key[0:self.size - 1]:
                    count += self.gram_frequencies[key]
            prob = math.log(self.gram_frequencies[pair] / count)
            self.gram_log_probabilities[pair] = prob

    def predict_next_sentence(self, prefix: tuple) -> list:
        word_1 = []
        if not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        final = list(prefix)
        while True:
            prob = []
            for n_gram in list(self.gram_log_probabilities.keys()):
                if n_gram[:-1] == prefix:
                    prob.append(self.gram_log_probabilities[n_gram])
            if not prob:
                break
            prob.sort(reverse=True)
            prob = prob[0]
            for word, probability in list(self.gram_log_probabilities.items()):
                if prob == probability:
                    word_1 = word[-1]
            final.append(word_1)
            pref_1 = list(prefix[1:])
            pref_1.append(word_1)
            prefix = tuple(pref_1)
        return final


def encode(storage_instance, corpus) -> list:
    code = []
    for sentence in corpus:
        code1 = []
        for element in sentence:
            element = storage_instance.get_id_of(element)
            code1.append(element)
        code.append(code1)
    return code


def split_by_sentence(text: str) -> list:
    corpus = []
    new_text = ''
    if isinstance(text, str) and ' ' in text:
        text = text.replace('\n', ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')
        text = text.replace('!', '.')
        text = text.replace('?', '.')
        if '.' in text:
            for symbol in text:
                if symbol.isalpha() or symbol == ' ' or symbol == '.':
                    new_text += symbol.lower()
    sentences = new_text.split('.')
    while '' in sentences:
        sentences.remove('')
    for element in sentences:
        element = element.split()
        element.insert(0, '<s>')
        element.append('</s>')
        corpus.append(element)
    return corpus
