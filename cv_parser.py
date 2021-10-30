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

# nltk.download('stopwords') # comment out after first run

from pyresparser import ResumeParser
data = ResumeParser('Michaela_Links_CV.pdf').get_extracted_data()

# print("\n\n",data)

json_object = json.dumps(data, indent = 4) 
print("\n\n", json_object)



