var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');
var rp = require('request-promise');
var $ = require('jQuery');
require("jsdom").env("", function(err, window) {
    if (err) {
        console.error(err);
        return;
    }

    var $ = require("jquery")(window);
});
var url = 'http://www.pgatour.com/stats/stat.02671.html'


request(url, function(error, response, body) {
  if(error) {
    console.log("Error: " + error);
  }
  console.log("Status code: " + response.statusCode);

  var $ = cheerio.load(body);
  // console.log(body);


// --- Gets the years of the stat category
  var years = []
  $('#yearSelector > option').each(function( index ) {
    var year = $(this).val().trim();
    years.push(year)
  });
    counter = 0
    console.log('hits');
          for (var i = 0; i < years.length; i++) {
            url = `http://www.pgatour.com/stats/stat.02394.${years[i]}.html`
            // console.log(url);

            request(url, function(error, response, body) {
              var $ = cheerio.load(body);
              console.log(url);
                // console.log(`--- ${years[counter]} ---`);
                firstPlayer = $('#statsTable > tbody > tr').first().text()
                console.log(firstPlayer);
                counter ++
            })
}

// // --- Section that picks up the headers on the page
//
//   var headers = []
//   $('#statsTable > thead > tr > th').each(function( index ) {
//     var tableField = $(this).text().trim();
//     headers.push(tableField)
//   });
//
//
// tableLength = $('tbody > tr').length //finds rows in table
//
// // --- Finds each statistical attribute for each player
//
//   $('tbody > tr').each(function( index ) {
//
//     //get player name for instance
//     var player = $(this).find('.player-name').text().trim()
//
//     //array to hold stats for player instance
//     var playerStats = []
//
//     //get all the stats for the player instance
//     $(this).find('td').each (function(index) {
//       var playerValue = `${headers[index]}: ${$(this).text().trim()}`
//       playerStats.push(playerValue) //inject into array
//     });
//
//     // Builds JSON object for each player
//
//       // Begins object with brackets and player name
//       var playerObject = ''
//       playerObject += `{${player}:\n{\n`
//
//       // Appends player's stats to the object
//       for (var i = 0; i < playerStats.length; i++) {
//         if (i === playerStats.length - 1) { //if last
//           playerObject += `${playerStats[i]}\n `
//         }
//         else {
//           playerObject += `${playerStats[i]},\n `
//         }
//       }
//
//       //closes object
//       if (index === tableLength-1) { //if last
//         playerObject += `} \n } \n `
//       }
//       else {
//         playerObject += `} \n },`
//       }
//
//       console.log(playerObject);
//     // fs.appendFileSync(
//     //   '2016FedexCup.json',
//     //   `{}`
//     // );
//   });
});
