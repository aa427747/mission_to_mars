# mission_to_mars
Unit 13 - Webscraping and Document Databases

### Overview
In this assignment, we built a web application that scrapes various websites for data related to the Mars and displays the information in a single HTML page. The following outlines what you need to do.

### Getting Started

The mission_to_mars_rjg.ipynb contains the initial scrapping, but then was moved into the scrape_mars.py file and executed through the the app.py and uses the MongoDB.  The mission to mars screen prints are in the word document to be downloaded.

There are 2 versions of the scraping code.  Version 1 is the Jupyter Notebook, which is what was used to initially create the scrape.  We then moveed that over in to the .py file in order for the app to perform the scrape, hold the data in a Mongo database and then pull that held information into the the webpage.

### Prerequisites

All the necessary libraries should be loaded in the app.py and scrape.mars.py.  These are built with BeautifulSoup and Spliter, so make sure you have those installed.  The back-end database for this exercise is Mongodb.

Requirements:
selenium==3.5.0
splinter==0.7.6

### Installing

To run the code, you will run the app.py to get the Flask app running.  Once that is up and running, then go to your local host and the template should bring up the site.  Pushing the button will begin the web scrape and it will return a series of information on Mars.  

### Built With

* Python [3.7.1]
* Jupyter [5.7.4]
