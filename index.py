import subprocess
import sys
from flask import Flask, request
import pandas as pd

# import cv2
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json


import numpy as np


@app.route("/", methods=["GET", "POST"])
def index():

        output = request.get_json()

        city = output['city']
        days = float(output['days'])
        latitude = float(output['lat'])
        longitude = float(output['long'])

        # data, _ = subprocess.Popen([sys.executable, "current.py", str(latitude) + "," + str(longitude)],
        #                            stdout=subprocess.PIPE).communicate()
        # data = {"city": city,  "days": days+100}
        #
        # lati = {"lat" : lat,  "long": long}
        lat = 30.3165
        long = 78.0322

        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=hotels&location="+str(lat)+"%2C" +str(long) +"&radius=500&type=lodging&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        data = r.json()

        j = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?&location="+str(lat)+"%2C" +str(long) +"&radius=25000&type=point_of_interest&keyword=places&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        data2 = j.json()

        # t = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=hotels&location="+str(lat)+"%2C" +str(long) +"&radius=500&type=hospital&keyword=hospitalnearme&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        # data3 = t.json()

        # print(data)
        # jsonString = json.loads(data)
        s1 = json.dumps(data)
        jsonstring = json.loads(s1)

        s2 = json.dumps(data2)
        jsonstring2 = json.loads(s1)

        s3 = json.dumps(data3)
        jsonstring3 = json.loads(s1)

        # block, _ = subprocess.Popen([sys.executable, "tiff.py", str(latitude) + "," + str(longitude)],
        #                             stdout=subprocess.PIPE).communicate()
        # j = json.loads(block)
        #
        # jsonString.update(j)
        # # print("current")
        # x = subprocess.Popen([sys.executable, "dist.py", str(latitude) + "," + str(longitude)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][0].update({"riverDistance": float(x)})
        #
        # locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))
        #
        # ans = locname.address.split(',')
        # jsonString["data"][0].update({"title": ans[0]})
        #
        # # print("dist")
        # e = subprocess.Popen([sys.executable, "elevation.py", str(latitude) + "," + str(longitude)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][0].update({"seaLevel": float(e)})
        #
        # s = subprocess.Popen([sys.executable, "slope.py", str(latitude) + "," + str(longitude)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][0].update({"slope": float(s)})
        #
        # n = random.randint(0, 2)
        #
        # jsonString["data"][0].update({"road": n})
        # f = subprocess.Popen([sys.executable, "forest.py", str(latitude) + "," + str(longitude)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][0].update({"forest": float(f)})
        #
        # m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][0])],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][0].update({"class": str(m)})
        #
        # locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))
        #
        # ans = locname.address.split(',')
        # jsonString["data"][1].update({"title": ans[0]})
        #
        # x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][1].update({"riverDistance": float(x)})
        # # print("dist")
        # e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][1].update({"seaLevel": float(e)})
        #
        # s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][1].update({"slope": float(s)})
        #
        #
        # f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude + 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][1].update({"forest": float(f)})
        #
        # m = subprocess.Popen([sys.executable, "test.py", str(jsonString["data"][1])],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][1].update({"class": str(m)})
        #
        # x = subprocess.Popen([sys.executable, "dist.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][2].update({"riverDistance": float(x)})
        # # print("dist")
        # e = subprocess.Popen([sys.executable, "elevation.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][2].update({"seaLevel": float(e)})
        #
        # s = subprocess.Popen([sys.executable, "slope.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][2].update({"slope": float(s)})
        #
        # n = random.randint(0, 2)
        #
        # jsonString["data"][2].update({"road": n})
        # locname = geoLoc.reverse(str(latitude) + " ," + str(longitude))
        #
        # ans = locname.address.split(',')
        # jsonString["data"][2].update({"title": ans[0]})
        #
        # f = subprocess.Popen([sys.executable, "forest.py", str(latitude + 0.09) + "," + str(longitude - 0.09)],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][2].update({"forest": float(f)})
        #
        # m = subprocess.Popen([sys.executable, "test2.py"],
        #                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
        # jsonString["data"][2].update({"class": str(m)})
        #
        # counter = False
        # df = pd.read_csv("datas.csv")
        #
        # for index, row in df.iterrows():
        #     long = row['Longitude']
        #     lat = row['Latitude']
        #     latmin = lat - 0.04
        #     latmax = lat + 0.04
        #     longmin = long - 0.04
        #     longmax = long + 0.04
        #
        #     if (latitude >= latmin and latitude <= latmax and longitude >= longmin and longitude <= longmax):
        #         counter = True
        # jsonString["data"][0].update({"allow": counter})
        # jsonString["data"][1].update({"allow": counter})
        # jsonString["data"][2].update({"allow": counter})

        combined = {"hospital": jsonstring3, "hotel": jsonstring, "Places": jsonstring}

        # print((jsonstring))
        # print(type(jsonstring2))
        #

        return combined


if __name__ == '__main__':
        # lat = 30.3165
        # long = 78.0322
        #
        # r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=hotels&location=" + str(
        #         lat) + "%2C" + str(long) + "&radius=500&type=lodging&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        # data = r.json()
        #
        # j = requests.get(
        #         "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&location=" + str(lat) + "%2C" + str(
        #                 long) + "&radius=25000&type=point_of_interest&keyword=places&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        # data2 = j.json()
        #
        # t = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=hospitals&location=" + str(
        #         lat) + "%2C" + str(
        #         long) + "&radius=500&type=hospital&keyword=hospitalnearme&key=AIzaSyDxcBJYDXKP9cOK6F9LjAA3jbQYxMtfxwc")
        # data3 = t.json()
        #
        # s1 = json.dumps(data)
        # jsonstring = json.loads(s1)
        #
        # s2 = json.dumps(data2)
        # jsonstring2 = json.loads(s1)
        #
        # s3 = json.dumps(data3)
        # jsonstring3 = json.loads(s1)
        #
        # combined = {"hospital": jsonstring3, "hotel": jsonstring, "Places": jsonstring}
        #
        # # print((jsonstring))
        # # print(type(jsonstring2))
        # #
        # print(combined)
        app.run(debug=True, host='0.0.0.0', port=2000)

