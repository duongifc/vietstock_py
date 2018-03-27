import requests
import json
import codecs
from src import vietstock_constants as Constants


page = requests.get(Constants.API_EXCHANGE_LIST)
json_obj = json.loads(page.text)

with codecs.open('../files/companies.json', 'w', encoding='utf-8-sig') as f:
    json.dump(json_obj['rows'], f, indent=4, sort_keys=True)