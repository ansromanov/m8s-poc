var express = require('express')
var app = express();
var port = process.env.PORT || 4200;

var routes = require('./api/routes');
routes(app);
app.listen(port, function() {
   console.log('Server started on port: ' + port);
});