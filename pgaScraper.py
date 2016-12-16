import requests
from BeautifulSoup import BeautifulSoup


# categories = [
#     'http://www.pgatour.com/stats/categories.ROTT_INQ.html',
#     'http://www.pgatour.com/stats/categories.RAPP_INQ.html',
#     'http://www.pgatour.com/stats/categories.RARG_INQ.html',
#     'http://www.pgatour.com/stats/categories.RPUT_INQ.html',
#     'http://www.pgatour.com/stats/categories.RSCR_INQ.html',
#     'http://www.pgatour.com/stats/categories.RSTR_INQ.html',
#     'http://www.pgatour.com/stats/categories.RMNY_INQ.html',
#     'http://www.pgatour.com/stats/categories.RPTS_INQ.html'
# ]
#
# ------ Fix this so that you can target the categories within the different categories -- Find the urls that you need for all the stat categories

startUrl = 'http://www.pgatour.com/stats/categories.ROTT_INQ.html'
response = requests.get(startUrl)
html = response.content
soup = BeautifulSoup(html)


# finds all stat sub categories on a stat category home page
statDivs = soup.findAll('div', attrs={'class': 'table-content clearfix'})
index = 0
statLinks = []
for stat in statDivs:
    statLinks.append(soup.findAll('li', attrs={'data-category-index': index}))
    print statLinks[index]
    index = index + 1

print statLinks[0]
# # ------ URL for individual stat category ------
#
# url = 'http://www.pgatour.com/stats/stat.02674.html'
# urlTrimmed = url[:-5]
# print urlTrimmed
# response = requests.get(url)
# html = response.content
# soup = BeautifulSoup(html)
#
# # ------ Succesfully gets headers ------
#
# headers = []
# headerHTML = soup.find('thead')
# differentHeaders = headerHTML.findAll('th')
# for header in differentHeaders:
#     headers.append(header.text)
#
# # ------ Succesfully gets years ------
#
# yearsHTML = soup.find('select', attrs={'id': 'yearSelector'})
# yearsArray = []
# for year in yearsHTML.findAll('option'):
#     yearsArray.append(year.text)
#
# # ------ Succesfully gets all players over multiple years ------
#
# for year in yearsArray:
#     newUrl = "{0}.{1}.html".format(urlTrimmed,year)
#     response = requests.get(newUrl)
#     html = response.content
#     soup = BeautifulSoup(html)
#
#     playerStats = soup.find('tbody')
#     allPlayers = playerStats.findAll('tr')
#
#     print ' '
#     print year
#     print ' '
#
#     # ------ Succesfully pulls all information and displays appropriate headers for all stats ------
#
#     for playerRow in allPlayers:
#         if playerRow == None:
#             print "Player Stats not available this year"
#         else:
#             playerStats = playerRow.findAll('td')
#             index = 0
#             print ' -- '
#             for stat in playerStats:
#                 print headers[index] + ': ' + stat.text.replace('&nbsp;', ' ')
#                 index = index + 1
