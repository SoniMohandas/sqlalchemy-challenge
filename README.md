
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

# Temperature Analysis
The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates. Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates.
Plot the min, avg, and max temperature from your previous query as a bar chart. Use the average temperature as the bar height. Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

![temp](https://user-images.githubusercontent.com/83611005/129138766-42ab93e0-c128-42c0-9433-b04c451a55f0.png)

# Daily Rainfall Average
Calculate the rainfall per weather station using the previous year's matching trip dates. Create a list of dates for the trip in the format %m-%d. Use hisdtoric TOBS that match the date string. Calculate the daily normals means min, avg, and max temperatures for each date string and append the results to a list. Load the list of daily normals into a Pandas DataFrame and set the index equal to the date. Use Pandas to plot an area plot (stacked=False) for the daily normals.

![normals](https://user-images.githubusercontent.com/83611005/129138773-bf0f7f61-36a2-4c4e-bbd1-1f01787a6b9f.png)


