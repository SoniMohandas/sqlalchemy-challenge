import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, cast

# connecting to the the database.
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect databases into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create Session to DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route('/')
def home():
    return(
        f"Welcome to the Home page of Climate app <br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"   
    )

# Convert the query results to a dictionary using date as the key and prcp as the value.Return the JSON representation of your dictionary

@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp_data=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > "2016-08-23").order_by(Measurement.date).all()
    
    prcp_dict={}
    for data in prcp_data:
        prcp_dict[data.date]=data.prcp
   
    return jsonify(prcp_dict)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    station=session.query(Station.station).all()
    
    result=[]
    for stat in station:
        result.append(stat[0])
    return jsonify(f"List of stations:{result}")

#Query the dates and temperature observations of the most active station for the last year of data.Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    twelve_month_tobs=session.query(Measurement.date,Measurement.tobs).filter(Measurement.station=='USC00519281', Measurement.date>"2016-08-23").all()
    
    result=[]
    for temp in twelve_month_tobs:
        result.append(temp[1])
    return jsonify(f"List of temperature observations of most active station: {result}")
   

@app.route("/api/v1.0/<start>")
def temp_start(start):
    results=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>start).all()
    result_set={}
    result_set["Lowest Temperature"]=results[0][0]
    result_set["Average Temperature"]=results[0][1]
    result_set["Highest Temperature"]=results[0][2]
    return jsonify(result_set)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    results=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>start).filter(Measurement.date<end).all()
   
    result_set={}
    result_set["Lowest Temperature"]=results[0][0]
    result_set["Average Temperature"]=results[0][1]
    result_set["Highest Temperature"]=results[0][2]
    return jsonify(result_set)

if __name__ == '__main__':
    app.run(debug=True)