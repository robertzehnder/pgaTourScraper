import os
import requests
from BeautifulSoup import BeautifulSoup

# ------ Links and names of the broad stat categories ------

categories = [
    # 'http://www.pgatour.com/stats/categories.ROTT_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RAPP_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RARG_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RPUT_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RSCR_INQ.html',
    # 'http://www.pgatour.com/stats/categories.RSTR_INQ.html',
    'http://www.pgatour.com/stats/categories.RMNY_INQ.html',
    'http://www.pgatour.com/stats/categories.RPTS_INQ.html'
]

categoryNames = [
    # 'Off_the_Tee',
    # 'Approach_Shots',
    # 'Around_the_Green',
    # 'Scoring',
    # 'Streaks',
    'Money-Finishes',
    'Points-Rankings'
]

# ------ Begins the process of getting all stats from sub categories ------
categoryIndex = 0
for category in categories:

    # file = open('data/data.json', 'wb')
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
            subCategoryNames.append(sublink.text.replace(' ', '_'))

    #------------------------------------------------------------
    #------ Begins to pull data from individual pages ------
    #------------------------------------------------------------

    subIndex = 0
    linkIndex = 0
    linkLength = len(actualLinks)
    for link in actualLinks:
        file = open('data/{0}/{1}.json'.format(categoryNames[categoryIndex],subCategoryNames[subIndex]), 'wb')
        # file.write('{\n')
        # file.write('{0}:'.format(subCategoryNames[subIndex]) + '{')
        # file.write('\n')

        subIndex = subIndex + 1

        # ------ URL for individual stat category ------

        url = 'http://www.pgatour.com{0}'.format(link)
        urlTrimmed = url[:-5]
        # file.write(urlTrimmed)
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)

        # ------ Succesfully gets headers ------

        headers = []
        headerHTML = soup.find('thead')
        differentHeaders = headerHTML.findAll('th')
        for header in differentHeaders:
            headers.append(header.text.replace(' ', '_'))

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

            # ------ Succesfully pulls all information and displays appropriate headers for all stats ------

            allplayersLength = len(allPlayers)
            allPlayersIndex = 0
            for playerRow in allPlayers:
                if playerRow == None:
                    file.write("Player Stats not available this year")
                else:
                    playerStats = playerRow.findAll('td')
                    index = 0
                    file.write('{' + '"' + 'index' + '"' + ':{' + '"' + '_id' + '"' + ':"' + "{0}".format(allPlayersIndex+1) + '"}}\n')
                    # file.write('{ \n')

                # 120-133
                    file.write('{"YEAR": ' + year + ',')

                    playerStatLength = len(playerStats)
                    for stat in playerStats:

                        # This looks like a job for RegEx, but don't know it well enough yet...
                        printedstat = stat.text
                        printedstat = printedstat.replace('&nbsp;', ' ')
                        printedstat = printedstat.replace(',','')
                        printedstat = printedstat.replace('$','')

                        if headers[index][:4] == 'RANK':
                            if printedstat[:1] == 'T':
                                printedstat = printedstat[1:]

                        if printedstat == '':
                            printedstat = '0'

                        try:
                            int(printedstat)
                            float(printedstat)
                        except Exception as e:
                            printedstat = '"' + printedstat + '"'

                        if index == playerStatLength - 1:
                            file.write('"{0}"'.format(headers[index]) + ': ' + printedstat)
                        else:
                            file.write('"{0}"'.format(headers[index]) + ': ' + printedstat + ',')
                        index = index + 1



                    # if allPlayersIndex == allplayersLength - 1:
                    file.write('} \n')
                    # else:
                        # file.write('}, \n')
                    allPlayersIndex = allPlayersIndex + 1
            # if linkIndex == linkLength - 1:
            #     file.write('} \n')
            # else:
            #     file.write('}, \n')
            # linkIndex = linkIndex + 1
            # file.write('}')
    file.close()
    os.system("curl -XPOST 'localhost:9200/data/{0}/_bulk?pretty' --data-binary @{1}.json".format(categoryNames[categoryIndex],subCategoryNames[subIndex]))
    categoryIndex = categoryIndex + 1
