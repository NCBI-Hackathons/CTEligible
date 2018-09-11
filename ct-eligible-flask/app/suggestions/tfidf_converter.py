

class TfidfConverter:
    def __init__(self, freq_vectors):
        """

        """
        self.freq_vectors = freq_vectors
        self.term_freq = {}
        self.doc_freq = {}
        self.idf = {}
        self.tfidf = {}

    def generate_tfidf_vectors(self):
        # Calculate TF and DF
        self.populate_term_doc_freq()

        # Calculate IDF

        # Calculate TF-IDF

    def populate_term_doc_freq(self):
        for cluster, freq_vector in self.freq_vectors.items():
            total = float(sum(freq for freq in freq_vector.values()))

            freq_dict = {}
            for term, count in freq_vector.items():
                freq_dict[term] = count / total

                if term in self.doc_freq:
                    self.doc_freq[term] = self.doc_freq[term] + 1.0
                else:
                    self.doc_freq[term] = 1.0

            self.term_freq[cluster] = freq_dict
