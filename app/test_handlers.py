import unittest
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher
from aiogram.test import TestBot, TestDispatcher

from app.handlers import router

class TestHandlers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bot = TestBot(token='TEST_TOKEN')
        cls.dp = TestDispatcher(cls.bot)
        cls.dp.include_router(router)

    def setUp(self):
        self.bot.reset()

    async def test_cmd_start(self):
        message = Message(
            message_id=1,
            from_user=User(id=123456789, is_bot=False, first_name='TestUser'),
            chat=Chat(id=123456789, type='private'),
            date=datetime.now(),
            text='/start'
        )
        results = await self.dp.message_handlers.handle(message)
        self.assertEqual(results[0].text, 'Salut! Aici poti gasi locurile ce poti sa le vizitezi! Alege din menu cu ce te-as putea ajuta')

    async def test_handle_to_main(self):
        callback_query = CallbackQuery(
            id='1',
            from_user=User(id=123456789, is_bot=False, first_name='TestUser'),
            message=Message(
                message_id=1,
                from_user=User(id=123456789, is_bot=False, first_name='TestUser'),
                chat=Chat(id=123456789, type='private'),
                date=datetime.now(),
                text='Test'
            ),
            data='to_main'
        )
        results = await self.dp.callback_query_handlers.handle(callback_query)
        self.assertEqual(results[0].text, "Selecteaza te rog din menu cu ce as putea sa te ajut?")

if __name__ == '__main__':
    unittest.main()
