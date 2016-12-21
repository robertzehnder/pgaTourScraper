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
    # 'off_the_tee',
    # 'approach_shots',
    # 'around_the_green',
    # 'scoring',
    # 'streaks',
    'money-finishes',
    'points-rankings'
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
        file = open('{0}.json'.format(subCategoryNames[subIndex].lower()), 'wb') #categoryNames[categoryIndex].lower(),
        # file.write('{\n')
        # file.write('{0}:'.format(subCategoryNames[subIndex]) + '{')
        # file.write('\n')



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

        headerLength = len(headers)

        # ------ Succesfully gets years ------

        yearsHTML = soup.find('select', attrs={'id': 'yearSelector'})
        yearsArray = []
        for year in yearsHTML.findAll('option'):
            yearsArray.append(year.text)

        # ------ Succesfully gets all players over multiple years ------
        esIndexCounter = 0
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

                    file.write('{' + '"' + 'index' + '"' + ':{' + '"' + '_index' + '"' + ':' + '"' + categoryNames[categoryIndex].lower() + '",' + '"' + '_type' + '"' + ':' + '"' + subCategoryNames[subIndex].lower() + '",' + '"' + '_id' + '"' + ':' + "{0}".format(esIndexCounter) + '}}\n')



                    file.write('{"YEAR": ' + year + ',')

                # ------ Prints out all stats for a player for a given year ------

                    playerStatLength = len(playerStats)
                    potato = 0
                    stringToBuild = ''
                    dataType = ''

                    for stat in playerStats:

                    # ------ Error Handling Section to create desirable data format for JSON file ------

                        # This looks like a job for RegEx, but don't know it well enough yet...Replace bad characters
                        printedstat = stat.text
                        printedstat = printedstat.replace('&nbsp;', ' ')
                        printedstat = printedstat.replace(',','')
                        printedstat = printedstat.replace('$','')

                        # Check to see if header is longer than 4, so no OB error. Then see if rank, then see if there's a T for tie and correct it to make it an integer


                        try:
                            if len(headers[index]) >= 4:
                                if headers[index][:4] == 'RANK':
                                    if printedstat[:1] == 'T':
                                        printedstat = printedstat[1:]
                        except Exception as e:
                            break

                        print 'Category: {0}'.format(subCategoryNames[subIndex].lower())
                        print 'this is the index: {0}'.format(index)
                        print 'This is the category being printed {0}'.format(headers[index])
                        print 'year: {0}'.format(year)
                        print 'Index to trigger string builder {0}'.format(allPlayersIndex)


                        # If it's blank, make it a zero
                        if printedstat == '':
                            printedstat = '0'
                            printedstat = int(printedstat)

                        # Format all data into int, float, or string, so that it can comply with JSON format and be easy to manipulate for schema template creation
                        try:
                            if float(printedstat):
                                printedstat = float(printedstat)
                            if int(printedstat):
                                printedstat = int(printedstat)
                        except Exception as e:
                            printedstat = '"' + str(printedstat) + '"'

                        # print '{0}: {1}'.format(headers[index],type(printedstat))
                        if index == playerStatLength - 1:
                            file.write('"{0}"'.format(headers[index]) + ': {0}'.format(printedstat))
                        else:
                            file.write('"{0}"'.format(headers[index]) + ': {0}'.format(printedstat) + ',')



                        if esIndexCounter == 0:
                            if potato == 0:
                                stringToBuild+=str('"' + 'YEAR' + '" : {"type' + '" : "' + 'integer' + '"},')
                                potato = potato + 1
                            if type(printedstat) is int:
                                dataType = 'integer'
                            elif type(printedstat) is float:
                                dataType = 'float'
                            else:
                                dataType = 'text'
                                # print headers
                            if dataType == 'text':
                                if index == headerLength - 1:
                                    stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" , "fielddata": true, "index" : "not_analyzed"}')
                                else:
                                    stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" , "fielddata": true, "index" : "not_analyzed"},')

                            if index == headerLength - 1:
                                stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" }')
                            else:
                                stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" },')

                        index = index + 1
                    file.write('} \n')
                    print ' '
                    print stringToBuild
                    print ' '

                    allPlayersIndex = allPlayersIndex + 1
                    esIndexCounter = esIndexCounter + 1 # Counter for Elasticsearch index template. Increments for indicies
            # if linkIndex == linkLength - 1:
            #     file.write('} \n')
            # else:
            #     file.write('}, \n')
            # linkIndex = linkIndex + 1
            # file.write('}')
        # commandString = 'curl -XPUT ' + '"' + "http://localhost:9200/{0}".format(subCategoryNames[subIndex].lower()) + '"' + " -d' " + '{' + '"' + 'mappings' + '"' + ' : {' + '"' + '_default_' + '" : {' + '"' + 'properties' + '"'
        # commandString += str(": {" + stringToBuild + " }}}}'")
        # print commandString
        subIndex = subIndex + 1
    file.close()
    # os.system("curl -XPOST 'localhost:9200/data/{0}/_bulk?pretty' --data-binary @{1}.json".format(categoryNames[categoryIndex],subCategoryNames[subIndex]))
    categoryIndex = categoryIndex + 1
