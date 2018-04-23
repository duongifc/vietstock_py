import json
import codecs
from src import vietstock_constants as Constants
from src import excel

begin_date = '04/01/18' # Month/Day/Year
end_date = '04/20/18'

params = {
	'exchange_name': Constants.EXCHANGE_HOSE,
	'company_code': 'VNM',
	'from_date': begin_date,
	'to_date': end_date,
	'table_title': 'Finance_Table_Title',
	'table_content': ['MatchingHoseResult','ForeignResult'],
	'investor': ['domestic', 'foreign']
}

excel.export(params)

#-------------------------------------------------------------------------

# UPCOM = ['ACV','HVN','DVN','BSR','POW','MCH','MSR','VGT','LPB','VIB']

# Ban_buon = ['AMV','ARM','ASM','BST','CDO','CKV','CLM','CMC','DBT','DGW','DIC',
# 			'DPS','DXV','FID','HAI','HAT','HHS','HKB','HMC','HTL','JVC','KDM',
# 			'KLF','KMT','MCF','MEL','MSC','PAN','PCN','PCT','PET','PGC','PIT',
# 			'PLX','PMG','PPY','PSC','PSD','PSE','PTB','PTS','QBS','SDP','SMA',
# 			'SMC','ST8','TCH','TDG','TH1','THS','TIE','TLH','TNA','TNI','TSC',
# 			'TTB','TTH','TXM','VFG','VID','VKC','VMD','VPG','VTV']

# Bao_hiem = ['BIC','BMI','BVH','PGI','PTI','PVI','VNR']

# Bat_dong_san = ['BII','CCL','CEO','DIG','DRH','DTA','DXG','FDC','FLC','HAR',
# 				'HDC','HDG','HLD','HQC','HTT','ICG','IDJ','IDV','IJC','ITA',
# 				'ITC','KAC','KBC','KDH','KHA','LDG','LGL','LHG','MCG','NBB',
# 				'NDN','NLG','NRC','NTL','NVL','PDR','PTL','PV2','PVL','PXA',
# 				'QCG','RCL','SCR','SDA','SGR','SGT','SJC','SJS','SZL','TDH',
# 				'TIG','TIP','TIX','VC3','VIC','VPH','VPI','VRC','VRE']

# Chung_khoan = ['AGR','APG','APS','BSI','BVS','CTS','FTS','HBS','HCM','IVS','MBS',
# 			  'ORS','PSI','SHS','SSI','TVS','VCI','VDS','VIG','VIX','VND','WSS']

# Cong_nghe_thong_tin = ['ADC','BDB','BED','CMT','DAD','DAE','DST','EBS',
# 					   'ECI','EID','ELC','GLT','HBE','HEV','HST','ITD',
# 					   'KST','LBE','ONE','QST','SED','SGD','SMN','STC','VIE']			  

# Ban_le = ['AMD','AST','BTT','CCI','CIA','CMV','COM','CTC','CTF','FPT','HAX','HTC',
# 		  'MWG','NAV','PIV','PNC','SFC','SVC','SVN','TAG','TMC','TMX','VGC','VTJ']

# Cham_soc_suc_khoe = ['DCL','DHG','DHT','DMC','DP3','IMP','LDP','MKV',
# 					 'OPC','PMC','PME','PPP','SPM','TRA','VDP','DVN']

# Khai_khoang = ['ACM','ALV','AMC','ATG','BKC','BMC','C32','CMI','CTA','CVN',
# 			   'DHA','DHM','HGM','HII','HLC','HPM','KHB','KSA','KSB','KSH',
# 			   'KSQ','LCM','MDC','MIM','NBC','NNC','PVB','PVC','PVD','PVS',
# 			   'SPI','TC6','TCS','TDN','THT','TMB','TNT','TVD','MSR']

# Ngan_hang = ['ACB','BID','CTG','EIB','HDB','KLB','MBB',
# 			 'NVB','SHB','STB','TPB','VCB','VPB','LPB','VIB']

# Nong_lam_ngu = ['APC','CTP','DPR','HAG','HKT','HNG','HRC','HVA','MLS',
# 				'NSC','PHR','PMB','PSW','SJF','SSC','TNC','TRC','VHG']

# SX_thiet_bi_may_moc = ['CJC','CTB','CTT','NAG','QHD','THI']

# SX_hang_gia_dung = ['ADS','DCS','DLG','EVE','FTM','GDT','GIL','GMC','KMR','MHL',
# 					'MPT','SAV','STK','TCM','TET','TNG','TTF','TVT','X20','VGT']

# San_pham_cao_su = ['BRC','CSM','DRC','SRC']

# SX_nhua_hoa_chat = ['AAA','ALT','BFC','BMP','CPC','CSV','DAG','DCM','DGC',
# 					'DGL','DNP','DPC','DPM','DTT','HCD','HDA','HVT','LAS',
# 					'LIX','NET','NFC','NHP','NTP','PBP','PCE','PLP','PMP',
# 					'RDP','SDN','SFG','SFN','SPP','TPC','TPP','VAF','VPS']

