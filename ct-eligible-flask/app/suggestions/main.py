from suggestions_utils import get_cluster_text
from suggestions_utils import clean_text
from suggestions_utils import convert_to_frequency
from tfidf_converter import TfidfConverter


def main():
    cluster_dir = '/home/jaojao/hackathon/clusters/'
    raw_cluster_text = get_cluster_text(cluster_dir)

    freq_vectors = {}
    for name, phrases in raw_cluster_text.items():
        raw_text = ' '.join(phrases)
        tokens = clean_text(raw_text)
        freq_vector = convert_to_frequency(tokens)
        freq_vectors[name] = freq_vector

    tfidf = TfidfConverter(freq_vectors)
    tfidf.generate_tfidf_vectors()
    vectors = tfidf.tfidf_vectors

    for cluster, vector in vectors.items():
        print(cluster + '\n')
        print(str(vector) + '\n')


if __name__ == '__main__':
    main()
