import json
import sys
import urllib.request
import urllib
import urllib.error



def getJSON(nct_id):
    try:
        with urllib.request.urlopen("https://clinicaltrialsapi.cancer.gov/v1/clinical-trial/" + nct_id) as url:
            try:
                return json.loads(url.read().decode())
            except urllib.error.HTTPError as e:
                return None
    except urllib.error.HTTPError as e:
        return None


def getEligabliltyUnstructured(jsonFile):
    unstructed=[]
    for criteria in jsonFile['eligibility']['unstructured']:
        unstructed.append(str(criteria["inclusion_indicator"])+":"+criteria["description"].replace("\n","").replace("\r","").strip())
    return("\t".join(unstructed))

def getEligabliltyStructured(jsonFile):
    headers=getEligabliltyStructuredHeader()
    structured=[]
    for h in headers:
        if 'eligibility' in jsonFile:
            if 'structured' in jsonFile['eligibility']:
                for k in jsonFile['eligibility']['structured'].keys():
                    if k not in headers:
                        print (k)
                if h in jsonFile['eligibility']['structured']:
                    structured.append(str(jsonFile['eligibility']['structured'][h]))
                else:
                    structured.append("None")
            else:
                structured.append("None")
        else:
            structured.append("None")
    return structured

def getEligabliltyStructuredHeader():
    return ["gender","max_age", "max_age_in_years", "max_age_number", "max_age_unit", "min_age","min_age_in_years","min_age_number","min_age_unit"]

def printStructedEligablility(in_file):
    print ("nct_id\t"+"\t".join(getEligabliltyStructuredHeader()))
    for line in in_file:
        if line.strip()=="":
            break
        nct_id=line.split("\t")[0].strip()
        jsonToParse=getJSON(nct_id)
        if jsonToParse is None:
            print (nct_id+"\t404ERROR")
        else:
            print (nct_id+"\t"+"\t".join(getEligabliltyStructured(getJSON(nct_id))))
    return

def main():
    printUnstructed=True
    with open(sys.argv[1], encoding="utf8", errors='ignore') as in_file:
        if printUnstructed:
            for line in in_file:
                if line.strip()=="":
                    break
                nct_id=line.split("\t")[0].strip()
                if nct_id=="nci_id":
                    continue
                jsonToParse=getJSON(nct_id)
                if jsonToParse is None:
                    print (nct_id+"\t404ERROR")
                else:
                    print (nct_id+"\t"+getEligabliltyUnstructured(jsonToParse))









if __name__ == '__main__':
    main()
    sys.stdout.flush()
    exit()
