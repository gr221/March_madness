import requests
import urllib.robotparser
from bs4 import BeautifulSoup
import pandas as pd

#function to check if the robots.txt allows parsing th site
def check_robot(url, user_agent):
    robotparser = urllib.robotparser.RobotFileParser()
    robotparser.set_url(url+'/robots.txt')
    robotparser.read()
    print(robotparser.can_fetch(user_agent,url))
    return robotparser.can_fetch(user_agent, url)

#tries to establish a connection to url
def connect(url, user_agent):
    connection = requests.get(url, user_agent)
    if connection.status_code:
        return connection
    else:
        print("Error connecting to {}.".format(url))
        return 0

if __name__=="__main__":
    user_agent = 'python-requests/2.18.4 (Compatible; John Doe)'
    # if check_robot(url, user_agent):
    url = "http://statisticstimes.com/economy/countries-by-gdp-growth.php"
    connection = connect(url, user_agent)
    if not connection:
        print("No connection possible. Aborting!")
        # return -1
    # print(connection)
    # print(connection.text)
    soup = BeautifulSoup(connection.text, 'html.parser')
    table = soup.tbody.find_all('td')
    columns = ["Country", "2014", "Rank", "2015",
        "Rank", "Continent"]
    data = pd.DataFrame(columns = columns)
    # data = pd.DataFrame()
    # print(table)
    for i in range(0, len(table)-6, 6):
        # print(table[i].text)
        row = pd.DataFrame([table[i].text, float(table[i+1].text),
            int(table[i+2].text), float(table[i+3].text), int(table[i+4].text),
            table[i+5].text], columns = columns)
        data.append(row)
        # data.append([table[i].text, float(table[i+1].text), int(table[i+2].text),
        #         float(table[i+3].text), int(table[i+4].text), table[i+5].text])
        # data.append(row, index=["Country", "2014", "Rank", "2015",
        #     "Rank", "Continent"])
    print(data)
    # print(soup.prettify())
    # print("tbody")
    # print(soup.tbody)
    # print(soup.tbody.find_all('td'))
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
