The project charter documents the business problem and the scope of the project.

# Project Charter

## Business background

* Who is the client, what business domain the client is in.
* What business problems are we trying to address?

## Scope
* What data science solutions are we trying to build?
* What will we do?
* How is it going to be consumed by the customer?

## Personnel
* Who are on this project:
	* Microsoft:
		* Project lead
		* PM
		* Data scientist(s)
		* Account manager
	* Client:
		* Data administrator
		* Business contact
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?

# 001 - Earth Quake Detector
**Summary**: Realtime detection and visualization of earth quake
occurrences in predefined region (map segment) over a certain time.

### 1. Use Case Classification
**Complexity:**  medium complex use case with focus on the selection and 
orchestration of various Python packages and the implementation of a frontend 
to get the job done. 

**Challenges:** Processing of real-time data, geo data calcuations and visualization, 
OpenStreetMaps, web frontend development, web-service backend development.

**Team setup:** 2 to 3 students.

### 2. Story
>A simple earth quake alerting system for the masses! 

**Me:** *I'm looking for real good vibrations! Where are they?*

**You:** *No problem, I'm a Python hero!*

### 3. Functional Requirements / Expected Results
Create a command line tool, named **quakemonitor.py** that... 

1. ...starts a web server, opens a web page in the default browser that provides the
   following features:
   - A nice logo and layout. Use the HSD logo or create your own.
   - A Google-like search field at the top with a search button to update the 
     visualization. The field should be prefilled with the current location.
     Pressing the search button will read the location from the search field
     and refresh the page.
   - Below the search field a screen-filling map is shown with the selected location
     in the center, and a zoom-in factor appropriate to cover a circle with actual 
     search radius.
   - On overlay that draws the location of all earthquakes of the last 24 hours 
     into the actual map, represented by a circle contains the strength (Richter scala)
     of the earth quake and a label with the timestamp of the earth quake.
   - the web page should be update evers


2. ...the command line tool takes two arguments for configuration, a location
   either as an address or a city, region or country name or longitude and latitude
   positioning (default value: Current location of the computer), a radius 
   for the radius around the location in kilometers (default value: 250km) and
   an update frequency in seconds (default 30 sec) . 
   Samples for valid calls
   - **quakemonitor.py**
   - **quakemonitor.py --location "Paris"**
   - **quakemonitor.py --location "Silicon Valley" --radius 500**
   - **quakemonitor.py --location "Düsseldorf" --radius 100 --update 10**
   - **quakemonitor.py --long 51.246839 --lat 6.7916647 --radius 100**


### 4. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.


### 5. To get you started...
 - Web and API development with Python: https://flask.palletsprojects.com/  
 - OSM & Overpass: https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0
 - OSM Wiki: https://wiki.openstreetmap.org/wiki/Main_Page
