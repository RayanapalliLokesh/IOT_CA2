import requests
import time
import json

while 1:
	
'''	
	
	to write the data as 1 to control led use write URL 
	thats is 'https://api.thingspeak.com/update?api_key=Z6HYMTKQN814W86O&field1=1'
	else 'https://api.thingspeak.com/update?api_key=Z6HYMTKQN814W86O&field1=0'
	
'''
		
	URL='https://api.thingspeak.com/channels/1922332/fields/1.json?api_key=829XS50YSO7LTAOC&results=1'
	data=requests.get(URL).json()
	feeds_data=data['feeds']
	new_data=json.dumps(feeds_data)
	final_data=json.loads(new_data)
	
	for item in final_data:
		led_status=item['field1']
		
	if led_status == '1':
		print('Turn on Led')
		
	else:
		print('Led is Off')
		
	time.sleep(15)			
	
