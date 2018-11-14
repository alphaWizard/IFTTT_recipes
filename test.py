import requests
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/{my_key}'
print(requests.post(ifttt_webhook_url))