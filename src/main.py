import json
import codecs
from src import vietstock_constants as Constants
from src import excel

hose_vnm_params = {
    'exchange_name': Constants.EXCHANGE_HOSE,
    'company_code': 'VNM',
    'from_date': '02/26/18',
    'to_date': '03/26/18',
    'table_title': 'Finance_Table_Title',
    'table_content': 'MatchingHoseResult'
}
# excel.export(hose_vnm_params)

#####################################################################

with open('files/companies.json', encoding="utf-8-sig") as f:
    companies = json.load(f)

for item in companies:
    code = item['cell'][1]
    excel.export({
        'exchange_name': Constants.EXCHANGE_HOSE,
        'company_code': code,
        'from_date': '02/26/18',
        'to_date': '03/26/18',
        'table_title': 'Finance_Table_Title',
        'table_content': 'MatchingHoseResult'
    })