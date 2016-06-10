var hypernova = require('hypernova/server');

hypernova({
  devMode: true,

  getComponent(name) {
    if (name === 'Component') {
      return require('./lib/Component');
    }

    return null;
  },

  port: 3553,
});
