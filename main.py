import threading
import requests
log = open('all.log', 'w')
with open('api.txt', 'r') as token_file:
    tokens = token_file.read().splitlines()
with open('users.txt', 'r') as users_file:
    users = users_file.read().splitlines()
message = '''
test text
'''
def send_message(token, user_id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {
        'chat_id': user_id,
        'text': message
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print(f'Send {user_id} use {token}')
    else:
        log.write(f'Error {user_id} use {token}: {response.text}')
for user_id in users:
    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_message, args=(token, user_id))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
