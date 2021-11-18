from telethon import TelegramClient, events
from config import SESSION_NAME, API_ID, API_HASH
from asyncio import sleep

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def event_handler(event, sender_id, forward_chat_id):
    if event.sender_id == sender_id:
        if event.message.is_reply:
            reply_message = await event.message.get_reply_message()
            await client.send_message(forward_chat_id, f'В ответ на сообщение:')
            await client.forward_messages(forward_chat_id, reply_message)
        await client.forward_messages(forward_chat_id, event.message)


async def message_handler(message, sender_id, forward_chat_id):
    if message.sender_id == sender_id:
        if message.is_reply:
            reply_message = await message.get_reply_message()
            await client.send_message(forward_chat_id, f'В ответ на сообщение:')
            await client.forward_messages(forward_chat_id, reply_message)
        await client.forward_messages(forward_chat_id, message)
        await sleep(1)


@client.on(events.NewMessage())
async def new_message_event_handler(event):
    await event.get_chat()
    await event.get_sender()
    await event_handler(event, 233787240, -657152166) #Slavik Investor
    await event_handler(event, 58149469, -642005665) #Anton Katin
    await event_handler(event, 309275950, -652900673) #Test


# async def main():
#     async for dialog in client.iter_dialogs():
#         if dialog.name == 'Test bot':
#             print(dialog.name, 'has ID', dialog.id)

    # async for message in client.iter_messages(-1001188323070):
    #     await message_handler(message, 58149469, -642005665)
    #     print(message.sender_id)
    #     print(message.id, message.text)


# with client:
#     client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
