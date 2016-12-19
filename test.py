link = '/potato'
url = 'http://www.pgatour.com{0}'.format(link)
num = 21
#
# if int(link) is not int:
#     print 'asdf'

try:
    int(num)
    float(num)
except Exception as e:
    print "asfasdfasdfasdf"

print type(num)
# import os
# os.system("curl -XPOST 'localhost:9200/data/Off_the_Tee/_bulk?pretty' --data-binary @Ball_Speed.json")
#                     playerStatLength = len(playerStats)
#                     for stat in playerStats:
#                         print stat
#                         printedstat = stat.text.replace(',', '')
#                         if type(printedstat) is not int:
#                             if type(printedstat) is not float:
#                                 if type(printedstat) is not str:
#                                     printedstat = '"' + printedstat + '"'
#
#                         print printedstat
#                         if index == playerStatLength - 1:
#                             file.write('"{0}"'.format(headers[index]) + ': ' + printedstat.text.replace('&nbsp;', ' '))
#                         else:
#                             file.write('"{0}"'.format(headers[index]) + ': ' + printedstat.text.replace('&nbsp;', ' ') + ',')
#                         index = index + 1
#                     if allPlayersIndex == allplayersLength - 1:
#                         file.write('} \n')
#                     else:
#                         file.write('}, \n')
#                     allPlayersIndex = allPlayersIndex + 1
#
#
# for ch in [',','&nbsp;']:
# ...   if ch in printedstat:
# ...      printedstat=printedstat.replace(ch,"\\"+ch)
