import requests
import json
import logging

def send_reply():
	msg=d['result'][-1]['message']['text']
	log.info('The message recieved is '+msg)
	if msg=='/hello':
		return 'Hey There'
	elif msg=='/gmail':
		return 'manankpatni@gmail.com'
	elif msg=='/github':
		return 'Man-Jain'
	elif msg=='/contact':
		return '@Man_Jain'
	else:
		return 'Sorry Could Not Understand You'

def file_read():
	with open('updateid.tdt') as f:
		prev_id=f.read()
		log.info('Previous ID: '+prev_id)
		return prev_id

def main():
	update_id=''
	global d
	d={}
	bot_key='560195331:AAGDggiM9L8R6M-OL4f3g0wMAf9o_WaMLiI'
	url='https://api.telegram.org/bot'+bot_key+'/getUpdates'
	log.info('The URL is: '+url)

	while True:
		prev_id=file_read()
		log.info('Requesting url...')
		req=requests.get(url)
		d=req.json()
		latest_id=str(d["result"][-1]['update_id'])
		log.info('Latest ID: '+latest_id)


		if prev_id==latest_id:
			log.info('Waiting for users message...')
			continue
		else:
			reply_text=send_reply()
			chat_id=d['result'][-1]['message']['from']['id']
			log.info('Chat ID: '+str(chat_id))
			send_url='https://api.telegram.org/bot'+bot_key+'/sendMessage?chat_id='+str(chat_id)+'&text='+str(reply_text)
			log.info('Sending Message '+reply_text)
			send_req=requests.get(send_url)
			log.info(send_req)
			update_id=str(d['result'][-1]['update_id'])
			log.info('Writing id to file: '+str(update_id))
			with open('updateid.tdt','w') as fw:
				fw.write(update_id)

if __name__=='__main__':
	logging.basicConfig(level=logging.INFO)
	log=logging.getLogger(__name__)
	main()