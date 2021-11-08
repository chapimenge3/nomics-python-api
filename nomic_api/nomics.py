#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Temkin Mengistu
@Linken: https://www.linkedin.com/in/chapi-menge/
@Telegram: https://t.me/chapimenge

This Wrapper is Targeted for interacting Nomics Cryptocurrency & Bitcoin API. Feel free to add your own custom methods. 
For more information, please visit: https://nomics.com/docs/

"""

import requests


class Nomics:
    '''
    Main Class for Nomics Rest API. 
    '''

    def __init__(self, key, base_url="https://api.nomics.com/v1/", ):
        '''
        Constructor for Nomics Class. you can find free api key in https://p.nomics.com/cryptocurrency-bitcoin-api .
        '''
        if key is None:
            raise Exception("Please provide a valid API key.")
        self.key = key
        self.base_url = base_url

    def request(self, endpoint, params):
        """The basic request that all API calls use
        the parameters are joined in the actual api methods so the parameter
        strings can be passed and merged. 

        Args:
            params ([dict]): additional parameters 
        """

        if params is None:
            params = {}
        params["key"] = self.key
        r = requests.get(self.base_url + endpoint, params=params)

        if r.status_code != 200:
            return r.text

        if "format" in params and params["format"] == "csv":
            return r.text

        return r.json()

    # Currencies
    def currencies_ticker(self, params=None):
        '''
        Currencies Ticker:

            Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 
            7 day, 30 day, 365 day, and year to date intervals. Current prices are updated 
            every 10 seconds.

            Endpoint: 
                https://api.nomics.com/v1/currencies/ticker

        Args:
            params ([dict]): query Parameters

        Returns:
            dict: Json data will be returned

        '''

        return self.request("currencies/ticker", params=params)

    def currencies_metadata(self, params=None):
        """
        The currencies endpoint returns all the currencies and their metadata that Nomics supports.

        Args:
            params (dict): query Parameters

        Returns:
            dict: Json data will be returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv

        """
        return self.request("currencies", params=params)

    # Markets
    def market(self, params=None):
        """
        The markets endpoint returns information on the exchanges and markets that Nomics supports,
        in addition to the Nomics currency identifiers for the base and quote currency.


        Args:
            params (dict): query Parameters

        Returns:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            

        """
        return self.request("market", params=params)

    def market_cap_history(self, params=None):
        """
        MarketCap History is the total market cap for all cryptoassets at intervals between the requested time period.

        Args:
            params (dict): query Parameters

        Returns:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """

        return self.request("market-cap/history", params=params)
    
    # Volume
    def volume_history(self, params=None):
        """
        Volume History is the total volume for all cryptoassets in USD
        at intervals between the requested time period. For each entry, 
        the volume field represents the sum of the spot_volume and derivative_volume fields.


        Args:
            params ([type]): [description]
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("volume/history", params=params)
    
    # Exchange Rates
    def exchange_rates(self, params=None):
        """
        The exchange rates endpoint returns the current exchange rates used
        by Nomics to convert prices from markets into USD. This contains Fiat
        currencies as well as a BTC and ETH quote prices. This endpoint helps 
        normalize data across markets as well as to provide localization for users.

        Currently, this endpoint does not support historical data, but this feature is planned.
        
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        
        """
        return self.request("exchange-rates", params=params)
    
    def exchange_rates_history(self, params=None):
        """
        Exchange rates for every point in a time range. This endpoint can be used 
        with other history endpoints to convert values into a desired quote currency.

        The currency parameter must be a Nomics Quote Currency, to get all Nomics 
        Quote Currencies, use the /exchange-rates endpoint for all current rates.
        
        Args:
            params (dict): query parameter
                        : currency and start required 
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        
        return self.request("exchange-rates/history", params=params)
    
    # The below methods are only available to customers of our paid API plans. Please 
    # https://p.nomics.com/pricing/ to learn more about our pricing plans.
    
    # Global*
    def global_ticker(self, params=None):
        """
        Globally-aggregated market cap and volume data over various intervals
        across all currencies.

        The total volume fields are computed by summing the spot_volume and 
        derivative_volume fields at each interval.

        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        
        return self.request("global-ticker", params=params)
    
    # Currencies*
    def currency_highlights(self, params=None):
        """
        The currency highlights endpoint returns various aggregate statistics for a currency over some interval.


        Args:
            params (dict): query parameter
                         : currency is required parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("currencies/highlights", params=params)
    
    def supply_history(self, params=None):
        """
        Supply history per currency for every day in a time range.
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("supplies/history", params=params)
    
    # Exchanges
    def exchange_hghlights(self, params=None):
        """
        The exchange highlights endpoint returns various aggregate statistics for an exchange over some interval.
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("exchanges/highlights", params=params)
    
    def exchanges_ticker(self, params=None):
        """
        The Exchanges Ticker provides high level information about the exchanges integrated with Nomics. 
        It provides a limited amount of metadata, the type of integration, the time range of available data,
        pairs, and interval information about the volume and, where applicable, the number of trades.
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("exchanges/ticker", params=params)
    
    def exchanges_volume_history(self, params=None):
        """
        Exchange Volume History is the total volume for all cryptoassets of an exchange in USD at 
        intervals between the requested time period. For each entry, the volume field represents 
        the sum of the spot_volume and derivative_volume fields.
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("exchanges/volume/history", params=params)
    
    def exchanges_metadata(self, params=None):
        """
        The exchanges endpoint returns all the exchanges and their metadata that Nomics supports.


        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("exchanges", params=params)
    
    # Markets
    def market_highlights(self, params=None):
        """
        The market highlights endpoint returns various aggregate statistics for a pair over some interval.
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """ 
        return self.request("exchange-markets/highlights", params=params)
    
    def exchange_markets_ticker(self, params=None):
        """
        The Exchange Markets Ticker provides high level information about individual markets on exchanges integrated with Nomics.
        It provides metadata, the type of market, aggregation information, current financial data, and financial data over preset intervals.

        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        """
        return self.request("exchange-markets/ticker", params=params)
    
    # Candles
    def candles(self, params=None):
        """
        The candles endpoint returns aggregated open, high, low, close, and volume information for Nomics currencies. 
        When asking for candles, a currency is provided as a parameter. Nomics aggregates all markets where the given 
        currency is the base currency and the quote currency is a fiat currency, BTC, or ETH and returns all values in USD.

        Candles are aggregated across all markets for the base currencies, which necessitates converting to a common quote currency. 
        Nomics converts all markets into USD in order to aggregated candles.

        Candles have the following time range limits based on interval and time:

            1d: Available from inception with no range limit
            1h: Available from inception. Time range limits:
                Past 30 days: accessible in a single request
                Older than 30 days: 1 day at a time

        CSV format is: timestamp,open,high,low,close,volume,empty,transparent_open,transparent_high,transparent_low,transparent_close,
        transparent_volume
        
        Args:
            params (dict): query parameter
        
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        
        """
        return self.request("candles", params=params)
    
    def exchange_candles(self, params=None):
        """
        The exchange candles endpoint returns raw open, close, high, low, and volume information for Nomics Markets. 
        The data is not aggregated, therefore prices are in the quote currency of the market and volume is in the base currency of the market.
        
        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        
        """
        return self.request("exchange-candles", params=params)
    
    def markets_candles(self, params=None):
        """
        The Aggregated Pair Candles endpoint returns aggregated open, close, high, low, and volume information for an Aggregated
        Pair of base and quote currencies. Open and Close are volume weighted averages across markets, while High and Low are the 
        max and min prices across markets. Volume is the total volume.

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
        
        """
        return self.request("markets/candles", params=params)
    
    # Trades
    def trades(self, params=None):
        """
        The trades endpoint returns individual trades in a normalized format for an individual exchange market.

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("trades", params=params)

    # Orders
    def orders_snapshot(self, params=None):
        """
        The most recent order book snapshot for the given exchange and market. 
        An empty result is returned if no snapshot is found within 24 hours prior to the provided timestamp.

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("orders/snapshot", params=params)

    def orders_batches(self, params=None):
        """
        This endpoint returns daily batches of order book snapshots as Zip archived CSV files. 
        Batches are available up to 2 days prior to the current date, inclusive.

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("orders/batches", params=params)
    
    # Predictions
    def currencies_predictions_ticker(self, params=None):
        """
        The Currencies Predictions Ticker endpoint returns the current price prediction for all currencies

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("currencies/predictions/ticker", params=params)
    
    def currencies_predictions_history(self, params=None):
        """
        The Currencies Predictions History endpoint returns historical price prediction for one currency

        Args:
            params (dict): query parameter
    
        Return:
            dict: Json data will returned if the format is passed as json
            str: CSV text data will be returned if the format is passed as csv
            
        """
        return self.request("currencies/predictions/history", params=params)
