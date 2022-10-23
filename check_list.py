import requests

url = "http://ergast.com/api/f1/current/driverStandings.json"

crude_resp = requests.get(url)

resp_dict = crude_resp.json()

driver_list = resp_dict["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

print(driver_list)
