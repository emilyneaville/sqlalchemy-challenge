# SQLAlchemy weather station analysis and Flask API design
Woohoo! I'm going to Honolulu, Hawaii. To help with my trip planning, I want to do a climate analysis about the area. I'm interested in seeing a visualization of the latest year's worth of precipitation in Hawaii as well as designing a Flask API so I can retrieve historical weather data.

## Part 1: Analyze and Explore the Climate Data
In this file, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. I utilized SQLAlchemy ORM queries, Pandas, and Matplotlib to analyze the dataset and visualize the latest year's worth of weather data.

![Precipitation Plot](https://github.com/emilyneaville/sqlalchemy-challenge/blob/main/Climate%20Analysis/Figure%20outputs/prcp_hawaii.png)

![TOBS Dist](https://github.com/emilyneaville/sqlalchemy-challenge/blob/main/Climate%20Analysis/Figure%20outputs/tobs_dist.png)

## Part 2: Design Your Climate App
Now that I completed the initial analysis, I wanted to be able to retrieve the historical weather data that I queried... To do so, I designed a Flask API and created routes so that I can retrieve the data based on parameters such as dates, stations, and measures of precipitation and temperature.