from core.exchange import Exchange
import json,calendar,datetime,requests




class binance(Exchange):
	def describe(self):
		return self.deep_extend(super().describe(),{
			'id' : 'binance',
			'urls' : {
				'api' : 'https://www.binance.com/api/v1/',
				'api_doc' : 'https://www.binance.com/restapipub.html'
			},
			'fees' : {
				'trading' : {
						'maker' : 0.001,
						'taker' : 0.001
				},
				'withdraw' : {
						'btc' : 0.0005,
						'eth' : 0.005,
						'ltc' : 0.001,
						'bch' : 0.0005,
						'IOTA' : 0
				}
			},
			'api' : {
				'order_book' : 'depth?symbol=',
				'ticker_24hr' : 'ticker/24hr?symbol=',
				'all_prices' : 'ticker/allPrices',
				'all_book_tickers' : 'ticker/allBookTickers'
			}
			})

	def fetch_symbols(self):
		result = []
		response = requests.get(self.urls['api']+self.api['all_prices']).json()
		for d in response:
			result.append(d['symbol'])
		return result

	def fetch_symbol_price(self,symbol):
		prices = {}
		response = requests.get(self.urls['api']+self.api['ticker_24hr']+symbol).json()
		prices['last_price'] = response['lastPrice']
		prices['bid_price'] = response['bidPrice']
		prices['ask_price'] = response['askPrice']
		return prices




#Query Methods

binance = binance()
#print(binance.symbols)
#print(requests.get(binance.urls['api']+binance.api['order_book']+'ETHBTC').json())
#print(requests.get(binance.urls['api']+binance.api['all_book_tickers']).json())
print(binance.get_symbol_price('ETHBTC'))

