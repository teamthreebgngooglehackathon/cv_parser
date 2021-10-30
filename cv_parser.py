#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:33:13 2021

@author: michaelalinks


1. pip install pyresparser or pip3 install pyresparser
2. pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz


"""

import json
import nltk
from docx2pdf import convert
from pyresparser import ResumeParser
import os

# nltk.download('stopwords') # comment out after first run

file = "Michaela_Links_CV.pdf"


if file.endswith(".pdf") is True: # for pdfs
    try:
        data = ResumeParser(file).get_extracted_data()
        json_object = json.dumps(data, indent = 4) 
        print("\n\n", json_object)
    except FileNotFoundError:
        print("File not found, try again")
elif file.endswith(".docx") is True: # for docx -> pdf conversion
    try: 
        convert(file)
        file_name = os.path.splitext(file)[0] + ".pdf"
        data = ResumeParser(file_name).get_extracted_data()
        json_object = json.dumps(data, indent = 4) 
        print("\n\n", json_object)
    except FileNotFoundError:
        print("File not found, try again") 
else:
    print("Please attach a valid file type")





