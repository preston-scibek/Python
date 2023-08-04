import requests
import json
import time



with open (".env.json", 'r') as jfile:
    tokens = json.load(jfile)
    DISCORD_TOKEN = tokens['DISCORD_TOKEN']
    SERVER_ID = tokens['SERVER_ID']
    AUTHOR_ID = tokens['AUTHOR_ID']
    CHANNEL_ID = tokens['CHANNEL_ID']

headers = {
  'Authorization': f'{DISCORD_TOKEN}',
}

def get_messages():
    try:
        messages = []
        last_message_id = "1136392850519642133"
        sleep_occurences = 0
        zeroed = 0
        while last_message_id:
            search_url = f"https://discordapp.com/api/v9/guilds/{SERVER_ID}/messages/search?author_id={AUTHOR_ID}&channel_id={CHANNEL_ID}&max_id={last_message_id}"

            response = requests.get(search_url, headers=headers)
            res = response.json()
            if len(messages) == 0:
                print(res['total_results'])
            
            if response.status_code == 200:
                messages.extend(res['messages'])
                if len(res['messages']) == 0:
                    zeroed+=1
                    print(f"Response has no messages, sleeping for 5 second")
                    time.sleep(5)
                    if zeroed == 5:
                        print("messages have returned 0 , 5 times, breaking search loop")
                        break
                else:
                    new_last_message_id = messages[-1][0]['id']
                    last_message_id = new_last_message_id if last_message_id != new_last_message_id else False

            elif response.status_code == 429:
                tts = float(response.json()['retry_after']) * 3
                print(f"429 for search, Sleeping for {tts} seconds")
                time.sleep(tts)
                sleep_occurences += 1
                if sleep_occurences % 20 == 0 and False:
                    print(f"Have been rated limited {sleep_occurences} times , moving to deletion") 
                    break
                    print(f"Have been rated limited {sleep_occurences} times , sleeping for 5 seconds")
                    time.sleep(5)
            if len(messages) > 1000 and False:
                break
            else:
                print(len(messages))
            time.sleep(.25)

        return messages
    except KeyboardInterrupt:
        return messages
    except Exception as e:
        print(e)
        return messages


def delete_messages(messages):
    failed_to_delete = []
    deleted = []
    messages_deleted = 0
    sleep_occurences = 0
    total_messages = len(messages)
    while len(messages) > 0:
        message = messages[0]
        print(f"{messages_deleted} / {total_messages} : Deleting : {message['content']} ({message['id']}) {message['timestamp']}")
        delete_url = f"https://discordapp.com/api/v6/channels/{message['channel_id']}/messages/{message['id']}"
        response = requests.delete(delete_url, headers=headers)
        
        if response.status_code == 404:
            failed_to_delete.append(messages.pop(0))
            print(f"404: Failed to delete {message['id']} ({message['content']})")
            continue
        elif response.status_code == 429:
            tts = float(response.json()['retry_after']) * 3
            print(f"429: Failed to delete {message['id']}, Sleeping for {tts} seconds")
            time.sleep(tts)
            sleep_occurences += 1
            if sleep_occurences % 5 == 0:
                print(f"Have been rated limited {sleep_occurences} times, sleeping for 5 seconds")
                time.sleep(5)
        elif response.status_code == 204:
            deleted.append(messages.pop(0))
            messages_deleted += 1
            time.sleep(.25)
        else:
            failed_to_delete.append(messages.pop(0))
            print(f"Failed to delete {message['id']} ({message['content']}, request returned {response.status_code})")
            continue
    print(f"failed to delete {len(failed_to_delete)}")
    print(f"deleted {len(deleted)}")

if __name__ == "__main__":
    with open('messages.json', 'r') as jfile:
        messages = json.load(jfile)
    messages = messages[1943+60::]
    if len(messages) > 0:
        delete_messages(messages)
        messages = []
    #else:
    messages = get_messages()
    messages = [message[0] for message in messages]
    with open('messages.json', 'w') as jfile:
        json.dump(messages, jfile, indent=4)
    delete_messages(messages)