import investpy

df = investpy.get_stock_recent_data(stock='PEUP',country='france')
print(df)

search_results = investpy.search_etfs(by='isin', value='LU1681043599')

print(search_results)

df = investpy.get_etf_recent_data(etf='Amundi MSCI World UCITS',country='france')
print(df)

df = investpy.get_etf_historical_data(etf='Amundi MSCI World UCITS',country='france',from_date='01/12/2019',to_date='06/02/2020')
print(df)