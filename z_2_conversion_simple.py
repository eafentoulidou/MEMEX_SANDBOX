import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "settings.yml"
settings = yaml.load(open(settingsFile))
bibKeys = yaml.load(open("zotero_biblatex_keys.yml"))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):

    bibDic = {}

    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read().split("\n@")

        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():

                record = record.strip().split("\n")[:-1]

                rType = record[0].split("{")[0].strip()
                rCite = record[0].split("{")[1].strip().replace(",", "")

                bibDic[rCite] = {}
                bibDic[rCite]["rCite"] = rCite
                bibDic[rCite]["rType"] = rType

                for r in record[1:]:
                    key = r.split("=")[0].strip()
                    val = r.split("=")[1].strip()
                    val = re.sub("^\{|\},?", "", val)

                    fixedKey = bibKeys[key]

                    bibDic[rCite][fixedKey] = val


    print("="*80)
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    print("="*80)
    return(bibDic)

###########################################################
# CONVERSION FUNCTIONS ####################################
###########################################################

import json
def convertToJSON(bibTexFile):
    data = bibLoad(bibTexFile)
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)


import yaml
def convertToYAML(bibTexFile):
    data = bibLoad(bibTexFile)
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:
        yaml.dump(data, f9)

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    data = bibLoad(bibTexFile)
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] 
    header = "\t".join(headerList)

    dataNew = [header]

    for k,v in data.items():
        citeKey = k

        if 'rType' in v:
            rType = v['rType']
        else:
            rType = "NA"

        if 'author' in v:
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"

        tempVal = "\t".join([citeKey, rType, author, title, date])
        dataNew.append(tempVal)

    finalData = "\n".join(dataNew)
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:
        f9.write(finalData)


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

#convertToJSON(settings["bib_all"])
#convertToYAML(settings["bib_all"])
#convertToCSV(settings["bib_all"])


print("Done!")