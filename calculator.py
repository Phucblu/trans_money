import api_bank as api

def amount_USD(number_VND):
    rate_USD = api.get_usd_rate()
    rate_usd_clear = rate_USD.replace(",", "")
    rate_usd_float = float(rate_usd_clear)
    total = rate_usd_float * number_VND
    return total
