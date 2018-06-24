import requests
import json

def send_reply():
	msg=d['result'][-1]['message']['text']
	print('The message recieved is '+msg)
	if msg=='/hello':
		return 'Hey There'
	elif msg=='/gmail':
		return 'manankpatni@gmail.com'
	elif msg=='/github':
		return 'Man-Jain'
	elif msg=='/contact':
		return '@Man_Jain'

def file_read():
	with open('updateid.tdt') as f:
		prev_id=f.read()
		print('Previous ID: '+prev_id)
		return prev_id

def main():
	update_id=''
	global d
	d={}
	bot_key=''
	url='https://api.telegram.org/bot'+bot_key+'/getUpdates'
	print('The URL is: '+url)

	while True:
		prev_id=file_read()
		print('Requesting url...')
		req=requests.get(url)
		d=req.json()
		latest_id=str(d["result"][-1]['update_id'])
		print('Latest ID: '+latest_id)


		if prev_id==latest_id:
			print('Waiting for users message...')
			continue
		else:
			reply_text=send_reply()
			chat_id=d['result'][-1]['message']['from']['id']
			print('Chat ID: '+str(chat_id))
			send_url='https://api.telegram.org/bot'+bot_key+'/sendMessage?chat_id='+str(chat_id)+'&text='+str(reply_text)
			print('Sending Message '+reply_text)
			send_req=requests.get(send_url)
			print(send_req)
			update_id=str(d['result'][-1]['update_id'])
			print('Writing id to file: '+str(update_id))
			with open('updateid.tdt','w') as fw:
				fw.write(update_id)

if __name__=='__main__':
	main()