# Thuc_pham_do_uong = ['AGM','BBC','BHN','CAN','CLC','DAT','DBC','GTN','HAD','HHC','HNM',
# 					 'KDC','KTS','LAF','LSS','MSN','NAF','NDF','NST','SAB','SAF','SBT',
# 					 'SCD','SGC','SGO','SLS','TAC','TFC','THB','VCF','VDL','VNM','VTL','MCH']

# Thuy_san = ['AAM','ABT','ACL','AGF','ANV','BLF','CMX','FMC',
# 			'HLG','HVG','ICF','IDI','KHS','NGC','SJ1','TS4','VHC']

# Vat_lieu_xay_dung = ['ACC','BCC','BTS','CCM','CLH','CVT','DID','DNY','DTL',
# 					 'FCM','GKM','GMX','HCC','HLY','HOM','HPG','HSG','HT1',
# 					 'HVX','KHL','KKC','KSK','LBM','MCC','NHC','NKG','NSH',
# 					 'PDB','POM','QNC','S74','SCJ','SCL','SHA','SHI','TBX',
# 					 'TCR','TKU','TTC','VCS','VGS','VHL','VIS','VIT','VTS']

# Tien_ich = ['ASP','BTP','BTW','BWE','CHP','CLW','CNG','DNC','DRL','GAS',
# 			'HJS','KHP','NBP','NBW','NT2','PC1','PCG','PGD','PGS','PIC',
# 			'PPC','PVG','S4A','SBA','SEB','SHP','SIC','SII','SJD','TBC',
# 			'TDW','TMP','UIC','VPD','VSH','POW','BSR']

# Van_tai_kho_bai = ['BSC','CAG','CDN','CLL','DL1','DS3','DVP','DXP','GMD',
# 				   'GSP','HAH','HCT','HHG','HMH','HTV','MAC','MAS','MHC',
# 				   'MNC','NAP','NCT','PDN','PGT','PHP','PJC','PJT','PRC',
# 				   'PVT','SFI','SKG','STG','STT','TCL','TCO','TCT','TJC',
# 				   'TMS','TTZ','VGP','VIP','VJC','VMS','VNF','VNL','VNS',
# 				   'VNT','VOS','VSA','VSC','VSM','VTO','WCS','HVN','ACV']

# Xay_dung = ['AME','ASA','B82','BAX','BCE','BHT','C47','C69','C92','CDC',
# 			'CEE','CIG','CII','CLG','CMS','CSC','CT6','CTD','CTI','CTX',
# 			'CX8','D11','D2D','DC2','DC4','DIH','DLR','DTD','EVG','FCN',
# 			'HAS','HBC','HID','HTI','HU1','HU3','HUT','KTT','L10','L14',
# 			'L18','L35','L43','L44','L61','L62','LCD','LCG','LCS','LEC',
# 			'LGC','LHC','LIG','LM7','LM8','LO5','LTC','LUT','MCO','MDG',
# 			'MEC','MST','NDX','NHA','PEN','PHC','PPI','PTC','PTD','PVV',
# 			'PVX','PXI','PXS','PXT','QTC','REE','ROS','S55','S99','SC5',
# 			'SCI','SD2','SD4','SD5','SD6','SD7','SD9','SDD','SDE','SDT',
# 			'SDU','SJE','SRA','SRF','TA9','TCD','TDC','TEG','THG','TKC',
# 			'TST','TTL','UDC','V12','V21','VC1','VC2','VC6','VC7','VC9',
# 			'VCC','VCG','VCR','VE1','VE2','VE3','VE4','VE8','VE9','VMC',
# 			'VMI','VNE','VSI','VXB']

# sectors = [Ban_buon, Bao_hiem, Bat_dong_san, Chung_khoan, Cong_nghe_thong_tin,
# 			Ban_le, Cham_soc_suc_khoe, Khai_khoang, Ngan_hang, Nong_lam_ngu,
# 			SX_thiet_bi_may_moc, SX_hang_gia_dung, San_pham_cao_su, SX_nhua_hoa_chat,
# 			Thuc_pham_do_uong, Thuy_san, Vat_lieu_xay_dung, Tien_ich, Van_tai_kho_bai, Xay_dung]

# for sector in sectors:
# 	for code in sector:
# 		params = {
# 			'exchange_name': Constants.EXCHANGE_HOSE,
# 			'company_code': code,
# 			'from_date': begin_date,
# 			'to_date': end_date,
# 			'table_title': 'Finance_Table_Title',
# 			'table_content': 'MatchingHoseResult'
# 		}
# 		excel.export(params)

#####################################################################
# with open('files/companies.json', encoding="utf-8-sig") as f:
#     companies = json.load(f)

# list_company = open('files/'+"list.txt", 'w') # save all company names in text files
	
# for item in companies:
#     code = item['cell'][1]
#     list_company.write(code + '\n')
#     excel.export({
#         'exchange_name': Constants.EXCHANGE_HOSE,
#         'company_code': code,
#         'from_date': begin_date,
#         'to_date': end_date,
#         'table_title': 'Finance_Table_Title',
#         'table_content': 'MatchingHoseResult'
#     })
# list_company.close()
