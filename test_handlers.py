import os
import pytest
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, User, Chat
from aiogram.utils.keyboard import InlineKeyboardMarkup
from app.handlers import router
from dotenv import load_dotenv
import app.keyboards as kb
import app.database.requests as rq

# Functia pentru a crea si returna obiectul botului
async def create_bot():
    load_dotenv(dotenv_path='.env')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not telegram_bot_token:
        raise ValueError("Nu s-a gasit Tokenul necesar")

    # Initializeaza si intoarce obiectul botului
    return Bot(token=telegram_bot_token, parse_mode='HTML')

# Fixture-ul bot() care apeleaza create_bot() si asteapta obtinerea obiectului botului
@pytest.fixture
async def bot():
    return await create_bot()

# Test pentru handler-ul cmd_start
@pytest.mark.asyncio
async def test_cmd_start(bot):
    user = User(id=123456789, is_bot=False, first_name='TestUser')
    chat = Chat(id=123456789, type='private')
    message = Message(
        message_id=1,
        from_user=user,
        chat=chat,
        date=None,
        text='/start'
    )

    # Initializeaza storage-ul
    storage = MemoryStorage()

    # Initializeaza Dispatcher-ul
    dp = Dispatcher(bot, storage=storage)
    dp.include_router(router)

    # Asteapta initializarea obiectului botului
    await bot.get_me()

    # Obține starea curenta a utilizatorului
    state = dp.current_state(chat=chat.id, user=user.id)
    await state.set_state(None)  # Resetare stare

    responses = []

    # Functie fake_send_message pentru a inlocui send_message
    async def fake_send_message(chat_id, text, reply_markup, **kwargs):
        responses.append((chat_id, text, reply_markup, kwargs))

    bot.send_message = fake_send_message

    # Feed update pentru a trimite mesajul catre dispatcher
    update = {"message": message}
    await dp.router.process_update(update)

    # Verifica raspunsurile
    assert len(responses) == 1
    assert responses[0][1] == 'Salut! Aici poti gasi locurile ce poti sa le vizitezi! Alege din menu cu ce te-as putea ajuta'
    assert isinstance(responses[0][2], InlineKeyboardMarkup)
    assert responses[0][2] == kb.main

print("Testul pentru cmd_start a fost finalizat cu succes!")
