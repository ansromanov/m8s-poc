'use strict'

var controller = require('./controller')

module.exports = function(app) {
  app.route('/')
    .get(controller.index);
  app.route('/about')
    .get(controller.about);
  app.route('/api/distance/:zipcode1/:zipcode2')
    .get(controller.get_distance);
}