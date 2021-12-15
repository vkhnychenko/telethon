# Telethon parser

## Configure project
- Create .env file
    * API_ID
    * API_HASH
    * SESSION_NAME
    

- create chats.json file
  * {"USER_ID": FORWARD_CHAT_ID}
## Run project

### First launch

```
docker-compose build
docker-compose run bot python ./main.py
```

### Other launch
```
docker-compose up
```