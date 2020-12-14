import os

# generate path from bibtex code:
def generatePublPath(pathToMemex, bibTexCode):
    temp = bibTexCode.lower()
    directory = os.path.join(pathToMemex, temp[0], temp[:2], bibTexCode)
    return(directory)

def loadYmlSettings(ymlFile):
    with open(ymlFile, "r", encoding="utf8") as f1:
        data = f1.read()
        data = re.sub(r"#.*", "", data) # remove comments
        data = re.sub(r"\n+", "\n", data) # remove extra linebreaks used for readability
        data = re.split(r"\n(?=\w)", data) # splitting
        dic = {}
        for d in data:
            if ":" in d:
                d = re.sub(r"\s+", " ", d.strip())
                d = re.split(r"^([^:]+) *:", d)[1:]
                key = d[0].strip()
                value = d[1].strip()
                dic[key] = value
    return(dic)