from urllib.parse import urlencode, quote_plus

API_BASE_URL = 'http://finance.vietstock.vn/Controls/'
API_TRADE_RESULT = 'TradingResult'
API_EXCHANGE_LIST = 'https://www.hsx.vn/Modules/Listed/Web/SymbolList?pageFieldName1=Code&pageFieldValue1=&pageFieldOperator1=eq&pageFieldName2=Sectors&pageFieldValue2=&pageFieldOperator2=&pageFieldName3=Sector&pageFieldValue3=00000000-0000-0000-0000-000000000000&pageFieldOperator3=&pageFieldName4=StartWith&pageFieldValue4=&pageFieldOperator4=&pageCriteriaLength=4&_search=false&nd=1522075856901&rows=9999999&page=1&sidx=id&sord=desc'

EXCHANGE_HOSE = 'Hose'
EXCHANGE_HNX = 'HNX'

def get_trading_url(exchange_name, scode, from_date, to_date, investor):
	if investor == 'domestic':
		params = {
			'scode': scode,
			#'lcol': 'KLNY,KLCPDLH,GTC,T,S,TKLGD,TGTGD,VHTT,CN,TN,GYG,GD1,KLD1,GTD1,GD2,KLD2,GTD2,GD3,KLD3,GTD3,TGG,TGPTG,GDC,KLDC,BQM,BQB,DM,DB,LDM,LDB,LDMB,KLDM,KLDB,KLDMB,KLGDKL,GTGDKL,KLGDTT,GTGDTT,',
			'lcol': 'GTC,TKLGD,TGTGD,CN,TN,GD1,KLD1,GTD1,GD3,KLD3,GTD3,TGPTG,GDC,BQM,BQB,DM,DB,LDM,LDB,',
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

	elif investor == 'foreign':
		params = {
			'scode': scode,
			#'lcol': 'Room,RoomCL,RoomCLPT,KL_M_GDKL,KL_MPT_GDKL,GT_M_GDKL,GT_MPT_GDKL,CL_GT_MB,CL_KL_MB,KL_B_GDKL,KL_BPT_GDKL,GT_B_GDKL,GT_BPT_GDKL,KL_M_GDTT,KL_MPT_GDTT,GT_M_GDTT,GT_MPT_GDTT,CL_GT_MB_TT,CL_KL_MB_TT,KL_B_GDTT,KL_BPT_GDTT,GT_B_GDTT,GT_BPT_GDTT,',
			'lcol': 'KL_MPT_GDKL,GT_M_GDKL,GT_MPT_GDKL,CL_GT_MB,CL_KL_MB,KL_B_GDKL,KL_BPT_GDKL,GT_B_GDKL,GT_BPT_GDKL,KL_M_GDTT,KL_MPT_GDTT,GT_M_GDTT,GT_MPT_GDTT,CL_GT_MB_TT,CL_KL_MB_TT,KL_B_GDTT,KL_BPT_GDTT,GT_B_GDTT,GT_BPT_GDTT,',
			'sort': 'Time',
			'dir': 'desc',
			'page': 1,
			'psize': 0,
			'fdate': from_date,
			'tdate': to_date,
			'exp': 'excel'

		}
		return (API_BASE_URL + API_TRADE_RESULT + '/' + 'Foreign_Result.aspx?' +
				urlencode(params, quote_via=quote_plus))
	else:
		raise ValueError("Sai roi 3")
