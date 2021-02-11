from pprint import pprint
from nsetools import Nse
nse = Nse()


q = nse.get_quote('PIIND')
pprint(q)
# all_stock_codes = nse.get_stock_codes()
# pprint(all_stock_codes)
# top_gainers = nse.get_top_gainers()
# pprint(top_gainers)