

class TfidfConverter:
    def __init__(self, freq_vectors):
        """

        """
        self.freq_vectors = freq_vectors
        self.term_freq = {}
        self.idf = {}

    def generate_tfidf_vectors(self):
        for cluster, freq_vector in freq_vectors.items():
