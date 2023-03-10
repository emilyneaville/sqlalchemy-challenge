import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
#################################################
# Connection to the sql(ite) database
engine = create_engine('sqlite:///../Resources/hawaii.sqlite')

# reflect an existing database into a new model:
# Instatiate the 'Base' object
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

@app.route('/api/v1.0/precipitation')
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
     
    # Query the results from the precipitation analysis
    results = session.query(measurement.date, measurement.prcp).\
            filter(measurement.date >= dt.date(2016, 8, 23)).\
            order_by(measurement.date).all()
     
    # Close the session
    session.close()
    
    # Return converted dictionary (using date as the key and prcp as the value) as json file
    precipitation_all = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation_all.append(precipitation_dict)
        
    return jsonify(precipitation_all)

if __name__ == '__main__':
    app.run(debug=True)