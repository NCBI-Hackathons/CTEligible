from suggestions_utils import get_cluster_text
from suggestions_utils import clean_text
from suggestions_utils import convert_to_frequency
from tfidf_converter import TfidfConverter
import operator


def get_text_from_mongo():
    pass


def get_text_from_dir(path):
    pass


class ClusterSuggestor:
    def __init__(self, from_mongo=True):
        self.cluster_text = {}
        if from_mongo:
            self.cluster_text = get_text_from_mongo()
        else:
            self.cluster_text = get_text_from_dir(
                '/home/jaojao/hackathon/clusters/')

        self.idf = {}
        self.cluster_tfidf = {}

    def suggest(self, input_text, n=1):
        if not self.cluster_tfidf:
            self.get_cluster_tfidf_vectors()

        input_tfidf = self.convert_to_tfidf(input_text)

        similarity = []  # (cluster, sim_score to input)
        for cluster, cluster_tfidf in self.cluster_tfidf.items():
            similarity.append(cluster, self.cosine(cluster_tfidf, input_tfidf))

        sorted_clusters_by_sim = sorted(
            similarity, key=operator.itemgetter(1), reversed=True)

        closest_cluster = sorted_clusters_by_sim[0][0]

        possible_suggestions = self.cluster_text[closest_cluster]

        return possible_suggestions[:n]

    def cosine(self, v1, v2):
        pass

    def convert_to_tfidf(self, input_text):
        pass

    def get_cluster_tfidf_vectors(self):
        # Obtain frequency vectors
        freq_vectors = {}
        for cluster, phrases in self.cluster_text.items():
            raw_text = ' '.join(phrases)
            tokens = clean_text(raw_text)
            freq_vector = convert_to_frequency(tokens)
            freq_vectors[cluster] = freq_vector

        # Obtain TF-IDF vectors
        tfidf = TfidfConverter(freq_vectors)
        tfidf.generate_tfidf_vectors()
        self.cluster_tfidf = tfidf.tfidf_vectors
        self.idf = tfidf.idf
