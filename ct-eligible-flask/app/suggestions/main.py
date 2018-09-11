from suggest_cluster import ClusterSuggestor
import pprint


def main():
    input_text_1 = 'The platelet greater than or equal to 70000 platelets per cubic millimeter'
    # input_text_2 = 'Within 36 days prior to registration, you must not have treatment'

    empty_string = ''
    gibberish = 'asdfaldfkl abgkfha 34h13bmnr $#42mn adf'
    gibberish_one_word = 'dafkajldf'
    suggestor = ClusterSuggestor(from_mongo=False)
    suggestions_1 = suggestor.suggest(input_text_1)
    # suggestions_2 = suggestor.suggest(input_text_2)

    print(input_text_1)
    pprint.pprint(suggestions_1)
    print()
    print(empty_string)
    pprint.pprint(suggestor.suggest(empty_string))
    print()
    print(gibberish)
    pprint.pprint(suggestor.suggest(gibberish))
    print()
    print(gibberish_one_word)
    pprint.pprint(suggestor.suggest(gibberish_one_word))


if __name__ == '__main__':
    main()
