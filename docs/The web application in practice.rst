The web application in practice
===============================


========
The data
========

To feed our dashboard , we need to access Google Cloud through an API. In this database is historicized the data from the stations every one hour. Each data is then modeled according to our needs and recorded in Google spread Sheet and this, in real time. Thus, 4 Google spread Sheet data sets will be created:

* the transmission pressure (PT), the temperature (TT), the transmission flow (FT) and the valve control pressure (PCV) according to time (year, month, day, hour)
* the location of all McPhy stations and their status
* energy consumption (kVA, KVAR, kW) as a function of time (year, month, day, hour) - motor data (air compressor, D1 cooling unit, air extractor) as a function of time (year, month, day, hour)


======================
Graphics
======================

In the dashboard, five (05) types of graphs are used to illustrate the data.

* Time series to follow in a first graph the evolution of the transmission pressure, temperature, transmission flow and control pressure of the valves over time, and in a second graph the evolution of the energy consumption.
* A Mapbox that allows a statistical representation of numerical data of transmission pressure, temperature, transmission flow and valve control pressure over time through their quartiles and median.
* A Mapbox Maps, which is a map that displays in a web browser the location of all hydrogen stations and their status (Offline, Not Available, Coming Soon and Available) by attaching individually requested vector data.
* The Sunburst graph, equivalent to a pie chart, visualizes the hierarchical location data of the different stations.
* A bar chart to represent the data of the motors (air compressor, D1 cooling unit, air extractor)



===========================
How to run the app locally?
===========================

**First create a virtual environment with conda or venv inside a temp folder, then activate it.**


*virtualenv venv*

| **Windows**
| *venv\Scripts\activate*
| **Or Linux**
| *source venv/bin/activate*


**Download the folder on your computer or**
**Clone the git repo, then install the requirements with pip**


In your terminal type :
  
* git clone [the link of the project on github]
* cd [position yourself in the folder]
* pip install -r requirements.txt or :

  * pip install dash
  * pip install jypyter-dash
  * pip install pandas



**Run the app**

*python app.py*

After execution of the script app.py we obtain :
*$ python app.py*
*...Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)*

open this link: http://127.0.0.1:8050/ to see the application


