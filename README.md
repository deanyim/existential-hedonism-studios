existential-hedonism-studios
============================

Getting Started
---------------

First, you'll want to install `virtualenvwrapper`. This is our dependency manager.

    venv/init.sh
    workon existential-hedonism-studios

Then, install Django (1.7c1):

    venv/install-django.sh


Troubleshooting
---------------

    Traceback (most recent call last):
      File "manage.py", line 8, in <module>
        from django.core.management import execute_from_command_line
    ImportError: No module named django.core.management

This means you should `workon existential-hedonism-studios`.
