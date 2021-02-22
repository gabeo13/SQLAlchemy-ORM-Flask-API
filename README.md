# sqlalchemy-challenge {Surfs Up!}
![](img/sqlalchemy.jpg)

---
# Background & Challenge
To aid in planning a trip to Hawaii, analyze temperature and precipitation data. Develop a Flask API to share information on common Hawaii climate queries. 

## Analysis & API Development Toolkit
* Python
* Pandas
* Matplotlib
* Seaborn
* SQLite
* SQLalchemy ORM
* Flask
* GitBash

---
# Precipitation Analysis
* As seen in the figure below, it rains quite frequently in Hawaii, suggesting that any traveler come prepared with appropriate rain gear (umbrella, jacket, footwear, etc.)

![](img/precip.png)

*Fig 1: Precipitation 2016-2017*

![](img/prcp_stats.png)

*Table 1: Precipitation Stats 2016-2017*

![](img/total_prcp.png)

*Table 2: Total precipitation by station for 6-day trip in early March*

---
# Temperature Analysis
In addtion to understanding precipitation levels, temperature must also be evaluated to fully understand what needs to be packed for the trip. In Figure 2 and Table 3 we see that daily normal temperature across the state remain relatively flat over the course of the trip with the average daily temperature plotted in Figure 3. In general temperatures remain relatively temperate year-round as seen in Figure 4. Temperatures do fluctuate enough between summer and winter to be statistically significant as seen in Figure 5, and this must be evaluated while planning future trips. 

![](img/plot_daily_normals.png)

*Figure 2: Area Plot Daily Normals*

![](img/daily_normals.png)

*Table 3: Daily Normals*

![](img/trip_avg_temp.png)

*Figure 3: Average Daily Temperature w/Error Bar*

![](img/temps.png)

*Figure 4: Temperature Distribution for most active station*

![](img/ttest.png)

*Figure 5: Paired T-Test Results*

---
# Weather Station Analysis
Researching the source of the weather data is an important analytical step. From analysis of the station information we determine that there are nine (9) weather stations. Table 4 organizes these stations by frequency of reported measurements. Addtional station information may be found in Table 2.

![](img/station_count.png)

*Table 4: Frequency of temperature data reporting by station*

![](img/active_station.png)

*Table 5: Temperature measures for most active station*

---
# Climate App {Flask API}
Design a Flask API based on the queries developed for the analysis. (see app.py file)

### Routes


 > '/'

    * Home page.
    * List all routes that are available.

> /api/v1.0/precipitation

    * Convert the query results to a dictionary using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.

> /api/v1.0/stations

    * Return a JSON list of stations from the dataset.

> /api/v1.0/tobs

    * Query the dates and temperature observations of the most active station for the last year of data.
    * Return a JSON list of temperature observations (TOBS) for the previous year.

> /api/v1.0/<start> and /api/v1.0/<start>/<end>

    * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

    * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

    * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.