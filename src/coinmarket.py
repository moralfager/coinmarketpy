import math
import requests
from bs4 import BeautifulSoup
import json
import time


class CoinMarket:
    __DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    def __init__(self, header=__DEFAULT_HEADERS):
        self.header = header

    def url_to_txt(self, txt, count_for_unique_urls=0):
        f = open(txt, 'w')
        urls = self.get_url()
        for url in range(len(urls)):
            unique_urls = f"https://coinmarketcap.com{urls[url]}\n"
            f.write(unique_urls)
            count_for_unique_urls += 1
        print(f"[INFO] => {count_for_unique_urls} elements entered into a {txt} file ")

    def get_url(self, count=0, quantity=-1):
        urls = []
        unique_url = []
        if quantity == -1:
            for i in range(1, self.count_of_page() + 1):
                url = f'https://coinmarketcap.com/?page={i}'
                bsoup = BeautifulSoup(requests.get(url, headers=self.header).content, 'lxml')
                tbody = bsoup.find("tbody")
                all_tr = tbody.find_all("tr")
                for item in all_tr:
                    all_td = item.find_all("td")
                    for item1 in all_td:
                        all_links = item1.find_all('a', class_="cmc-link")
                        for item2 in all_links:
                            item_url = item2.get("href").replace("markets/", "").replace("?period=7d", "")
                            urls.append(item_url)
                            count += 1
                            print(f'{count} is done')
            urls = list(dict.fromkeys(urls))
        elif quantity >= 0:
            count_of_page = math.ceil(quantity / 100)
            print(count_of_page)
            for j in range(1, count_of_page + 1):
                url = f'https://coinmarketcap.com/?page={j}'
                bsoup = BeautifulSoup(requests.get(url, headers=self.header).content, 'lxml')
                tbody = bsoup.find("tbody")
                all_tr = tbody.find_all("tr")
                for item in all_tr:
                    all_td = item.find_all("td")
                    for item1 in all_td:
                        all_links = item1.find_all('a', class_="cmc-link")
                        for item2 in all_links:
                            item_url = item2.get("href").replace("markets/", "").replace("?period=7d", "")
                            urls.append(item_url)
                            count += 1
                            print(f'{count} is done')
            urls = list(dict.fromkeys(urls))
            pop_count = 100 - (quantity % 100)
            print(pop_count)
            for i in range(pop_count):
                urls.pop()
        count_for_unique_urls = 0
        for url in range(len(urls)):
            temp = f"https://coinmarketcap.com{urls[url]}"
            unique_url.append(temp)
            count_for_unique_urls += 1
        print(f"[INFO] => {count_for_unique_urls} elements")
        return unique_url

    def count_of_page(self):
        page = self.find_count_of_crypto() / 100
        return math.ceil(page)

    def find_count_of_crypto(self):
        url = f'https://coinmarketcap.com/'
        soup = BeautifulSoup(requests.get(url, headers=self.header).content, 'lxml')
        div = soup.find('div', class_="sc-16r8icm-0 sc-4r7b5t-0 gJbsQH")
        showing = div.find('p', class_="sc-1eb5slv-0 hykWbK")
        return int(showing.text[-4:])

    def print_info(self, url, count, data, retry=10):
        currency = {'Cryptocurrencies': []}
        for i in range(1):
            try:
                response = requests.get(url=url, headers=self.header)
                result = response.content
                soup = BeautifulSoup(result, 'lxml')
                price_value = soup.find(class_="priceValue")
                name = soup.find("span", class_="sc-1eb5slv-0 sc-1308828-0 bwAAhr")
                # name_symbol = soup.find(class_="nameSymbol")
                stats = soup.find_all(class_="statsValue")
                # usd_converter = soup.find_all(class_="sc-16r8icm-0 sc-1etv19d-4 iQGGZq")

                # 0 - marcap 1 - full marcap 2 - volume24 3- volume/marcap 4 - circulating Supply
                currency['Cryptocurrencies'].append({
                    'ID': count,
                    'Name': name.text,
                    'Price': price_value.text,
                    'Market Capitalization': stats[0].text,
                    'Fully Diluted Market Cap': stats[1].text,
                    'Volume 24h': stats[2].text,
                    'Volume/Marcap': stats[3].text,
                    'Circulating Supply': stats[4].text
                })
                data.append(currency)
                print(currency)
                print(f'{count} {name.text} is [DONE]')
            except Exception as ex:
                time.sleep(15)
                if retry:
                    print(f"[INFO] retry = {retry} =>{url}")
                    return self.print_info(url, count, retry=(retry - 1), data=data)
                else:
                    currency['Cryptocurrencies'].append({
                        'ID': count,
                        'Name': None,
                        'Price': None,
                        'Market Capitalization': None,
                        'Fully Diluted Market Cap': None,
                        'Volume 24h': None,
                        'Volume/Marcap': None,
                        'Circulating Supply': None
                    })
                    data.append(currency)
                    print(currency)
                    continue
            else:
                return response
        return data

    def info_to_json(self, url, count, retry=15):
        currency = {'Cryptocurrencies': []}
        for i in range(1):
            try:
                response = requests.get(url=url, headers=self.header)
                result = response.content
                soup = BeautifulSoup(result, 'lxml')
                price_value = soup.find(class_="priceValue")
                name = soup.find("span", class_="sc-1eb5slv-0 sc-1308828-0 bwAAhr")
                # name_symbol = soup.find(class_="nameSymbol")
                stats = soup.find_all(class_="statsValue")
                # usd_converter = soup.find_all(class_="sc-16r8icm-0 sc-1etv19d-4 iQGGZq")

                # 0 - marcap 1 - full marcap 2 - volume24 3- volume/marcap 4 - circulating Supply
                currency['Cryptocurrencies'].append({
                    'ID': count,
                    'Name': name.text,
                    'Price': price_value.text,
                    'Market Capitalization': stats[0].text,
                    'Fully Diluted Market Cap': stats[1].text,
                    'Volume 24h': stats[2].text,
                    'Volume/Marcap': stats[3].text,
                    'Circulating Supply': stats[4].text
                })
                print(f'{count} {name.text} is [DONE]')
                with open('CoinMarket.json', 'w') as file:
                    json.dump(currency, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                time.sleep(15)
                if retry:
                    print(f"[INFO] retry = {retry} =>{url}")
                    return self.info_to_json(url, count, retry=(retry - 1))
                else:
                    currency['Cryptocurrencies'].append({
                        'ID': count,
                        'Name': None,
                        'Price': None,
                        'Market Capitalization': None,
                        'Fully Diluted Market Cap': None,
                        'Volume 24h': None,
                        'Volume/Marcap': None,
                        'Circulating Supply': None

                    })
                    with open('CoinMarket.json', 'w') as file:
                        json.dump(currency, file, indent=4, ensure_ascii=False)
                    f = open('ex_log.txt', 'w')
                    f.write(f"{count} {url}\n")
                    continue
            else:
                return response

    def get_top(self, quantity):
        data = []
        all_information = self.get_url(quantity=quantity)
        count = 1
        for all_info in all_information:
            self.print_info(url=all_info, count=count, data=data)
            count += 1

    def get_all_info(self):
        data = []
        all_information = self.get_url()
        count = 1
        for all_info in all_information:
            self.print_info(url=all_info, count=count, data=data)
            count += 1
        print(data)

    def get_news(self, coin_name):
        result_list = []
        while True:
            total_count = self.find_count_of_crypto()
            responce = requests.get(url=f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1'
                                        f'&limit={total_count}&sortBy=market_cap&'
                                        f'sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false')
            data = responce.json()
            for i in range(0, total_count):
                result_list.append({
                    'id': data['data']['cryptoCurrencyList'][i]['id'],
                    'name': data['data']['cryptoCurrencyList'][i]['name']
                })
            print(result_list)
            for i in range(0, total_count):
                if 'name' == 'Bitcoin' in result_list:
                    print(result_list.get('id'))
            for i in range(len(result_list)):
                if result_list[i]['name'] == coin_name.lower().title():
                    coin_id = result_list[i]['id']
            urls = f'https://api.coinmarketcap.com/content/v3/news?coins={coin_id}'
            res = requests.get(url=urls)
            data_news = res.json()
            data_news_json = []
            for i in range(0, len(data_news['data'])):
                data_news_json.append({
                    'News title': data_news['data'][i]['meta']['title'],
                    'Text': data_news['data'][i]['meta']['subtitle']
                })
            return data_news_json
