### CTEligible, Flask application

ct-eligible-flask describes a web-based API for providing eligibilty criteria suggestions based on previous clustering results (see /data/clusters.json).

#### Deployment

There are two options for deployment.

##### Manual installation

ct-eligible-flask runs using Flask and MongoDB. To install dependencies, we provide a requirements file to be used by pip.

```
pip install -r requirements
```

Make sure to download MongoDB before moving on to the following steps.

First, initialize MongoDB daemon:

```
mongod
```

Second, add cluster information to the database:

```
python index.py add_cluster_json data/clusters.json
```

Third, add ctep information to the database:

```
python index.py add_ctep_json data/ctep.json
```


Last, run the server:

```
python index.py run_server
```

##### Docker-Compose

ct-eligible-flask has been developed with deployment by [Docker Compose](https://docs.docker.com/compose/) in mind.

To deploy, use the following commands:

```
docker-compose build
docker-compose up
```

#### API

HTTP requests can be used to find eligibility criteria suggestions based on a text input.  The API calls require the following structure:

```
HOST:PORT/get-suggestion/<TEXT OR JSON STRING>
```

Example syntax is as follows:

```
http://localhost:4000/get-suggestion/platelet
```

The API returns suggestions in JSON format.  The format is as follows:

```
[{"ctep_suggestion":[<SUGGESTIONS>, ], "data_suggestion":[<SUGGESTIONS>, ], "text":<INPUT TEXT>}, ]
```
