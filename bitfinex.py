from core.exchange import Exchange
from core.errors import ExchangeError

import json,calendar,datetime,requests



#url links
api_v1 = 'https://api.bitfinex.com/v1/'

class bitstamp(Exchange):
	def describe(self):
		return self.deep_extend(super().describe(),{
			'id' : 'bitstamp',
			'urls' : {
				'api' : 'https://api.bitfinex.com/v1/',
				'api_doc' : 'https://docs.bitfinex.com/docs'
			},
			'fees' : {
				'trading' : {
						'maker' : 0.01,
						'taker' : 0.02
				},
				'withdraw' : {
						'btc' : 0.0005,
						'eth' : 0.01,
						'ltc' : 0.001,
						'bch' : 0.0005,
						'IOTA' : 0
				},
				'lending' : {
						'open' : 0.15,
						'hidden' : 0.18
				}
			},
			'api' : {
				'get' : {                                                                                     
						'ticker' : 'pubticker/',
						'volume' : 'stats/',
						'order_book' : 'book/',
						'recent_trade' : 'trades',
						'symbols' : 'symbols',
						'symbols_details' : 'symbols_details'
					}
			}
			})

bitstamp = bitstamp()
print (bitstamp.api['get'])
