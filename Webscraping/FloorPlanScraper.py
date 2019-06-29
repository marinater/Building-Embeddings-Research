from requests_html import HTMLSession
import time



inputFile = open('plan_numbers.txt')
plans = [line.strip() for line in inputFile.readlines()]
inputFile.close()





output = open('data.csv', 'w')
session = HTMLSession()
base_url = 'http://www.ultimateplans.com/Plans/{}.aspx'





for plan_number in plans:
	print(plan_number)
	url = base_url.format(plan_number)
	r = session.get(url)

	labels = r.html.find('td.SpecLabel') + r.html.find('td.SpecLabel1') + r.html.find('td.specification')
	text = r.html.find('td.SpecData') +  r.html.find('td.SpecData1') + r.html.find('td.detail')

	if (len(labels) + len(text) != 24):
		print("data not found for plan number", plan_number)
		continue

	combined_data = { labels[i].text.strip(':') : text[i].text for i in range(12) }
	combined_data['Number'] = plan_number

	images = r.html.find('center img')
	
	if len(images) > 0:
		combined_data["Bottom"] = images[0].attrs['src']
	if len(images) > 1:
		combined_data["Top"] = images[1].attrs['src']

	for val in combined_data.values():
		output.write(val.strip().replace('\n', '|').replace(',', '+') + ',')
	output.write('\n')

for key in combined_data.keys():
	output.write(key + ',')
output.write('\n')