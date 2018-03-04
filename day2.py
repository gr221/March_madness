import requests
import urllib.robotparser

def connect(url, **kwargs):
    user_agent = 'python-requests/2.18.4 (Compatible; John Doe)'
    try:
        connection = requests.get(url, user_agent)
        return connection
    except:
        print("Could not connecto to ",url)
        return 0

def check_robot(url, **kwargs):
    user_agent = 'python-requests/2.18.4 (Compatible; John Doe)'
    robotparser = urllib.robotparser.RobotFileParser()
    robotparser.set_url(url)
    robotparser.read()
    return robotparser.can_fetch(user_agent, url)



if __name__=='__main__':
    url = 'http://kicker.de'
    connection = connect(url)
    if connection:
        print(connection)
        # print(connection.text)

    print(check_robot(url))
