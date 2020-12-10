def bibliography():

    bibliodict =  {}

    with open(r"C:\Users\Eirini\Documents\Digital HUmanities\WS_2020_MRomanov\HW070172\Lesson6\zotero_biblatex_sample.bib", "r", encoding="utf8") as f1:
        biblioRaw = f1.read()
    bibliosplit = biblioRaw.split("\n@")
    
    for record in bibliosplit:
        keyValue = record.split(",\n")
        citationkey = keyValue[0]
        citkey = citationkey.split("{")
        recordType = citkey[0]
        citationKey = citkey[1]
        recorddict = {"recordType": recordType}
        for r in keyValue[1:]:
            recordsRest = r.split("=")
            key = recordsRest[0].strip()
            value = recordsRest[1].strip()
            recorddict[key] = value
        bibliodict[citationKey] = recorddict

    import yaml
    with open(r"C:\Users\Eirini\Documents\Digital HUmanities\WS_2020_MRomanov\HW070172\Lesson6\bibliography.yaml", "w", encoding="utf8") as f2:
        yaml.dump(bibliodict, f2)
    f2.close()
    
bibliography()