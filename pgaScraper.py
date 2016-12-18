import requests
from BeautifulSoup import BeautifulSoup

# ------ Links and names of the broad stat categories ------

categories = [
    'http://www.pgatour.com/stats/categories.ROTT_INQ.html'#,
    # 'http://www.pgatour.com/stats/categories.RAPP_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RARG_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RPUT_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RSCR_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RSTR_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RMNY_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RPTS_INQ.html'
]

categoryNames = [
    'Off_the_Tee'#,
    # 'Approach_Shots',
    # 'Around_the_Green',
    # 'Scoring',
    # 'Streaks',
    # 'Money-Finishes',
    # 'Points-Rankings'
]

# ------ Begins the process of getting all stats from sub categories ------
categoryIndex = 0
for category in categories:

    # file = open('{0}.txt'.format(categoryNames[categoryIndex]), 'wb')
    # file.write('\n')
    # file.write('{')
    # file.write(categoryNames[categoryIndex])
    # file.write(':')
    # file.write('\n')
    # categoryIndex = categoryIndex + 1

    startUrl = '{0}'.format(category)
    response = requests.get(startUrl)
    html = response.content
    soup = BeautifulSoup(html)

    # print soup.prettify()

    # ------ Succesfully extracts all links to sub categories ------

    statDivs = soup.findAll('div', attrs={'class': 'table-content clearfix'})
    statLinks = []
    actualLinks = []
    subCategoryNames = []
    for stat in statDivs:
        statLinks.append(stat.findAll('a'))
    for link in statLinks:
        for sublink in link:
            actualLinks.append(sublink['href'])
            subCategoryNames.append(sublink.text)

    print subCategoryNames
    # ------------------------------------------------------------
    # ------ Begins to pull data from individual pages ------
    # ------------------------------------------------------------

    # for link in actualLinks:
    #
    #     print link
    #
    #     # ------ URL for individual stat category ------
    #
    #     url = 'http://www.pgatour.com{0}'.format(link)
    #     urlTrimmed = url[:-5]
    #     # file.write(urlTrimmed)
    #     response = requests.get(url)
    #     html = response.content
    #     soup = BeautifulSoup(html)
    #
    #     # ------ Succesfully gets headers ------
    #
    #     headers = []
    #     headerHTML = soup.find('thead')
    #     differentHeaders = headerHTML.findAll('th')
    #     for header in differentHeaders:
    #         headers.append(header.text)
    #
    #     # ------ Succesfully gets years ------
    #
    #     yearsHTML = soup.find('select', attrs={'id': 'yearSelector'})
    #     yearsArray = []
    #     for year in yearsHTML.findAll('option'):
    #         yearsArray.append(year.text)
    #
    #     # ------ Succesfully gets all players over multiple years ------
    #
    #     for year in yearsArray:
    #         newUrl = "{0}.{1}.html".format(urlTrimmed,year)
    #         response = requests.get(newUrl)
    #         html = response.content
    #         soup = BeautifulSoup(html)
    #
    #         playerStats = soup.find('tbody')
    #         allPlayers = playerStats.findAll('tr')
    #
    #         # ------ Succesfully pulls all information and displays appropriate headers for all stats ------
    #
    #         for playerRow in allPlayers:
    #             if playerRow == None:
    #                 file.write("Player Stats not available this year")
    #             else:
    #                 playerStats = playerRow.findAll('td')
    #                 index = 0
    #                 file.write('{ \n')
    #                 file.write('YEAR: ' + year + ',\n')
    #                 for stat in playerStats:
    #                     file.write(headers[index] + ': ' + stat.text.replace('&nbsp;', ' ') + ',\n')
    #                     index = index + 1
    #                 file.write('}, \n')
    # file.write('}')
    # file.close()
