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
[Streamlit](https://streamlit.io/) allows us to quickly build a beautiful dashboard in the form of a website. Streamlit itself is a package written for python and handles the web component parts for us. 

Like most libraries/packages/frameworks, Streamlit come with [documentation](https://docs.streamlit.io) which describes the functionality it ships with, as well as some examples. 

### Getting started guide
A good way to quickly get up-to speed with any new library is to first go through their tutorial (I prefer the  "getting started" guides).

For Streamlit, the [getting started guide](https://docs.streamlit.io/get-started) consists of:
1. [Installation](https://docs.streamlit.io/get-started/installation) (skip)
2. [Fundamentals](https://docs.streamlit.io/get-started/fundamentals) (important)
    1. Basic concepts (important, showcase of features)
    2. Advanced concepts (cool to know)
    3. Additional features (not so relevant in the beginning)
3. [First steps](https://docs.streamlit.io/get-started/tutorials) (shows how to build a functional app)
4. [Github codespaces](https://docs.streamlit.io/get-started/installation/community-cloud) (not important for us)

We can the installation, as we have take care of that in the previous section. The fundamentals give us a broad overview of what Streamlit can do, and gives hints to the functionality of the library. The examples are all seperate from each other, it's just a showcase of the features.
First steps show us how to build a functional app, from data loading, to interactive filtering and finally the visulasitation. Github codespaces is not relevant for us.

So let's get started with the "fundamentals" and work our way to "first steps"!

### Additional notes
>What is Streamlit and what does it do for us?

The library Streamlit comes with a few features such as the website and it's own plotting engine. It is important to note that we can use a number of other libraries to create plots and use Streamlit to integrate them into a website/dashboard.
We would suggest to use Streamlit's plotting functionality where it is enough, and use Plotly or Altair for more complex interactive graphs. If you want a static plot, we can also display any [matplotlib](https://matplotlib.org) base graph (such as [Plotnine](https://plotnine.org) or [Seaborn](https://seaborn.pydata.org)).

If you want to dive deeper into what good plotting libraries there are, have a look at this [blog article](https://datavizandai.github.io/2024/05/16/streamlit-five-varieties.html) when you're bored:).

>Cool! I want to see EVERY feature of Streamlit and want to know in detail how to use it, or whether I can customise it. How?

There is an API reference which goes into detail how each function should be used. It usually covers the whole library and is an exhaustive source of information to describe the capabilities of a library, for Streamlit it can be found [here](https://docs.streamlit.io/develop/api-reference).

>The API reference is too boring. Give me some creative inspiration!

Sure, here is a [gallery](https://streamlit.io/gallery) of tools build with Streamlit, most of them have code examples. You can also just google "Streamlit + Examples" to find more usescases. The world is your oyster, get creative!

>Now what?

One can spend hours exploring examples and going through tutorials. We think, the getting started guide is enough to, well, get you started. Have a look at the examples to get a feel of what's possible, and then just dive into our dataset. The best way to learn is by trying it yourself.

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

Have a look at row 82 of the data. What do you think might have happened here? 

How is `overall_completeness` calculated? Are there any exceptions?

Why do we have both `mean` and `median`? When would you be likely to use median rather than mean?



## Task 4: Data visualization with python and Streamlit

### Get your app running
Open the file `app.py`. This is a short python script which uses Streamlit to display only a title. This is our starting point for the data dashboard.

Run Streamlit by typing `streamlit run app.py` into a terminal window. What happens? 

Go back to `app.py` and add another line of code at the bottom:

    st.write("This app visualizes wearables data.")

Save the file. What happens? Go back to the browser where your app is running. There are buttons at the top labelled `Rerun`, `Always rerun`. Use one of these to update the app in the browser.

Make sure you can see your application running, and make changes to it, before you go on to the next stage.

### Load the example data
We will use a python package called [pandas](https://pandas.pydata.org/docs/user_guide/index.html) to help with loading and manipulating the data.

Add an import statement at the top of `app.py`:

    import pandas as pd

Now load in the example data using the pandas function `read_csv()` - you can learn how to use it [here](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) (skip all the way to the bottom for a very simple example!). Store the data as a variable called `df`.

Use the streamlit function `dataframe()` to add a table to the app, displaying the data. Check how it looks in the web browser. It's much easier to view the data this way, than it was in the csv file! You can sort it by whichever column you like and search for particular values.

### Create a line graph
Instead of the data frame, create a graph plotting time on the horizontal axis and the median heart rate (hr_median) on the vertical axis.
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

## Extension 5: Incorporate `Git` and GitHub into the workflow
Git is a powerful Version Control System (VCS) that we can use to keep track of our code changes and roll back to earlier versions in case we broke something (like a time machine). In addition to version control, Git allows for multiple users to efficiently collaborate on the same codebase simultaneously. 
For our use case, we will use Git together with GitHub, to share code, track issues (you can also think of them as features or tasks here), merge pull requests and more.

### Git tutorial
As before, we recommend going through a short Git tutorial to get familair with the basic commands. After that, we will apply it to our Wearables Dashboard project!

FreeCodeCamp has a great one: [Learn the Basics of Git in Under 10 Minutes
](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)

### How to use git in "bigger" project
We could use git just for version control, to commit (save) changes and to push (upload) them to a remote repository, like Github, to keep track of our code. In this extension, we would like to use Git and related tools to manage a project.
Let's simulate a bigger (collaborative) project, where each _task_ and _extension_ is split into its own _issue_.

A typical workflow could be as follows:
1. Someone (your manager, the community, you) defines a set of features they would like to see in the project
2. These tasks get added to the repository as an issue
3. [Optional] You could then add multiple issues to a milestone, which needs to be completed before the next release. (We'll skip this for now)
4. The issue is assigned to someone, and they work on it, submit a pull request and close the issue.

#### Step 1: Fork this repository
To keep this Git repository clean, we recommend you to for the project and work on your own repo. You can also commit your current code into your fork!
Here's how to do it on [Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

#### Step 2: Add issues
Add all the remaining tasks and extensions as issues to your forked repository, you can assign the issues or label them if you want (some people have tags such as "bug", "enhancement", "wontfix" etc).

#### Step 4: Write code and commit to new branch
Create a new branch for each issue and commit your code to it.
Here's how you would do it in [VSCode](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags) (or if you prefer, use the command line).

#### Step 5: Merge code into the main branch
The committed code currently resides on a separate branch (copy) compared to the main version. To make add it back to the main branch, you would need to merge them first.
Why do we go through the extra step of branches? It could be, that somebody else is working on another feature that uses the same files as you do. Branches allow us to work on seperate copies and only worry about how to combine the work at the end, when they are both ready.

It also allows us to do _code review_. We would normally like to keep the _main_ branch prestine and working. Only code that works and is approved, gets merged (added) into it.

Somebody else normally would then review your code, add comments and then when it's all good, merge it into main. If you want, we can be your code reviewers, otherwise just merge it into main:)
<!-- Think of more/better extensions -->

