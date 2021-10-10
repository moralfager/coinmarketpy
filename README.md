# CoinMarket scrapper



### Installation
```bash
git clone https://github.com/moralfager/coinmarketpy.git
cd src
python3 setup.py install
```

### Usage

```python
from coinmarketpy import CoinMarket
cm = CoinMarket()
```

### Examples
Usage examples:
```python
# getting all url, if quantity not provided
>>> cm.get_url(quantity=1)
['https://coinmarketcap.com/currencies/bitcoin/']
>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
# News about crypto
>>> cm.get_news('Bitcoin')
[{'News title': 'US Senator Reveals That She Had Stacked Up $100K Worth Of BTC In August', 'Text': 'Senator Cynthia Lummis revealed through a filing that she had purchased bitcoin in August. The value of her BTC purchase is worth between $50K to $100K. Senator Lummis is one of the pro-crypto members of the senate, notably saying that she would like bitcoin to form “part of a di...'}, {'News title': 'Voting period for Mt. Gox civil rehabilitation plan finally ends', 'Text': 'Tokyo-based crypto exchange Mt. Gox shut down in 2014 after it lost Bitcoin (BTC) worth $450 million at the time...  Continue reading  \n'}]
# Printing all information about currencies
>>> cm.get_all_info()
# List of top by market cap
>>> cm.get_top(quantity=1)
{'Cryptocurrencies': [{'ID': 1, 'Name': 'Bitcoin', 'Price': '$55,366.58', 'Market Capitalization': '$1,043,102,852,155', 'Fully Diluted Market Cap': '$1,162,698,149,960', 'Volume 24h': '$35,633,816,402', 'Volume/Marcap': '0.03416', 'Circulating Supply': '18,839,937.00 BTC'}]}

```

### API documentation
https://coinmarketcap.com/api/

## License
[MIT](https://choosealicense.com/licenses/mit/)
