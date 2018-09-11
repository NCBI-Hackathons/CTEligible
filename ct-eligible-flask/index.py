import json

import click
from flask import jsonify, make_response, render_template

from app import app, mongo


def add_cluster_json_file_to_mongo(json_file):

    with open(json_file) as f:
        clust_list = json.load(f)

    for clust in clust_list:
        mongo.db.clusters.insert_one(clust)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return render_template('index.html')


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    app.run()


@cli.command()
@click.argument('json_file')
def add_cluster_json(json_file):
    add_cluster_json_file_to_mongo(json_file)


if __name__ == '__main__':
    cli()
