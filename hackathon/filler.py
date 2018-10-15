from __future__ import print_function
import os
import requests
import re
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
#Authored by Nathaniel Chong, Brandon Morrell, Stephen Welch, and Justin Williams: c/o BigParser Summer 2017.

SHEET_NAME = 'Common_Crypto_Currencies'
WORKSHEET_TITLE = 'crypto_currencies'

CRYPTO_API_URL = 'https://api.coinmarketcap.com/v1/ticker/{0}/'

RANK_COL = 'H'
PRICE_USD = 'I'
PRICE_BTC = 'J'
DAY_VOL = 'K'
MKT_CAP = 'L'
AVAIL_SUPPLY = 'M'
TOTAL_SUPPLY = 'N'
PERCENT_CHANGE_HOUR = 'O'
PERCENT_CHANGE_DAY = 'P'
PERCENT_CHANGE_WEEK = 'Q'
UPDATE_TIMESTAMP = 'R'
colTypes = [RANK_COL, PRICE_USD, PRICE_BTC, DAY_VOL, MKT_CAP, AVAIL_SUPPLY, TOTAL_SUPPLY, PERCENT_CHANGE_HOUR, PERCENT_CHANGE_DAY, PERCENT_CHANGE_WEEK, UPDATE_TIMESTAMP]
infoTypes = ['rank', 'price_usd', 'price_btc', '24h_volume_usd', 'market_cap_usd', 'available_supply', 'total_supply', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated']

def main():
	
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
	 
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_TITLE)
	
	currencyNames = sheet.col_values(1)
	currencyNames = ' '.join(currencyNames).split()
			
	print(currencyNames)
	
	for i in range(1, len(currencyNames)):
		# Get currency name
		name = str.lower(currencyNames[i])
		# Grab info for currency
		requests.encoding = 'utf-8'
		currency = requests.get(CRYPTO_API_URL.format(name)).json()
		print('Grabbing data for {0}'.format(currencyNames[i]))
		try:
			if(len(currency) > 0):
				currency = currency[0]
				print(currency)
				for x in range(0, len(colTypes)):
					sheet.update_cell(i + 1, (ord(colTypes[x]) % 65) + 2, currency[infoTypes[x]])
				
			
			print('Success for {0}!'.format(currencyNames[i]))
		except KeyError:
			print('Skipping {0}'.format(currencyNames[i]))
		except gspread.exceptions.RequestError:
			print('Lost server lock. Restarting operations.')
			main()
			
			
if __name__ == '__main__':
    main()
