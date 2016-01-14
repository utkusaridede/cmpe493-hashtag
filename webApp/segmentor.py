#!/usr/bin/python

from bottle import route, run, response
import traceback, re, datetime
import os

def removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)

def json2str(json):
    s = ""
    if type(json) is list:
        i = 0
        s = "["
        for item in json:
            if i > 0:
                s = s+","
            if type(item) is dict or type(item) is list:
                s = s + json2str(item)
            else:
                val = removeNonAscii(str(item))
                val = re.sub(r"\"", "\\\"", val)
                s = s + "\"" + val + "\""
            i = i+1
        s = s+"]"
    elif type(json) is dict:
        s = "{"
        i = 0
        for key in json:
            if i > 0:
                s = s+","
            if type(json[key]) is dict or type(json[key]) is list:
                s = s + "\""+key+"\": "+json2str(json[key])
            elif type(json[key]) is float:
                s = s + "\""+key+"\": "+str(json[key])
            else: 
                val = removeNonAscii(json[key])
                val = re.sub(r"\"", "\\\"", val)
                s = s + "\""+key+"\": \""+ val+"\""
            i = i+1
        s = s+"}"
        
    return s

@route('/segment/<hashtag>')
def save(runid, params):
    global db
    response.headers['Access-Control-Allow-Origin'] = '*'

    # run your program here

load()
run(host='localhost', port=10001)