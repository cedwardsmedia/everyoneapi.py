#!/bin/python3

'''
Copyright (c) 2017, Corey Edwards. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# Make sure we're using at least Python 3.0
import sys
if (sys.version_info.major < 3):
	print("Stop using Python 2! I only work with Python 3")
	exit(1)

import requests
import json

__version__ = '0.1.2'
__copyright__ = '(c) 2017 Corey Edwards. All Rights Reserved.'
__license__ = "BSD 3-Clause"


class EveryoneAPI:
	def __init__(self):
		self.sid = None # EveryoneAPI Account SID
		self.token = None # EveryoneAPI Account Token
		self.apiversion = '1' # EveryoneAPI API Version
		self.phone = None # Initialize Phone Variable
		self.datapoints = None
		self.results = None
		self.error = None

	def query(self, phone):

		self.datapoints = ",".join(str(dp) for dp in self.datapoints)
		# Query EveryoneAPI
		try:
			q=requests.get("https://api.everyoneapi.com/v" + self.apiversion + "/phone/+1" + phone + "?data=" + self.datapoints, auth=(self.sid, self.token))

			status=str(q.status_code) # HTTP Status

			if (status == "400"):
				self.error = "HTTP 400 Bad Request: Invalid phone number."
			elif (status == "401"):
				self.error = "HTTP 401 Unauthorized: Check API credentials."
			elif (status == "402"):
				self.error = "HTTP 402 Payment Required: Check EveryoneAPI account balance."
			elif (status == "403"):
				self.error = "HTTP 403 Forbidden: You've been rate-limited."
			elif (status == "404"):
				self.error = "HTTP 404 Not Found: Phone number not found in EveryoneAPI database."
			elif (status == "500"):
				self.error = "HTTP 500 Internal Server Error: EveryoneAPI is currently experiencing technical difficulties."
			elif (status == "503"):
				self.error = "HTTP 503 Service Unavailable: EveryoneAPI is currently experiencing service outages."

			if (status == "200"):
				# Populate the results dict from JSON
				try:
					self.results = q.json() # Set data
				except KeyError:
					print("Response JSON was not properly populated even though EveryoneAPI responded with HTTP 200. Something is seriously wrong! The apocalypse is upon us!")

				return self.results['status']

		except requests.exceptions.ConnectionError:
			self.error = "An unknown connection error has occurred."
			exit()
