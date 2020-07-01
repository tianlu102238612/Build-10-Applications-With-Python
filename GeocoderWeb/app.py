from flask import Flask,render_template,request,send_file
import pandas
from geopandas.tools import geocode
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import os
import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload/",methods=['GET','POST'])
def upload():
    global filename
    if request.method == 'POST':
        if request.files:
            file = request.files['selectedFile']
            if file:
                df = pandas.read_csv(file)
                locator = Nominatim(user_agent='autogis_app')
                geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
                location = df['Address'].apply(geocode)
                point = location.apply(lambda loc: tuple(loc.point) if loc else None)
                df[['latitude', 'longitude', 'altitude']] = pandas.DataFrame(point.tolist(), index=df.index)
                df=df.drop("altitude",1)
                filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".csv")
                df.to_csv(filename,index=None)
                return render_template("index.html",tables=[df.to_html(classes='data', header="true")])
            else:
                errorMsg = "You must upload a file before submit"
                return render_template("index.html",errorMsg = errorMsg)
            
@app.route("/download/")
def download():
    return send_file(filename,as_attachment = True)
            
            
if __name__ == "__main__":
    app.run()
