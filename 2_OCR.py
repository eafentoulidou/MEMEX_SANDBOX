# NEW LIBRARIES
import pdf2image    # extracts images from PDF
import pytesseract  # interacts with Tesseract, which extracts text from images

import os, yaml, json, random

# SCRIPT WITH OUR PREVIOUS FUNCTIONS
import functions

###########################################################
# VARIABLES ###############################################
###########################################################

settings = functions.loadYmlSettings("settings.yml")

###########################################################
# MAIN FUNCTIONS ##########################################
###########################################################

# function OCR a PDF, saving each page as an image and
# saving OCR results into a JSON file


def ocrPublication(citationKey, language):
    # generate and create necessary paths
    publPath = functions.generatePublPath(settings["path_to_memex"], citationKey)
    pdfFile  = os.path.join(publPath, citationKey + ".pdf")
    jsonFile = os.path.join(publPath, citationKey + ".json") # OCR results will be saved here
    saveToPath = os.path.join(publPath, "pages") # we will save processed images here

    # first we need to check whether this publication has been already processed
    if not os.path.isfile(pdfFile):
        return
    if not os.path.isfile(jsonFile):
        # let's make sure that saveToPath also exists
        if not os.path.exists(saveToPath):
            os.makedirs(saveToPath)
        
        # start process images and extract text
        print("\t>>> OCR-ing: %s" % citationKey)
# create an empty dictionary for the OCR results. 
        textResults = {}
        images = pdf2image.convert_from_path(pdfFile)
        pageTotal = len(images)
        pageCount = 1
        #OCR the text by image (page) and put it into this dictionary with the page number (= image number) as key
        for image in images:
            text = pytesseract.image_to_string(image, lang=language)
            textResults["%04d" % pageCount] = text

            image = image.convert('1') # binarizes image, reducing its size
            finalPath = os.path.join(saveToPath, "%04d.png" % pageCount)
            image.save(finalPath, optimize=True, quality=10)

            print("\t\t%04d/%04d pages" % (pageCount, pageTotal))
            pageCount += 1
# save the dictionary as a json file
        with open(jsonFile, 'w', encoding='utf8') as f9:
            json.dump(textResults, f9, sort_keys=True, indent=4, ensure_ascii=False)
    
    else: # in case JSON file already exists
        print("\t>>> %s has already been OCR-ed..." % citationKey)


###########################################################
# FUNCTIONS TESTING #######################################
###########################################################

ocrPublication("AbdurasulovMaking2020", "eng")

###########################################################
# PROCESS ALL RECORDS: APPROACH 2 #########################
###########################################################

# Why this way? Our computers are now quite powerful; they
# often have multiple cores and we can take advantage of this;
# if we process our data in the manner coded below --- we shuffle
# our publications and process them in random order --- we can
# run multiple instances fo the same script and data will
# be produced in parallel. You can run as many instances as
# your machine allows (you need to check how many cores
# your machine has). Even running two scripts will cut
# processing time roughly in half.

def processAllRecords(bibDataFile):
    # load the bib file as dictionary using the function from previous step
    bibData = functions.loadBib(bibDataFile)
    # save the keys of the dictionary bibData as a list
    keys = list(bibData.keys())
    random.shuffle(keys)
    print
    print(str(keys))
# in a loop, process each key from the list keys (i.e. each record by citation key)
    for key in keys:
        bibRecord = bibData[key]
        # run the function from the previous step that creates a path with pdf and bib files, if not already there
        functions.processBibRecord(settings["path_to_memex"], bibRecord)
        language = functions.identifyLanguage(bibRecord, "eng")
        # run the function that saves ocr-ed text as json files and created .png images for each page
        ocrPublication(bibRecord["rCite"], language)

###########################################################

processAllRecords(settings["bib_all"])
print("Done!")