# F1 Championship Standings Prediction Tool
#### Video Demo:  https://youtu.be/QtBY-aD78Cs
#### Description:

This project uses a F1 API (http://ergast.com/mrd/). This API was used to service the application with the necessary informations such as driver infos, races in the current season, etc.

Serviced driver information:
    - Driver name
    - Driver's code
    - Driver's permanent number
    - Driver's current point count
    - Driver's current position

Serviced race information:
    - Race round
    - Race name
    - Race location
    - Sprint (as a dict key, if sprint element existant)
    - Race date

#### Python files
Three Python files were created
### app.py
The main Python file. In this file the Flask configuration was made, the main application logic was set and functions were called.

### variables.py
I used this file in order to set global variables, define functions and import libraries. This was done in order to make the app.py file more concise (only one line was used in app.py to import all modules and functions from variables.py, which in turn has multiple lines that do not have to do with the app's main logic).

### check_list.py
This was only used in order to run specific lists. This file does not have to do with the app's main usage.

#### html files

### apology.html
This template was used once (when a user inputs the same arriving position for two different drivers in a same round). It simple. It contains a explaining text and a link that redeirects the user to the predictions table.

### layout.html
This sets the basic page information for all other pages (this application used Jinja to extend html pages). Header information, reference to static files, and other main .html layout information was set in this file.

### predictions.html
This page rendered the predictions input table. Each input box has the following id: {{driver}}{{round}}. For each drivers position (for instance, driver currently in first place), there is an input box for a specific round (for instance, round 18). As a result, this input box is 118 (not the 118th input, the input for the driver in the first position in the 18th race).

### results.html
This page takes each of the {{driver}}{{round}} inputs and processes it. After running each prediction through an if clause (if "1", then 25 points and so on), the app returns the predicted points for each driver. The app then adds the predicted points to the current points, then adds that to the final dictionary.

### standings.html
This template has very little added python logic. It simply requests the driver information (which contains their points) and returns it in the form of a table.

### welcome.html
Simple text explaining the user what the application does with a link that takes the user to the standings table.

#### static
### styles.css
This file contains the little css that was applied to the application. Table formatting, flex display and border were set here.

### f1.png
This free use icon was set because a picture conveys the ability of making the user associate what the website is about (better than text in most cases).

#### Other files
Files like flas_session and __pycache__ were created by python and flask.