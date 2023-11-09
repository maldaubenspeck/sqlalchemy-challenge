# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Create an instance of the Flask application
app = Flask(__name__)
# Connect to the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database tables
Base = automap_base()
Base.prepare(engine, reflect=True)
# Create references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session to interact with the database
session = Session(engine)
# Define your routes
# Route 1: Homepage
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation data<br/>"
        f"/api/v1.0/stations - List of stations<br/>"
        f"/api/v1.0/tobs - Temperature observations<br/>"
        f"/api/v1.0/start_date - Temperature statistics from start date<br/>"
        f"/api/v1.0/start_date/end_date - Temperature statistics from start date to end date"
    )
# Route 2: Precipitation data for the last year
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(func.max(Measurement.date)).scalar()
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    one_year_ago = last_date - dt.timedelta(days=365)
    # Query the last year of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    # Convert the results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)
# Implement the other routes as specified in the project instructions
# Route 3: List of stations
@app.route("/api/v1.0/stations")
def stations():
    # Query the list of stations
    results = session.query(Station.station, Station.name).all()
    # Convert the results to a list of dictionaries
    station_list = [{"Station": station, "Name": name} for station, name in results]
    return jsonify(station_list)
# Add routes for temperature observations and statistics
# Route 4: Temperature observations
# Route 5: Temperature statistics for a specified start date
# Route 6: Temperature statistics for a specified start and end date
if __name__ == "__main__":
    app.run(debug=True)
#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
