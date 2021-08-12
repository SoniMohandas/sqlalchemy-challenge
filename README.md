
# sqlalchemy-challenge
# Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
Use SQLAlchemy create_engine to connect to your sqlite database.
Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

# Precipitation Analysis

Design a query to retrieve the last 12 months of precipitation data.
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.

![prcp](https://user-images.githubusercontent.com/83611005/129138741-a1d15c51-aca7-46c8-9b11-92827a22e680.png)

![tobs](https://user-images.githubusercontent.com/83611005/129138760-581b6434-5707-407a-b55a-f33a6aad6bd8.png)

![temp](https://user-images.githubusercontent.com/83611005/129138766-42ab93e0-c128-42c0-9433-b04c451a55f0.png)

![normals](https://user-images.githubusercontent.com/83611005/129138773-bf0f7f61-36a2-4c4e-bbd1-1f01787a6b9f.png)


