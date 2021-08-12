
# sqlalchemy-challenge
# Climate Analysis and Exploration

Python and SQLAlchemy used to do basic climate analysis and data exploration of climate database. All the analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
Start date and end date were used for the trip. The vacation range is approximately 9 days.
SQLAlchemy was used to create_engine to connect to the sqlite database.
SQLAlchemy automap_base() used to reflect tables into classes and saved a reference to those classes called Station and Measurement.

# Precipitation Analysis

Query designed to retrieve the last 12 months of precipitation data. Select only the date and prcp values. Load the query results into a Pandas DataFrame and set the index to the date column. Sort the DataFrame values by date. Plot the results using the DataFrame plot method.

![prcp](https://user-images.githubusercontent.com/83611005/129138741-a1d15c51-aca7-46c8-9b11-92827a22e680.png)

![prcp1](https://user-images.githubusercontent.com/83611005/129243489-d146ce9e-b227-484b-827f-62fc82d99b7e.png)

# Station Analsys
Design a query to calculate the total number of stations. Design a query to find the most active stations. List the stations and observation counts in descending order.
Which station has the highest number of observations? 

Design a query to retrieve the last 12 months of temperature observation data (TOBS).Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12.

![tobs](https://user-images.githubusercontent.com/83611005/129138760-581b6434-5707-407a-b55a-f33a6aad6bd8.png)



![temp](https://user-images.githubusercontent.com/83611005/129138766-42ab93e0-c128-42c0-9433-b04c451a55f0.png)

![normals](https://user-images.githubusercontent.com/83611005/129138773-bf0f7f61-36a2-4c4e-bbd1-1f01787a6b9f.png)


