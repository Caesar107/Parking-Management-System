#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/6 15:33
# @Author  : zml
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os
DEBUG = True

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'dzj'
PASSWORD = 'Dzj1365878'
HOST = 'rm-2zes1gmjlcey26osclo.mysql.rds.aliyuncs.com'
PORT = '3306'
DATABASE = 'parking-system'
SECRET_KEY = os. environ. get( 'SECRET_ KEY') or 'you will never guess'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True