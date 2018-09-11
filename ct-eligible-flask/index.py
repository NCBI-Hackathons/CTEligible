import json

import click
from flask import jsonify, make_response, render_template

from app import app, mongo
from app.suggestions.suggest_cluster import ClusterSuggestor


def add_cluster_json_file_to_mongo(json_file):

    with open(json_file) as f:
        clust_list = json.load(f)

    for clust in clust_list:
        mongo.db.clusters.replace_one(
            {'_id': clust['_id']}, clust, upsert=True)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-suggestion/')
@app.route('/get-suggestion/<input_json>')
def get_suggestions(input_json=None, methods=['POST']):

    if not input_json:
        return 'No input text.'

    try:
        input_data = json.loads(input_json)
    except ValueError:
        input_data = json.loads(json.dumps(input_json))

    cluster_suggestor = ClusterSuggestor()
    suggestion = cluster_suggestor.suggest(input_data)

    return jsonify(suggestion)


@click.group()
def cli():
    pass


@cli.command()
def run_server():
    app.run(host='0.0.0.0', port=4000)


@cli.command()
@click.argument('json_file')
def add_cluster_json(json_file):
    add_cluster_json_file_to_mongo(json_file)


if __name__ == '__main__':
    cli()
