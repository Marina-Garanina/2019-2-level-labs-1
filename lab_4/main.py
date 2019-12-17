import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    corpus = []
    if not texts or not isinstance(texts, list):
        return corpus
    for text in texts:
        if not isinstance(text, str):
            continue
        clean_text = ''
        text = text.replace('\n', ' ')
        text = text.replace('<br />', ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')
        for symbol in text:
            if symbol.isalpha() or symbol == ' ':
                clean_text += symbol.lower()
        clean_text = clean_text.split()
        corpus.append(clean_text)
    return corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for doc in self.corpus:
            if not isinstance(doc, list):
                continue
            doc_dict = {}
            cleaned_doc = []
            for elem in doc:
                if isinstance(elem, str):
                    cleaned_doc.append(elem)
            for word in cleaned_doc:
                if word not in doc_dict:
                    doc_dict[word] = doc.count(word) / len(cleaned_doc)
            self.tf_values.append(doc_dict)

    def calculate_idf(self):
        if not isinstance(self.corpus, list):
            return {}
        all_words = [el for doc in self.corpus if isinstance(doc, list) for el in doc if isinstance(el, str)]
        words = list(set(all_words))
        cleaned_corpus = []
        for doc in self.corpus:
            if isinstance(doc, list):
                cleaned_corpus.append(doc)
        for word in words:
            frequency = [1 for doc in cleaned_corpus if isinstance(doc, list) and word in doc]
            self.idf_values[word] = math.log(len(cleaned_corpus) / sum(frequency))

    def calculate(self):
        if not isinstance(self.tf_values, list):
            return []
        for doc in self.tf_values:
            new_dict = {}
            for key in doc:
                if key in doc and key in self.idf_values:
                    new_dict[key] = doc[key] * self.idf_values[key]
                else:
                    return []
            self.tf_idf_values.append(new_dict)

    def report_on(self, word, document_index):
        if self.tf_idf_values is None or document_index > len(self.tf_idf_values) - 1 or \
                word not in self.tf_idf_values[document_index]:
            return ()
        word_info = [self.tf_idf_values[document_index][word]]
        the_most_important = list(self.tf_idf_values[document_index].items())
        the_most_important.sort(key=lambda x: x[1], reverse=True)
        ind = -1
        for elem in the_most_important:
            if elem[0] == word:
                ind = the_most_important.index(elem)
                break
        if ind != -1:
            word_info.append(ind)
        return tuple(word_info)


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
