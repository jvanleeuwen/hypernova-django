var React = require('react');
var renderReact = require('hypernova-react').renderReact;

function Component(props) {
  return React.createElement('div', {}, 'test');
}

module.exports = renderReact('Component.js', Component);
