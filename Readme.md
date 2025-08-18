# Wearables data visualization project

This python project creates an interactive visualization of data collected from wearable devices, including heart rate, respiratory rate, and temperature. This will allow a researcher or doctor to monitor a patient's status and check the data.

A device is attached to the patient's chest for a period of up to 5 days, and records their vital signs every second. 

An example data file is provided in `./data/example_data.csv`. This represents the data from a single patient (see below for more details).

The visualisation uses [Streamlit](https://streamlit.io/), a framework for generating interactive data apps. You will learn about this in Task 2.


## Task 1: Set-up and installation
Before you can begin coding you will need to do some setup steps. These include installing an IDE, installing python, installling python packages (some of these may have been done for you!), and learning how to run an example application.

### Installing an IDE 
An IDE is an interactive development environment. This is a program where you can write your code and it helps you by highlighting parts of the code like keywords in different colours, giving you suggestions, and helping you navigate between different files and tasks. [Visual Studio Code](https://code.visualstudio.com/) is recommended.


### Familiarisation with VS Code
VS Code gives you several separate panels, each of which can have lots of tabs within them, which can be confusing at first. The main panel is the top-centre panel, where you can view and edit your code. On the left is a navigation sidebar, where you can open different files, search for particular keywords, and more. At the bottom, you may have a set of tabs named 'Output', 'Terminal' etc. You will need a terminal to run your code so click Terminal -> New Terminal in the top menu, if you don't already see a terminal at the bottom.

Find the file `Readme.md`. Click to open it in the main panel. At the top right, click the button labelled 'Open Preview to the Side'. Now you can see and follow this readme file within your IDE (if you like!).

Click on `File`->`Preferences`->`Themes`->`Colour Theme` and try a couple of different light modes and dark modes. Use whichever one you prefer.


### Installing python and packages
The software and packages that you need may have already been installed for you. If not, you will need:
- The [python extension for VS Code](https://code.visualstudio.com/docs/languages/python)
- a virtual environment (optional)
- python packages, as listed in `requirements.txt`. Install these using the command `pip install -r requirements.txt`


## Task 2: Introduction to Streamlit
There are some tutorials available online:
<!-- TODO KEVIN ... -->



## Task 3: Data familiarity
The device records several measures of the patient's health, once every second, for up to 5 days. It is difficult to directly visualize this amount of data (5 days * 24 hours * 60 minutes * 60 seconds = 432,000 rows of data per patient) so the data has been [binned](https://en.wikipedia.org/wiki/Data_binning) and a summary of each bin is given instead of listing every reading. The mean, median, and amount of missing data is calculated for each measure, within each bin.

An example dataset is provided in `./data/example_data.csv`. Take a look at this (e.g. you can open it in Visual Studio Code). The data is stored in 'comma-separated variable' format. The column headings on the first row tell you what is in the rest of the rows. The abbreviations used are:
- `hr`: Heart rate (number of beats per minute)
- `rr`: Respiratory rate (number of breaths per minute)
- `rmssd`: Root mean squared standard deviation. This is an indicator of heart rate variability
- `calib`: Calibrated. The device records the patient's skin temperature, which is usually lower than their core body temperature. A calibrated temperature is one that has been adjusted to account for this difference.

The example data is real data recorded by one of the wearables devices, but it was being worn by a member of our team, not a patient. What difference do you think this might make to the data?


#### Questions:
Do you understand all the column headings? 

Have a look at row 474 of the data. What do you think might have happened here? 
<!-- TODO JO: generate data with a bigger gap -->

How is `overall_completeness` calculated? Are there any exceptions?

Why do we have both `mean` and `median`? When would you be likely to use median rather than mean?



## Task 4: Data visualization with python and Streamlit

### Get your app running
Open the file `app.py`. This is a short python script which uses Streamlit to display only a title. This is our starting point for the data dashboard.

Run Streamlit by typing `streamlit run app.py` into a terminal window. What happens? 

Go back to `app.py` and add another line of code at the bottom:
`st.write("This app visualizes wearables data.")`. Save the file. What happens? Go back to the browser where your app is running. There are buttons at the top labelled `Rerun`, `Always rerun`. Use one of these to update the app in the browser.

Make sure you can see your application running, and make changes to it, before you go on to the next stage.

### Load the example data
We will use a python package called [pandas](https://pandas.pydata.org/docs/user_guide/index.html) to help with loading and manipulating the data.

Add an import statement at the top of `app.py`:

    import pandas as pd

Now load in the example data using the pandas function `read_csv()` - you can learn how to use it [here](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) (skip all the way to the bottom for a very simple example!). Store the data as a variable called `df`.

Use the streamlit function `dataframe()` to add a table to the app, displaying the data. Check how it looks in the web browser. It's much easier to view the data this way, than it was in the csv file! You can sort it by whichever column you like and search for particular values.

### Create a line graph
Create a graph plotting time on the horizontal axis and the heart rate (hr) on the vertical axis.
<!-- TODO: add more info -->

Add labels on the axes. How else can you make the chart look nicer?

### Data selector
Add a radio button to select which data will be shown in the graph: heart rate, respiratory rate, temperature, or calibrated temperature.

Add another radio group to choose between mean and median.

<!-- TODO: add more info -->

Can you think of any better alternatives for allowing the user to switch between these different plots?


## Task 5: Load the real data
The real data consists of separate data files for many different patients. 

Update the dashboard to include a drop-down list of all the patients, and when you select one, it shows the graphs for that patient.


## Extension 1: Overview page 
Create a landing page showing a list of all the patients, their start and end dates, and how many rows of data we have for them. Add a button (or hyperlink) for each one so that the user can click through to see their data on the dashboard

## Extension 2: Generate a plot showing how many patients were wearing a device at any time during the study

## Extension 3: Change the colour of the line when there is missing data above a certain threshold

## Extension 4: Search for gaps in the data, where the device was not worn properly


<!-- TODO: Think of more/better extensions -->

