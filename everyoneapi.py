#!/bin/python3

# Make sure we're using at least Python 3.0
import sys
if (sys.version_info.major < 3):
	print("Stop using Python 2! I only work with Python 3")
	exit(1)

import requests
import json

__version__ = '0.1.0'
__copyright__ = '(c) 2017 Corey Edwards. All Rights Reserved.'
__license__ = "BSD 3-Clause"


class EveryoneAPI:
	def __init__(self):
		self.sid = None # EveryoneAPI Account SID
		self.token = None # EveryoneAPI Account Token
		self.apiversion = '1' # EveryoneAPI API Version
		self.phone = None # Initialize Phone Variable
		self.results = None
		self.error = None

	def query(self, phone):
		# Query EveryoneAPI
		try:
			q=requests.get("https://api.everyoneapi.com/v" + self.apiversion + "/phone/+1" + phone, auth=(self.sid, self.token))

			status=str(q.status_code) # HTTP Status

			if ((status == "400") or (status == "404")):
				self.error = "Error: Phone number not found"
			elif ((status == "403") or (status == "401")):
				self.error = "Error: Permission denied. Did you pass your account credentials?"

			if (status == "200"):
				# Populate the results dict from JSON
				try:
					self.results = q.json() # Set data
				except KeyError:
					print("Response JSON was not properly populated even though EveryoneAPI responded with HTTP 200. Something is seriously wrong! The apocalypse is upon us!")

				return self.results['status']

		except requests.exceptions.ConnectionError:
			self.error = "Error: Unable to connect to EveryoneAPI"
			exit()
