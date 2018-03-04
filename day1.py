import requests
import urllib.robotparser

def connect(url, user_agent):
    #Try to make a request at url with user_agent raise an exception
    #if there is a problem
    try:
        request = requests.get(url,user_agent)
        print(request)
    except:
        print("There was a problem")

def parse_robots(url, user_agent):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url+'/robots.txt')
    try:
        rp.read()
        print(rp)
    except:
        print("There was a problem readint the robots.txt at ", url)

# request = requests.get(url)
# print(request)
# print("Status code {} returned.".format(request.status_code))

# robot = requests.get(url+'/robots.txt')
# print(robot)

if __name__ == '__main__':
    user_agent = 'python-requests/2.18.4 (Compatible; John Doe)'
    url = 'http://kicker.de'
    # url = 'https://google.com'
    connect(url, user_agent)
    parse_robots(url, user_agent)

