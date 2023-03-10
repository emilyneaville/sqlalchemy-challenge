import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
# Connection to the sql(ite) database
engine = create_engine('sqlite:///../Resources/hawaii.sqlite')

# reflect an existing database into a new model:
Base = automap_base() # Instatiate the 'Base' object
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

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
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app.route('/api/v1.0/precipitation')
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
     
    # Query the results from the precipitation analysis
    precipitation_results = session.query(measurement.date, measurement.prcp).\
            filter(measurement.date >= dt.date(2016, 8, 23)).\
            order_by(measurement.date).all()
     
    # Close the session
    session.close()
    
    # Return converted dictionary (using date as the key and prcp as the value) as json file
    precipitation_all = []
    for date, prcp in precipitation_results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation_all.append(precipitation_dict)
        
    return jsonify(precipitation_all)


@app.route('/api/v1.0/stations')
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
     
    # Query a list of stations from the dataset
    station_results = session.query(station.station).all()
    
    # Close the session
    session.close()
    
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(station_results))
    
    # Return list of all stations in JSON format
    return jsonify(all_stations)


@app.route('/api/v1.0/tobs')
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
     
    # Query the dates and temperature observations of the most-active station for the previous year of data
    tobs_results = session.query(measurement.date, measurement.tobs).\
                                filter(measurement.date >= dt.date(2016, 8, 23)).\
                                filter(measurement.station == 'USC00519281').all()
    
    # Close the session
    session.close()
    
    # Return a JSON list of temperature observations for the previous year.
    all_tobs = []
    for date, tob in tobs_results:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tob
        all_tobs.append(tobs_dict)
    
    # Return JSON format of all temperature observations and dates
    return jsonify(all_tobs)


if __name__ == '__main__':
    app.run(debug=True)