import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.pgatour.com/stats/stat.02674.html'
urlTrimmed = url[:-5]
print urlTrimmed
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

# ------ Succesfully gets headers ------

headers = []
headerHTML = soup.find('thead')
differentHeaders = headerHTML.findAll('th')
for header in differentHeaders:
    headers.append(header.text)

# ------ Succesfully gets years ------

yearsHTML = soup.find('select', attrs={'id': 'yearSelector'})
yearsArray = []
for year in yearsHTML.findAll('option'):
    yearsArray.append(year.text)

# ------ Succesfully gets all players over multiple years ------

for year in yearsArray:
    newUrl = "{0}.{1}.html".format(urlTrimmed,year)
    response = requests.get(newUrl)
    html = response.content
    soup = BeautifulSoup(html)

    playerStats = soup.find('tbody')
    allPlayers = playerStats.findAll('tr')

    print ' '
    print year
    print ' '

    # ------ Succesfully pulls all information and displays appropriate headers for all stats ------

    for playerRow in allPlayers:
        if playerRow == None:
            print "Player Stats not available this year"
        else:
            playerStats = playerRow.findAll('td')
            index = 0
            print ' -- '
            for stat in playerStats:
                print headers[index] + ': ' + stat.text.replace('&nbsp;', ' ')
                index = index + 1
