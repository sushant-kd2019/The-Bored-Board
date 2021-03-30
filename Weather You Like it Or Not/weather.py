from flask import Flask, render_template, request
  
# import json to load JSON data to a python dictionary
import json
  
# urllib.request to make a request to api
import urllib.request
  
  
app = Flask(__name__)
  
@app.route('/', methods =['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'delhi'
  
    api = "85b8d1653b405711f28d4313b1aa5d50"
  
    # source contain json data from api
    data = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()
  
    # converting JSON data to a dictionary
    dict_of_data = json.loads(data)
  
    # data for variable dict_of_data
    individual = {
        "cityname":city,
        "country_code": str(dict_of_data['sys']['country']),
        "coordinate": str(dict_of_data['coord']['lon']) + ' ' 
                    + str(dict_of_data['coord']['lat']),
        "temp": str(dict_of_data['main']['temp']) + ' K',
        "temp_cel":str("%.3f C" % (float(str(dict_of_data['main']['temp']))-273)),
        "pressure": str(dict_of_data['main']['pressure']),
        "humidity": str(dict_of_data['main']['humidity']),
    }
    print(individual)
    return render_template('index.html', data = individual)
  
  
  
if __name__ == '__main__':
    app.run(debug = True)