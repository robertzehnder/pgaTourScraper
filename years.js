var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');
var rp = require('request-promise');
let http = require('http')
let axios = require('axios')
// var $ = require('jQuery');
var url = 'http://www.pgatour.com/stats/stat.02671.html'
var years = []
fakearray = []

// function getYears() {
//   let request = rp(url)
//   return request
// }
//
function getYears() {
  let arg = axios.get(url)
  return arg
}

getYears().then((response) => {
  // console.log(response);
  module.exports = response
})

//
// getYears().then((response) => {
//   var $ = cheerio.load(response)
//   $('#yearSelector > option').each(function( index ) {
//     console.log('hits');
//     var year = $(this).val().trim();
//     years.push(year)
//   })
// })
//


// x = kickStarter(url)
// console.log(x);
//
// getYears(url).then((respsonse) => {
//   console.log(response);
// })
//
// function kickStarter(startUrl) {
//   // hopefullyYearsArray = getYears(startUrl)
//   // console.log(hopefullyYearsArray);
//   return hopefullyYearsArray
// }
//
//  function newarray(array) {
//   console.log(array);
// }
//
// function getYears(url) {
//   var options = {
//     uri: url,
//     transform: function (body) {
//       return cheerio.load(body);
//     }
//   };
//
//   let request = rp(options)
//   .then(function ($) {
//     // Process html like you would with jQuery...
//     $('#yearSelector > option').each(function( index ) {
//       var year = $(this).val().trim();
//       years.push(year)
//     })
//     return years
//   })
//   .catch(function (err) {
//     // Crawling failed or Cheerio choked...
//     console.log('whooops');
//   });
//   console.log(request);
//   return request
//
// }
//





// request(url, function(error, response, body) {
//   // if(error) {
//   //   console.log("Error: " + error);
//   // }
//   // console.log("Status code: " + response.statusCode);
//   // else {
//   //
//   // }
//   var $ = cheerio.load(body);
// // console.log(body);
//   $('#yearSelector > option').each(function( index ) {
//     var year = $(this).val().trim();
//     years.push(year)
//   });
//   console.log(years);
//
// });
// console.log(`Hi ${years}`);




//
// function(link, callback){
//   request(link, function(err, im, body){
//     callback(err, body);
//   });
// });






//
// var url = 'http://www.pgatour.com/stats/stat.02671.html'
//
//
// request(url, function(error, response, body) {
//   if(error) {
//     console.log("Error: " + error);
//   }
//   console.log("Status code: " + response.statusCode);
//
//   var $ = cheerio.load(body);
// // console.log(body);
//   var years = []
//   $('#yearSelector > option').each(function( index ) {
//     var year = $(this).val().trim();
//     years.push(year)
//   });
//
// });
//
// firstPlayer = $('#statsTable > tbody > tr').first().text()
// console.log(firstPlayer);
//
// $('tbody > tr').each(function( index ) {
//
//   //get player name for instance
//   var player = $(this).find('.player-name').text().trim()
//
//   //array to hold stats for player instance
//   var playerStats = []
//
//   //get all the stats for the player instance
//   $(this).find('td').each (function(index) {
//     var playerValue = `${headers[index]}: ${$(this).text().trim()}`
//     playerStats.push(playerValue) //inject into array
//   });
//
//   // Builds JSON object for each player
//
//     // Begins object with brackets and player name
//     var playerObject = ''
//     playerObject += `{${player}:\n{\n`
//
//     // Appends player's stats to the object
//     for (var i = 0; i < playerStats.length; i++) {
//       if (i === playerStats.length - 1) { //if last
//         playerObject += `${playerStats[i]}\n `
//       }
//       else {
//         playerObject += `${playerStats[i]},\n `
//       }
//     }
//
//     //closes object
//     if (index === tableLength-1) { //if last
//       playerObject += `} \n } \n `
//     }
//     else {
//       playerObject += `} \n },`
//     }
//
//     console.log(playerObject);
