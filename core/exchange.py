"""
Generic exchange class
All info and methods for each exchange is done through this module
"""

import calendar
import datetime
import json
import time
import requests


class Exchange(object):
	id = None

	def __init__(self,config={}):
		settings = self.deep_extend(self.describe(),config)

		for key in settings:
			setattr(self,key,settings[key])

		self.symbols = []
		self.load_symbols()







	def describe(self):
		return {}

	def deep_extend(*args):
		result = None
		for arg in args:
			if isinstance(arg,dict):
				if not isinstance(result,dict):
					result = {}
				for key in arg:
					result[key] = Exchange.deep_extend(result[key] if key in result else None,arg[key])
			else:
				result = arg

		return result

	def load_symbols(self):
		symbols = self.fetch_symbols()
		for sym in symbols:
			if sym not in self.symbols:
				self.symbols.append(sym)

	def get_symbol_price(self,symbol):
		return self.fetch_symbol_price(symbol)
	



	#looping json request until we get a 200/successful response
	def loop_json(self,url):
		result = None
		print(url)
		while result == None:
			try:
				print('trying')
				response = requests.get(url)
				print(response)
				print(response.text)
				final = response.json()
				result = 1
			except:
				time.sleep(3)
				pass
		return final



















