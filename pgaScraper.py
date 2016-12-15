import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.pgatour.com/stats/stat.02673.html'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

# ------ Succesfully gets years ------

yearsHTML = soup.find('select', attrs={'id': 'yearSelector'})
yearsArray = []
for year in yearsHTML.findAll('option'):
    yearsArray.append(year.text)

# ------ Succesfully gets first player over multiple years ------

# for year in yearsArray:
#     url = "http://www.pgatour.com/stats/stat.02673.{0}.html".format(year)
#     response = requests.get(url)
#     html = response.content
#     soup = BeautifulSoup(html)
#
#     playerStats = soup.find('tbody')
#     firstPlayer = playerStats.find('td', attrs={'class': 'player-name'})
#     if firstPlayer == None:
#         print "Player Stats not avialable this year"
#     else:
#         name = firstPlayer.text.replace('&nbsp;', ' ')
#         print str(year) + ": " + name

# ------ Tests getting all players over multiple years ------
for year in yearsArray:  
    url = "http://www.pgatour.com/stats/stat.02673.{0}.html".format(year)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)

    playerStats = soup.find('tbody')
    firstPlayer = playerStats.find('td', attrs={'class': 'player-name'})
    if firstPlayer == None:
        print "Player Stats not avialable this year"
    else:
        name = firstPlayer.text.replace('&nbsp;', ' ')
        print str(year) + ": " + name
