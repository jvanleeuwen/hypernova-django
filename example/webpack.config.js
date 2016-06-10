var path = require('path');
var webpack = require('webpack');

module.exports = {

  entry: './client/entry.js',

  output: {
    path: path.resolve(__dirname, 'render', 'static', 'render', 'js'),
    publicPath: '/static',
    filename: 'bundle.js'
  },

  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
        exclude: /node_modules/,
      }
    ]
  }

};
