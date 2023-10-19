from django.urls import re_path
from surlex import Surlex

def surl(surlex, *args, **kwargs):
    return url(Surlex(surlex).translate(), *args, **kwargs)
