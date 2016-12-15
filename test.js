/* I want to be able to return the value, an array from line 24 to options (or anything else I don't care) and use this value to be the return value for the getYears function */

var url = 'http://www.pgatour.com/stats/stat.02671.html'
var years = [] // <<< I want to be able to run the getYears function and access this data upon its completion

function getYears(url) {

  // This block grabs the url and leverages it to scrape data with cheerio
  var options = {
    uri: url,
    transform: function (body) {
      return cheerio.load(body);
    }
  };

//Used the request-promise library (https://github.com/request/request-promise) on James' recommendation, this is where the result of cheerio is outputted to
  let request = rp(options)
  .then(function ($) {
    //This selects the data I want from the page that I have scraped
    $('#yearSelector > option').each(function( index ) {
      var year = $(this).val().trim();
      years.push(year)
    })
    console.log(years);
    //!!!!!! What is not working. I want to return years, but I can't seem to do it. I have tried .return, .bind, but I can't seem to understand how to use them or get them working. How do I return something out of this promise and use it?
    return years // <<<< Does not work.....
  })
  .catch(function (err) {
    console.log('whooops');
  });
