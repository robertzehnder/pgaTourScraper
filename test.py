import os
# var x =  "YEAR" : { "type" : "integer" },"RANK_THIS_WEEK" : { "type" : "integer" },"RANK_LAST_WEEK" : { "type" : "integer" },"PLAYER_NAME" : {"type": "text", "fielddata": true, "index" : "not_analyzed" },"EVENTS" : { "type" : "integer" },"MONEY" : { "type" : "integer" },"YTD_VICTORIES" : { "type" : "integer" }
#
# '"' + header + '" : {"type' + '" : "' + dataType + '" },'
#
# '"' + header + '" : {"type' + '" : "' + dataType + '" }'

headers = ['YEAR','RANK_THIS_WEEK','RANK_LAST_WEEK','PLAYER_NAME','EVENTS','MONEY','YTD_VICTORIES']
stringToBuild = ''
thingarray = [1,2,3,'asdf',5,4,4]
length = len(thingarray)
header = "asdf"
dataType = ''
index = 0
for i in thingarray:
    # print type(thingarray[index])
    if type(thingarray[index]) is int:
        dataType = 'integer'
    elif type(thingarray[index]) is float:
        dataType = 'float'
    else:
        dataType = 'text'
# , "fielddata": true, "index" : "not_analyzed"

    if dataType == 'text':
        if index == length - 1:
            # print dataType
            stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" , "fielddata": true, "index" : "not_analyzed"}')
        else:
            # print dataType
            stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" , "fielddata": true, "index" : "not_analyzed"},')

    if index == length - 1:
        # print dataType
        stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" }')
    else:
        # print dataType
        stringToBuild+=str('"' + headers[index] + '" : {"type' + '" : "' + dataType + '" },')
    index += 1
# print stringToBuild

commandString = 'curl -XPUT ' + '"' + "http://localhost:9200/official_money" + '"' + " -d' " + '{' + '"' + 'mappings' + '"' + ' : {' + '"' + '_default_' + '" : {' + '"' + 'properties' + '"'

commandString += str(": {" + stringToBuild + " }}}}'")
print commandString
os.system(commandString)

# curl -XPUT "http://localhost:9200/official_money" -d' {"mappings" : {"_default_" : {"properties": {"YEAR" : {"type" : "integer" },"RANK_THIS_WEEK" : {"type" : "integer" },"RANK_LAST_WEEK" : {"type" : "integer" },"PLAYER_NAME" : {"type" : "text" , "fielddata": true, "index" : "not_analyzed"},"PLAYER_NAME" : {"type" : "text" },"EVENTS" : {"type" : "integer" },"MONEY" : {"type" : "integer" },"YTD_VICTORIES" : {"type" : "integer" } }}}}'
#
# curl -XPUT "http://localhost:9200/official_money" -d' {"mappings" : {"_default_" : {"properties" : {"YEAR" : { "type" : "integer" },"RANK_THIS_WEEK" : { "type" : "integer" },"RANK_LAST_WEEK" : { "type" : "integer" },"PLAYER_NAME" : {"type": "text", "fielddata": true, "index" : "not_analyzed" },"EVENTS" : { "type" : "integer" },"MONEY" : { "type" : "integer" },"YTD_VICTORIES" : { "type" : "integer" }   }}}}'
#
#
#











# os.system('curl -XPUT' "http://localhost:9200/official_money"  '-d' '{"mappings" : {"_default_" : {"properties" : {1}}}}'.format(stringToBuild))
# os.system(commandString)

# os.system("curl -XPUT" "http://localhost:9200/official_money" '-d' '{"mappings" : {"_default_" : {"properties" : {"YEAR" : { "type" : "integer" },"RANK_THIS_WEEK" : { "type" : "integer" },"RANK_LAST_WEEK" : { "type" : "integer" },"PLAYER_NAME" : {"type": "text", "fielddata": true, "index" : "not_analyzed" },"EVENTS" : { "type" : "integer" },"MONEY" : { "type" : "integer" },"YTD_VICTORIES" : { "type" : "integer" }   }}}}')

# link = '/potato'
# url = 'http://www.pgatour.com{0}'.format(link)
# num = 21
# #
# # if int(link) is not int:
# #     print 'asdf'
#
# try:
#     int(num)
#     float(num)
# except Exception as e:
#     print "asfasdfasdfasdf"
#
# print type(num)
# # import os
# # os.system("curl -XPOST 'localhost:9200/data/Off_the_Tee/_bulk?pretty' --data-binary @Official_Money.json")
# #                     playerStatLength = len(playerStats)
# #                     for stat in playerStats:
# #                         print stat
# #                         printedstat = stat.text.replace(',', '')
# #                         if type(printedstat) is not int:
# #                             if type(printedstat) is not float:
# #                                 if type(printedstat) is not str:
# #                                     printedstat = '"' + printedstat + '"'
# #
# #                         print printedstat
# #                         if index == playerStatLength - 1:
# #                             file.write('"{0}"'.format(headers[index]) + ': ' + printedstat.text.replace('&nbsp;', ' '))
# #                         else:
# #                             file.write('"{0}"'.format(headers[index]) + ': ' + printedstat.text.replace('&nbsp;', ' ') + ',')
# #                         index = index + 1
# #                     if allPlayersIndex == allplayersLength - 1:
# #                         file.write('} \n')
# #                     else:
# #                         file.write('}, \n')
# #                     allPlayersIndex = allPlayersIndex + 1
# #
# #
# # for ch in [',','&nbsp;']:
# # ...   if ch in printedstat:
# # ...      printedstat=printedstat.replace(ch,"\\"+ch)
