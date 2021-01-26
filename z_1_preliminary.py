import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "settings.yml"
vars = yaml.load(open(settingsFile))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile):

    tempDic = {}

    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read()
        records = records.split("\n@")

        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                record = record.strip()
                record = record.split("\n")[:-1]

                for r in record[1:]:
                    r = r.split("=")[0].strip()

                    if r in tempDic:
                        tempDic[r] += 1
                    else:
                        tempDic[r] = 1

    results = []
    for k,v in tempDic.items():
        result = "%010d\t%s" % (v, k)
        results.append(result)

    results = sorted(results, reverse=True)
    results = "\n".join(results)

    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:
        f9.write(results)

bibAnalyze(vars['bib_all'])