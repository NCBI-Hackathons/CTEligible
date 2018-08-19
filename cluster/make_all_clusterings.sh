set -euxo pipefail
python3 make_clustering.py --tag "Hemoglobin_CTEP Trials_072018"
python3 make_clustering.py --tag "Platelets_CTEP Trials_072018"
python3 make_clustering.py --tag "WBC_CTEP Trials_072018"
python3 make_clustering.py --tag "HIV_CTEPTrials_072018"
