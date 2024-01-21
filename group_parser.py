import re
from asyncio import sleep

from telethon import TelegramClient
from config import SESSION_NAME, API_ID, API_HASH
from google_sheets import append_data

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

PARSING_CHAT_ID = '-1001756744048'


async def main():

    chat_entity = await client.get_entity(-1001756744048)
    async for message in client.iter_messages(chat_entity, reverse=True):
        print(message)
        print(message.sender_id, ':', message.text)

        if not message.sender_id:
            continue

        if not message.text:
            continue

        user_info = await client.get_entity(message.sender_id)
        print('user_info: ', user_info)

        url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        urls = re.findall(url_regex, message.text)
        print('urls', urls)

        # instagram_url = urls[0]
        # print('instagram_url', instagram_url)
        if user_info.username:
            append_data('test', [user_info.username, user_info.first_name, 'instagram_url', message.text])
        await sleep(1)

    # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message(-100123456, 'Hello, group!')
    # # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')

    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )


with client:
    client.loop.run_until_complete(main())