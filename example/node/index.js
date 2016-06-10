var hypernova = require('hypernova/server');

hypernova({
  devMode: true,

  getComponent(name) {
    if (name === 'Component') {
      return require('./Component');
    }

    return null;
  },

  port: 3553,
});
