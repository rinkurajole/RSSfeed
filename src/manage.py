#!/usr/bin/env python

"""
A thin wrapper around ```django-admin```.
It takes care of several things for us before delegating to ```django-admin```.

For more information on this file, see
https://docs.djangoproject.com/en/stable/ref/django-admin/
"""


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
