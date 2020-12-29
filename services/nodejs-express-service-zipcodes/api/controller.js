'use strict';

const fs = require("fs");


var properties = require('../package.json')
var distance = require('../service/distance');

var controllers = {
  index: function (req, res) {
    fs.readFile("views/index.html", "utf8", (err, html) => {
      if (err) throw err;
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(html);
    });
  },
  about: function (req, res) {
    var aboutInfo = {
      name: properties.name,
      version: properties.version
    }
    res.json(aboutInfo);
  },
  get_distance: function (req, res) {
    distance.find(req, res, function (err, dist) {
      if (err)
        res.send(err);
      res.json(dist);
    });
  },
};

module.exports = controllers;