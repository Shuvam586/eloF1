import json
import requests
from bs4 import BeautifulSoup
from bs4.element import TemplateString

def raceResultGetter(URL):
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text , "lxml")
    race_title = soup.find("h1" , class_ = "ResultsArchiveTitle").text.replace("\n" , "").replace("  " , "").title()
    race_details = soup.find("p" , class_ = "date")
    date = race_details.find("span" , class_ = "full-date").text
    circuit_info = race_details.find("span" , class_ = "circuit-info").text

    drivers = {}
    drivers_body = soup.find("tbody")
    drivers_table = drivers_body.find_all("tr")

    i = 0
    while i < len(drivers_table):
        req_level = drivers_table[i]
        req_fields = req_level.find_all("td")

        position = req_fields[1].text
        driver_no = req_fields[2].text

        driver = req_fields[3].text
        not_req_1 , name , surname , short , not_req_2 = driver.split("\n")
        driver = f"{name} {surname}"

        team = req_fields[4].text
        laps = req_fields[5].text
        time = req_fields[6].text
        points = req_fields[7].text

        temp_driver_dict = {
            "position" : position,
            "driver_no" : driver_no,
            "driver" : driver,
            "team" : team,
            "laps" : laps,
            "time" : time,
            "points" : points
        }

        drivers[i + 1] = temp_driver_dict
        i += 1


    return {
        "title": race_title,
        "date": date,
        "circuit": circuit_info,
        "drivers": drivers
    }

def raceResult(year, race_no):
    URL = f"https://www.formula1.com/en/results.html/{year}/races.html"
    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text , "lxml")

    body = soup.find("tbody")
    rows = body.find_all("tr")

    req_race = rows[race_no - 1]
    data_levels = req_race.find_all("td")

    req_level = data_levels[1]
    url_tag = req_level.find("a")

    url = url_tag['href']

    datafr = raceResultGetter(f"https://www.formula1.com{url}")

    return datafr

def raceCount(year):
    URL = f"https://www.formula1.com/en/results.html/{year}/races.html"
    html_text = requests.get(URL).text

    soup = BeautifulSoup(html_text , "lxml")

    results_table = soup.find("table" , class_ = "resultsarchive-table")
    results_body = results_table.find("tbody")
    result = results_body.find_all("tr")
    
    return len(result)

