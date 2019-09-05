import requests

import ckan.plugins.toolkit as toolkit


def get_helpers():
    return {
        'recaptcha_site_key': recaptcha_site_key,
        'recaptcha_verify': recaptcha_verify
    }


def recaptcha_site_key():
    return toolkit.config['ckanext.recaptcha.site_key']


def recaptcha_verify(token, action=None, min_score=0):
    secret = toolkit.config['ckanext.recaptcha.secret_key']

    payload = {'secret': secret, 'response': token}
    data = requests.post(
        'https://www.google.com/recaptcha/api/siteverify', payload
    ).json()

    if not data['success']:
        return False

    if action and data['action'] != action:
        return False
    if data['score'] < min_score:
        return False

    return True
