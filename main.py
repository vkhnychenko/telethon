from telethon import TelegramClient, events
from config import SESSION_NAME, API_ID, API_HASH, CHATS
from loguru import logger

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def event_handler(sender_id: int, message):
    try:
        if message.is_reply:
            reply_message = await message.get_reply_message()
            await client.send_message(CHATS[str(sender_id)], f'Answer to message:')
            await client.forward_messages(CHATS[str(sender_id)], reply_message)
        await client.forward_messages(CHATS[str(sender_id)], message)
    except Exception as e:
        logger.error(e)


@client.on(events.NewMessage(from_users=[int(i) for i in CHATS.keys()]))
async def new_message_handler(event):
    sender = await event.get_sender()
    sender_id = event.sender_id
    logger.info(f'New message from {sender_id}')
    await event_handler(sender_id, event.message)


@client.on(events.MessageEdited(from_users=[int(i) for i in CHATS.keys()]))
async def message_edit_handler(event):
    sender = await event.get_sender()
    sender_id = event.sender_id
    logger.info(f'Message edit from {sender_id}')
    await client.send_message(CHATS[str(sender_id)], '#EDIT')
    await event_handler(sender_id, event.message)


@client.on(events.NewMessage(chats=[-1001188323070]))
async def chats_event_handler(event):
    logger.info(event.message.text)


# @client.on(events.NewMessage())
# async def test_event(event):
#     """Handler all events new message"""
#     logger.info(event.message.text)


async def get_chat(chat_name: str):
    """Get chat id all chats user"""
    async for dialog in client.iter_dialogs():
        if dialog.name == chat_name:
            logger.info(f'{dialog.name}, has ID, {dialog.id}')

logger.info('start')
client.start()
# client.loop.run_until_complete(get_chat('NEUTRINO CHAT [RU]'))
client.run_until_disconnected()
