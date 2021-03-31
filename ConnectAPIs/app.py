import requests

def getfact():
    req = requests.get('http://numbersapi.com/random/trivia?json')
    return req.json()['text']

def generatebarcode():
    req = requests.post('http://bwipjs-api.metafloor.com/?bcid=code128&text='+str(getfact()))
    print( req.url)

print("use the following url to get a fact barcode")
generatebarcode()
