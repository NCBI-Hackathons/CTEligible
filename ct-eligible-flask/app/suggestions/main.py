from suggest_cluster import ClusterSuggestor
import pprint


def main():
    input_text_1 = 'The platelet greater than or equal to 70000 platelets per cubic millimeter'
    input_text_2 = 'Within 36 days prior to registration, you must not have treatment'
    suggestor = ClusterSuggestor(from_mongo=False)
    suggestions_1 = suggestor.suggest(input_text_1)
    suggestions_2 = suggestor.suggest(input_text_2)

    pprint.pprint(suggestions_1)
    pprint.pprint(suggestions_2)


if __name__ == '__main__':
    main()
