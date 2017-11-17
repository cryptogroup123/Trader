from core.exchange import Exchange
from core.errors import ExchangeError

import json,calendar,datetime,requests


class bitstamp(Exchange):
	def describe(self):
		return self.deep_extend(super().describe(),{
			'id' : 'bitstamp',
			'urls' : {
				'api' : 'https://www.bitstamp.net/api/v2/',
				'api_doc' : 'https://www.bitstamp.net/api/'
			},
			'fees' : {
				'trading' : {
						'maker' : 0.025,
						'taker' : 0.025
				},
				'withdraw' : {
						'btc' : 0
				}
			},
			'api' : {
				'get' : {
					'ticker' : 'ticker/',
					'ticker_hourly' : 'ticker_hour/',
					'order_book' : 'order_book/',
					'transactions' : 'transactions/',
					'symbols_details' : 'trading-pairs-info'
				}
			}
			})

	def fetch_symbols(self):
		result = []
		url = self.urls['api'] + self.api['get']['symbols_details']
		response = self.loop_json(url)
		for sym in response:
			temp = sym['url_symbol']
			result.append(temp)
		return [x.upper() for x in result]


		"""
		request = requests.get(self.urls['api'] + self.api['get']['symbols_details'])
		print(request.status_code)
		response = request.json()
		for sym in response:
			temp = sym['url_symbol']
			result.append(temp)
		return [x.upper() for x in result
		"""



bitstamp = bitstamp()
print(bitstamp.symbols)
