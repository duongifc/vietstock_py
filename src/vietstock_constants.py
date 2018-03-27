from urllib.parse import urlencode, quote_plus

API_BASE_URL = 'http://finance.vietstock.vn/Controls/'
API_TRADE_RESULT = 'TradingResult'
API_EXCHANGE_LIST = 'https://www.hsx.vn/Modules/Listed/Web/SymbolList?pageFieldName1=Code&pageFieldValue1=&pageFieldOperator1=eq&pageFieldName2=Sectors&pageFieldValue2=&pageFieldOperator2=&pageFieldName3=Sector&pageFieldValue3=00000000-0000-0000-0000-000000000000&pageFieldOperator3=&pageFieldName4=StartWith&pageFieldValue4=&pageFieldOperator4=&pageCriteriaLength=4&_search=false&nd=1522075856901&rows=9999999&page=1&sidx=id&sord=desc'

EXCHANGE_HOSE = 'Hose'
EXCHANGE_HNX = 'HNX'
EXCHANGE_UPCOM = 'UPCOM'


def get_trading_url(exchange_name, scode, from_date, to_date):
    params = {
        'scode': scode,
        'lcol': 'TKLGD,TGTGD,VHTT,GD3,TGG,TGPTG,BQM,BQB,KLGDKL,GTGDKL,',
        'sort': 'Time',
        'dir': 'desc',
        'page': 1,
        'psize': 0,
        'fdate': from_date,
        'tdate': to_date,
        'exp': 'excel'

    }
    return (API_BASE_URL + API_TRADE_RESULT + '/' +
            'Matching_' + exchange_name + '_Result.aspx?' +
            urlencode(params, quote_via=quote_plus))


