import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect the database into our classes.
Base = automap_base()
#Reflect the database
Base.prepare(engine, reflect=True)
#Create a variable for each of the classes so that we can reference them 
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create a session link from Python to our database
session = Session(engine)
#Define our Flask app
app = Flask(__name__)
#Define the welcome route 
@app.route("/")
#Create function welcome
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#Create the route
@app.route("/api/v1.0/precipitation")
#Create the precipitation() function
def precipitation():
    return
#Calculates the date one year ago from the most recent date 
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   return
#A query to get the date and precipitation for the previous year
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return
#Use jsonify() to format our results into a JSON structured file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
#Defining route and name
@app.route("/api/v1.0/stations")
#Create new function
def stations():
    return
#Create a query that will allow us to get all of the stations in our database
def stations():
    results = session.query(Station.station).all()
    return
#Unraveling our results into a one-dimensional array
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# Defining the route
@app.route("/api/v1.0/tobs")
#Create function
def temp_monthly():
    return
#Calculate the date one year ago from the last date in the database.
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return
#Query the primary station for all the temperature observations from the previous year
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    return
#Unravel the results into a one-dimensional array and convert that array into a list Then jsonify the list and return our results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
#Create a starting and ending date for route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Create a function
def stats():
     return
# Add parameters to our stats()function
def stats(start=None, end=None):
     return
#Create a query to select the minimum, average, and maximum temperatures from our SQLite database
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
#Determine the starting and ending date, add an if-not statement to our code
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
#Calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

