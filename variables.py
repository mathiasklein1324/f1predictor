# Import libraries
import os
import requests
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "signed_cookies"
 
Session(app)

# Define functions
def check_remaining_races(race_list):
    rem_races_list.clear()
    for race in race_list:
        date_check = datetime.strptime(race["date"], "%Y-%m-%d")
        # today = datetime.strptime(str(datetime.today()), "%Y-%m-%d")
        today = datetime.today()
        if date_check > today:
            rem_races_list.append(race)
        
        if "sprint_date" in race:
            date_check = datetime.strptime(race["sprint_date"], "%Y-%m-%d")
            today = datetime.today()
            if date_check > today:
                rem_races_list.append(race)

    return rem_races_list

def generate_standings_list():
    standings_list.clear()
    for driver in driver_list:
        position = (driver["position"])
        code = (driver["Driver"]["code"])
        name = (driver["Driver"]["givenName"] + " " + driver["Driver"]["familyName"])
        points = (driver["points"])
        perm_number = (driver["Driver"]["permanentNumber"])
        wins = (driver["wins"])
        constructor = (driver["Constructors"][0]["name"])
        driver_info = {
            "position": position,
            "code": code,
            "name": name,
            "points": points,
            "perm_number": perm_number,
            "wins": wins,
            "constructor": constructor,
        }
        standings_list.append(driver_info)
    return standings_list
 
def generate_concise_race_list():
    race_list.clear()
    for race in race_info_list:
        race_name = race["raceName"]
        circuit_name = race["Circuit"]["circuitName"]
        city = race["Circuit"]["Location"]["locality"]
        country = race["Circuit"]["Location"]["country"]
        date = race["date"]
        round = race["round"]
        if "Sprint" in race:
            sprint_date = race["Sprint"]["date"]
            sprint_dict = {
                "race_type": "sprint",
                "race_name": race_name,
                "circuit_name": circuit_name,
                "city": city,
                "country": country,
                "date": sprint_date,
                "round": str(round) + "(Sprint)"
            }
            race_dict = {
                "race_type": "normal",
                "race_name": race_name,
                "circuit_name": circuit_name,
                "city": city,
                "country": country,
                "date": date,
                "round": round
            }
            race_list.append(sprint_dict)
            race_list.append(race_dict)
        else:
            race_dict = {
                "race_type": "normal",
                "race_name": race_name,
                "circuit_name": circuit_name,
                "city": city,
                "country": country,
                "date": date,
                "round": round
            }
            race_list.append(race_dict)

    return race_list

# Define variables
driver_url = "http://ergast.com/api/f1/current/driverStandings.json"

driver_resp = requests.get(driver_url)

driver_dict = driver_resp.json()

driver_list = driver_dict["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

total_driver_count = len(driver_list)

driver_count = total_driver_count - 2

standings_list = []

current_year = str((date.today()).year)

schedule_url = "http://ergast.com/api/f1/" + current_year + ".json"

schedule_resp = requests.get(schedule_url)

schedule_dict = schedule_resp.json()

race_count = schedule_dict["MRData"]["total"]

race_info_list = schedule_dict["MRData"]["RaceTable"]["Races"]

race_list = []

rem_races_list = []

predictions_list = []
