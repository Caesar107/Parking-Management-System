#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:__init__.py.py
# author:ZML
# datetime:2022/4/30 14:10
# software: PyCharm

"""
this is function  description 
"""

from flask import Blueprint

history_bp = Blueprint('history', __name__)

from . import historyviews
