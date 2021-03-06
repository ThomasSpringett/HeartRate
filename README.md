
This repository is actively being developed. Background details regarding objectives can be found in the 'project proposal' files.


## General Info
The original csv data file was too large (>100MB) to copy to GitHub. As an alternative, the data file was saved as a pickly file
which fell into the limits. 

## Built With 
This project is built with Python and Jupyter. 

## License 
Distributed under the MIT License. See LICENSE for more information.

## Objective
It is a Udacity capstone project. The objective is to analyze the heart rate distribution and determine, through machine learning 
techniques, if clusters in the data can be found. If so, how do they compliment the current target zones promoted by the CDC, Mayo 
Clinic and others. And how do these new zone definitions improve high intensity workout sessions. 

An additional objective, is demonstrating a data science analysis flow. Starting with loading  and processing input data, data exploration and data modeling and selection. 

###  Maximum Heart Rate
The first step in determining high intensity heart rate zones is to determine maximum heart rate. There are several methods for this: 

1. 220 - age. 0r 158bpm for a 62 year old.
2. Heart Rate Monitor data collected over a period of months with various activities. 
3. Using a treadmill or stationary bike with an ECG. 
Option number 1 is the most common for folks that do not have access to the treadmill and ECG. It is remarkable how well it works. The body seems to have a built in algorithm.  
After the maximum heart rate is determined, target heart rates can be determined:

### Hear Rate Intensity Zones

#### CDC
The CDC defines zones as follows: Target Heart Rate is 64% to 76%. High Intensity target heart rate is 76-93% (CDC). Or 120 to 146 for the 62 year old. 
#### MayoClinic
The Mayo Clinic defines moderate intensity as 50-70% of maximum heart rate and vigorous as 70% to 85%.
#### Polar
The heart rate monitor company Polar suggests 5 heart rate zones:
1. Very light at 50-60% of HRMAX. Boost recovery and prepare for higher zones.
2. Light 60-70%. Improve general endurance and increase capillary density.
2. Moderate at 70-80%. Lactic acid build up,improve efficiency of blood circulation in the heart and muscles
4. Hard 80-90%. Improve speed endurance.
5. Maximum 90-100%. For elite atheletes to further improve speed.
