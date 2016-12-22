var elasticsearch = require('elasticsearch')
var client = elasticsearch.Client({
  host: 'localhost:9200'
})

client.search({
  index: 'official_money',
  type: 'stats',
  body: {
    query: {
      match_all: {}
      }
    }
}).then(function (response) {
  console.log(response);
  var hits = response.hits.hits
}, function (error) {
  console.trace(error.message)
})
