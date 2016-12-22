var express = require("express");
var elasticsearch = require('elasticsearch')
var app = express();
var client = elasticsearch.Client({
  host: 'localhost:9200'
})

app.listen(4000, () => {
  console.log("app listening on port 4000");
});

app.get("/:name", (req, res) => {
  client.search({
    index: req.params.name,
    type: 'stats',
    body: {
      size: 1000,
      query: {
        match_all: {}
        }
      }
  }).then(function (response) {
    res.json(response);
    // var hits = response.hits.hits
  }, function (error) {
    console.trace(error.message)
  })
});

app.get("/_cat/indices?v")
