# Udacity-ND-Programming-for-Data-Science-with-Python
# Udacity and Misk 
# Created by Marwan Saeed Alsharabbi
## Project 2

### Overview

In this project, the student had to make use of Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. The student had to write code to 
(a) import the data and answer interesting questions about it by computing descriptive statistics, and 
(b) write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.


## Statistics Computed

1. Popular times of travel (i.e., occurs most often in the start time)

   - most common month
   - most common day of week
   - most common hour of day

2. Popular stations and trip

   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

   - total travel time
   - average travel time

4. User info

   - counts of each user type
   - counts of each gender (only available for NYC and Chicago)
   - earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Project Submission

The developed CLI program allows the user to explore an US bikeshare system database and retrieve statistics information from the database. The user is able filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data. The user is also able to chose to view raw data and to sort this data by columns, in ascending or descending order.


### Python Learning In The Course

Check the link for my learning material.
[Check this out](https://github.com/marwan1023/udacity-Programming-for-Data-Science-with-Python-ND/blob/master/bikeshare.py)

#### Files Used

The required files for running this program are: 

* washington.csv
* new_york_city.csv
* chicago.csv

#### Requirements
This program was written in Python (version 3.7.1) and relies on the following libraries:

* import time
* import pandas as pd
* import numpy as np
* import calendar
* import matplotlib.pyplot as plt
* import statistics  
