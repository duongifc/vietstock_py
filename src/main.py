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
begin_date = '02/26/18' # Month/Day/Year
end_date = '03/26/18'

with open('files/companies.json', encoding="utf-8-sig") as f:
    companies = json.load(f)

list_company = open('files/'+"list.txt", 'w') # save all company names in text files
for item in companies:
    code = item['cell'][1]
    list_company.write(code + '\n')
    excel.export({
        'exchange_name': Constants.EXCHANGE_HOSE,
        'company_code': code,
        'from_date': begin_date,
        'to_date': end_date,
        'table_title': 'Finance_Table_Title',
        'table_content': 'MatchingHoseResult'
    })
list_company.close()
