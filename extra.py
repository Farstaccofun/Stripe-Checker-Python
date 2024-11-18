import requests

def hit_sender(card,message,chat_id):
    bot_token = '7258733018:AAGxCaThUukOoL5kueCIELn1SrCf0TBtSjw'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
