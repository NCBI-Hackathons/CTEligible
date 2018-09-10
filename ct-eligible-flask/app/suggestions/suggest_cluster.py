import os
import csv


def get_cluster_text(cluster_dir):
    cluster_text = {}

    for file in os.listdir(cluster_dir):
        cluster_file = os.path.join(cluster_dir, file)
        cluster_name = os.path.basename(cluster_file)

        phrases = []
        with open(cluster_file, 'r') as file_reader:
            reader = csv.reader(file_reader, delimiter=' ')
            for row in reader:
                text = row[1].strip()
                phrases.append(text)

        cluster_text[cluster_name] = phrases

    return cluster_text


def main():
    cluster_dir = '/home/jaojao/hackathon/clusters/'
    cluster_text = get_cluster_text(cluster_dir)

    for name, phrases in cluster_text.items():
        print(name + '\t' + str(len(phrases)))


if __name__ == '__main__':
    main()
