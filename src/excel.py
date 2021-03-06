import requests
from bs4 import BeautifulSoup
import csv
import codecs
import os

from src import vietstock_constants as Constants

def export(params):
	# file_name = (params['exchange_name'] + '_' +
	#              params['company_code'] + '_' +
	#              params['from_date'] + '_' +
	#              params['to_date']) + '.csv'
	file_name = (params['company_code'] + '_' +
				 params['from_date'] + '_' +
				 params['to_date']) + '.csv'
	file_name = file_name.replace('/', '_')

	try:
		print(file_name)
		file_path = 'files/' + file_name
		if not os.path.exists('files'):
			os.makedirs('files')

		titles = []
		soups = []
		for investor in params['investor']:
			url = Constants.get_trading_url(
				params['exchange_name'], params['company_code'], params['from_date'], params['to_date'], investor
			)
			page = requests.get(url)

			# Create a BeautifulSoup object
			soup = BeautifulSoup(page.text, 'html.parser')
			soups.append(soup)

			title_elements = soup.find(class_=params['table_title']).find_all('b')
			for title_element in title_elements:
				if len(title_element.contents) > 0:
					elementValue = title_element.contents[0]
					if elementValue.isdigit():
						titles.append(float(title_element.contents[0].replace(',', '')))
					else:
						titles.append(title_element.next)

		with codecs.open(file_path, 'w', 'utf-8-sig') as fp:
			f = csv.writer(fp)
			f.writerow(titles)
			for soup, tc in zip(soups, params['table_content']):
				content = soup.find(id=tc).find('tbody').find_all('tr')
				#total_kl = []
				for trElement in content:
					tdValues = []
					tdElements = trElement.find_all('td')
					#total_kl.append(float(tdElements[-1].contents[0].replace(',', '')))

					for tdElement in tdElements:
						content = tdElement.contents
						if len(content) > 0:
							if tdElement.contents[0].isdigit():
								tdValues.append(tdElement.contents[0].replace(',', ''))
							else:
								tdValues.append(tdElement.next)
					f.writerow(tdValues)

			#if len(total_kl) > 0 and sum(total_kl) / float(len(total_kl)) > 10000:
			 #   os.remove(file_path)
	except ValueError:
		print('Phắc >"<, có lỗi với file ' + file_name)
		print(ValueError)


#----------------------------------------------
# def export(params):
# 	# file_name = (params['exchange_name'] + '_' +
# 	#              params['company_code'] + '_' +
# 	#              params['from_date'] + '_' +
# 	#              params['to_date']) + '.csv'
# 	file_name = (params['company_code'] + '_' +
# 				 params['from_date'] + '_' +
# 				 params['to_date']) + '.csv'
# 	file_name = file_name.replace('/', '_')

# 	try:
# 		print(file_name)
# 		file_path = 'files/' + file_name
# 		if not os.path.exists('files'):
# 			os.makedirs('files')

# 		titles = []
# 		url = Constants.get_trading_url(
# 			params['exchange_name'], params['company_code'], params['from_date'], params['to_date'],
# 		)
# 		page = requests.get(url)

# 		# Create a BeautifulSoup object
# 		soup = BeautifulSoup(page.text, 'html.parser')
# 		title_elements = soup.find(class_=params['table_title']).find_all('b')
# 		for title_element in title_elements:
# 			if len(title_element.contents) > 0:
# 				elementValue = title_element.contents[0]
# 				if elementValue.isdigit():
# 					titles.append(float(title_element.contents[0].replace(',', '')))
# 				else:
# 					titles.append(title_element.next)

# 		with codecs.open(file_path, 'w', 'utf-8-sig') as fp:
# 			f = csv.writer(fp)
# 			f.writerow(titles)

# 			content = soup.find(id=params['table_content']).find('tbody').find_all('tr')
# 			#total_kl = []
# 			for trElement in content:
# 				tdValues = []
# 				tdElements = trElement.find_all('td')
# 				#total_kl.append(float(tdElements[-1].contents[0].replace(',', '')))

# 				for tdElement in tdElements:
# 					content = tdElement.contents
# 					if len(content) > 0:
# 						tdValues.append(tdElement.contents[0].replace(',', ''))
# 				f.writerow(tdValues)

# 		#if len(total_kl) > 0 and sum(total_kl) / float(len(total_kl)) > 10000:
# 		 #   os.remove(file_path)
# 	except ValueError:
# 		print('Phắc >"<, có lỗi với file ' + file_name)
# 		print(ValueError)
