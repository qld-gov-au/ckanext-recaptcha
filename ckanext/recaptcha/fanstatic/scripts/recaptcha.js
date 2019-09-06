ckan.module('recaptcha', function($, _) {
  'use strict';
  return {
    options: {
      version: 3,
      action: 'check',
      siteKey: null
    },
    initialize: function() {

      ckan.pubsub.subscribe('recaptcha:regenerate-token', this._generateToken.bind(this));
    },

    _onGetToken: function(token) {
      this.el.val(token);
    },
    _generateToken: function(cb) {
      var self = this;
      window.grecaptcha.ready(function() {
        window.grecaptcha
          .execute(self.options.siteKey, { action: self.options.action })
          .then(self._onGetToken.bind(self))
          .then(function() {
            if (cb) {
              return cb();
            }
            return null;
          });
      });
    }
  };
});
