#!/bin/bash

python ct_eligible/index.py add_cluster_json ct_eligible/data/clusters.json
python ct_eligible/index.py add_ctep_json ct_eligible/data/ctep.json
python ct_eligible/index.py run_server
