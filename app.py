import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station=Base.classes.station
Measurement=Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and precipitations values"""
    # Query date and precipitation from Measurement class
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Convert query to dictionary
    date=[row.date for row in results]
    prcp=[row.prcp for row in results]

    res = {} 
    for key in date: 
        for value in prcp: 
            res[key] = value 
            prcp.remove(value) 
            break  

    return jsonify(res)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query station information from Station class
    results = session.query(Station.station,Station.name).all()

    session.close()

    # Convert query to dictionary
    station=[row.station for row in results]
    name=[row.name for row in results]

    res = {} 
    for key in station: 
        for value in name: 
            res[key] = value 
            name.remove(value) 
            break  

    return jsonify(res)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Find most active station and date ranges for previous year"""
    # Query for active station
    station_count=func.count(Measurement.station).label('station_count')

    most_active = session.query(Measurement.station, station_count)\
        .group_by(Measurement.station).order_by(station_count.desc()).first()

    # Query for latest data point and calculate year ago using Datetime

    last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    for i in last_date:
        date_time_obj = dt.date.fromisoformat(i)

    year_ago =  dt.date(date_time_obj.year,date_time_obj.month,date_time_obj.day) - dt.timedelta(days=365)

    """ Query for dates and temperatures of the most active station for the last year of data """

    results = session.query(Measurement.date,Measurement.tobs)\
        .filter(Measurement.station==most_active.station)\
            .filter(Measurement.date >= year_ago)


    session.close()

    # Convert query to dictionary
    date=[row.date for row in results]
    tobs=[row.tobs for row in results]

    res = {} 
    for key in date: 
        for value in tobs: 
            res[key] = value 
            tobs.remove(value) 
            break  

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
