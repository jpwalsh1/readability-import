#!/usr/bin/python

import readability
from datetime import date, timedelta
from sqlalchemy import *

'''		readability config		''' 
token = readability.xauth('read_username', 'read_apikey', 'read_email', 'read_pass')
rdd = readability.oauth('read_username', 'read_apikey', token=token)

'''		sqlalchemy setup		'''
engine = create_engine('mysql://db_username:db_passwd@db_host/db')
connection = engine.connect()


'''		Fetch new bookmarks since yesterday		'''
yesterday = date.today() - timedelta(1)

for b in rdd.get_bookmarks(added_since=yesterday.strftime('%m-%d-%y')):	
	result = connection.execute("INSERT INTO bookmarks VALUES(NULL, " + str(b.id) + ", '" + b.article.title.encode("utf-8") + "', '" + b.article.url.encode("utf-8") + "')" )

