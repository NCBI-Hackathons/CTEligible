from suggest_cluster import ClusterSuggestor
import pprint


def main():
    input_text = 'The platelet count is greater than 10000'
    suggestor = ClusterSuggestor(from_mongo=False)
    suggestions = suggestor.suggest(input_text)

    pprint.pprint(suggestions)


if __name__ == '__main__':
    main()
