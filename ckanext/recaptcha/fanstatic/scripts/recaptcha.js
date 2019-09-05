ckan.module('recaptcha', function($, _) {
  'use strict';
  return {
    options: {
      version: 3,
      action: 'check',
      siteKey: null
    },
    initialize: function() {
      var self = this;
      window.grecaptcha.ready(function() {
        window.grecaptcha
          .execute(self.options.siteKey, { action: self.options.action })
          .then(self._onGetToken.bind(self));
      });
    },

    _onGetToken: function(token) {
      this.el.val(token);
    }
  };
});
