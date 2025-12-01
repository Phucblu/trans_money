import requests
import xmltodict

def get_usd_rate():
    url ="https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=10"
    response = requests.get(url)
    data_dict = xmltodict.parse(response.content)
    items = data_dict["ExrateList"]["Exrate"]

    for item in items:
        # currency = item["@CurrencyCode"]
        # seller = item["@Sell"]
        # print(f"{currency} - {seller}")
        if item["@CurrencyCode"] == "USD":
            # print(item["@Sell"])
            return item["@Sell"]
    return None