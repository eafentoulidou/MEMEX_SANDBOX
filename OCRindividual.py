def ocrPublication(citationKey, language):
    # generate and create necessary paths
    publPath = functions.generatePublPath(settings["path_to_memex"], citationKey)
    pdfFile  = os.path.join(publPath, citationKey + ".pdf")
    jsonFile = os.path.join(publPath, citationKey + ".json") # OCR results will be saved here
    saveToPath = os.path.join(publPath, "pages") # we will save processed images here

    # first we need to check whether this publication has been already processed
    if not os.path.isfile(jsonFile):
        # let's make sure that saveToPath also exists
        if not os.path.exists(saveToPath):
            os.makedirs(saveToPath)
        
        # start process images and extract text
        print("\t>>> OCR-ing: %s" % citationKey)

        textResults = {}
        images = pdf2image.convert_from_path(pdfFile)
        pageTotal = len(images)
        pageCount = 1
        for image in images:
            text = pytesseract.image_to_string(image, lang=language)
            textResults["%04d" % pageCount] = text

            image = image.convert('1') # binarizes image, reducing its size
            finalPath = os.path.join(saveToPath, "%04d.png" % pageCount)
            image.save(finalPath, optimize=True, quality=10)

            print("\t\t%04d/%04d pages" % (pageCount, pageTotal))
            pageCount += 1

        with open(jsonFile, 'w', encoding='utf8') as f9:
            json.dump(textResults, f9, sort_keys=True, indent=4, ensure_ascii=False)
    
    else: # in case JSON file already exists
        print("\t>>> %s has already been OCR-ed..." % citationKey)

ocrPublication(GarzanitiApocryphal2018, eng)