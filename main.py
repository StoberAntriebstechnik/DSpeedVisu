#!/usr/bin/python
# -*- coding: utf-8 -*-

from Writer import Writer

from collections import OrderedDict

def start():
    data = OrderedDict()
    data.update({'Sheet -' : [[1,  5,  9], [2, 'fuck',  0]]})
    writer = Writer('inout/Testy.ods')
    writer.setData(data)
    matrix = [[1,  2,  '3'],  [4,  5,  6],  ['7', '8',  '9']]
    writer.addSheet('Hi there',  matrix)
    
    writer.write('ods')
    
if __name__ == "__main__":
    start()
