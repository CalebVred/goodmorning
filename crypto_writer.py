'''
Returns a string giving cryptocurrency stats from the last 24 hours
'''
from pycoingecko import CoinGeckoAPI


def crypto_stat_string(coin_list, vsc):
    c_stat_str = ""
    cg = CoinGeckoAPI()

    for coin in coin_list:
        print("Appending stats for", coin)
        c_stat_str += coin
        c_stat_str += " is priced at "
        cgdatac = cg.get_price(ids=coin, vs_currencies=vsc)
        cid = cgdatac[coin]
        price = cid[vsc]
        c_stat_str += str(price)
        c_stat_str += '.'

    return c_stat_str
