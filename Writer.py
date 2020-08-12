#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pyexcel_ods import save_data as save

class Writer:
    
    def __init__(self,  file_name):
        self.data = OrderedDict()
        self.filename = file_name
        
    def setData(self,  data):
        self.data = data
        
    def addSheet(self,  name,  matrix):
        self.data.update({name : matrix})
        
    def write(self, sheet_type):
        if sheet_type == 'ods':
            save(self.filename,  self.data)
