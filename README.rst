============
ckanext-recaptcha
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-recaptcha:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-recaptcha Python package into your virtual environment::

     pip install ckanext-recaptcha

3. Add ``recaptcha`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    ckanext.recaptcha.site_key = SITE_KEY
    ckanext.recaptcha.secret_key = SECRET_KEY


------------------------
Development Installation
------------------------

To install ckanext-recaptcha for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/DataShades/ckanext-recaptcha.git
    cd ckanext-recaptcha
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.recaptcha --cover-inclusive --cover-erase --cover-tests

