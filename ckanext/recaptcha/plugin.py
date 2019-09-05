import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.recaptcha.helpers import get_helpers


class RecaptchaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'recaptcha')

    # ITemplateHelpers

    def get_helpers(self):
        return get_helpers()
