import urllib.request
import json
import sys


def getJSON(nct_id):
    with urllib.request.urlopen("https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" + nct_id) as url:
        try:
            jsonFile = json.loads(url.read().decode())
        except urllib.error.HTTPError as e:
            return None
        return None


def getUnstructured(jsonFile):
    unstructed=[]
    for criteria in jsonFile['eligibility']['unstructured']:
        #print (jsonFile['eligibility'])
        unstructed.append(str(criteria["inclusion_indicator"])+":"+criteria["description"].strip())
    return("\t".join(unstructed))

def getStructured(jsonFile):
    headers=getStructuredHeader()
    structured=[]
    for h in headers:
        structured.append(str(jsonFile['eligibility']['structured'][h]))
    return structured

def getStructuredHeader():
    return ["gender","max_age", "max_age_in_years", "max_age_number", "max_age_unit", "min_age","min_age_in_years","min_age_number","min_age_unit"]

def main():
    printStructured=True
    with open('../other_data/trials_criteria_phrases.txt', encoding="utf8", errors='ignore') as in_file:
        if printStructured:
            print ("nct_id\t"+"\t".join(getStructuredHeader()))
            for line in in_file:
                if line.strip()=="":
                    break
                #print (line)
                nct_id=line.split(",")[0].strip()
                if nct_id == "NCT01841723":
                    continue
                #getJSON(nct_id)
                #print (json.dumps(getJSON(nct_id), indent=4, sort_keys=True))
                jsonToParse=getJSON(nct_id)
                if jsonToParse is None:
                    continue
                print (nct_id+"\t"+"\t".join(getStructured(getJSON(nct_id))))








if __name__ == '__main__':
    main()
    sys.stdout.flush()
    exit()
