from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
import app.database.requests as rq

router = Router()


@router.callback_query(lambda c: c.data == 'to_main')
async def handle_to_main(callback_query: CallbackQuery):
    await callback_query.message.answer("Selecteaza te rog din menu cu ce as putea sa te ajut?")
    await callback_query.answer()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Salut! Aici poti gasi locurile ce poti sa le vizitezi! Alege din menu cu ce te-as putea ajuta', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Alege una dintre categoriile de mai jos', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Ați ales categoria')
    await callback.message.answer('Alegeți un produs după categorie',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Ați ales produsul')
    await callback.message.answer(f'Titlu: {item_data.name}\nDescriere: {item_data.description}\nPreț: {item_data.price}')


@router.message(F.text == 'Despre noi')
async def catalog(message: Message):
    await message.answer('Acest proiect a fost realizat in cadrul proiectului Python Odyssey, organizat de catre Sigmoid.\nAici gasiti link-ul lor https://www.sigmoidai.org/\n Iar pentru a fi la curent cu toate evenimentele da un follow pe pagina de instagram https://www.instagram.com/sigmo.ai/')
   
@router.message(F.text == 'Contacte')
async def catalog(message: Message):
    await message.answer('Acest proiect este doar un inceput, iar daca dvs aveti un local si ati dori sa fie aici, lasa un mesaj pe mailul: morari.nicolae1998@gmail.com sau numarul de telefon +37379023900')
    

@router.message(F.text)
async def understand(message:Message):
    await message.answer('Nu inteleg, incearca te rog sa scrii comanda /start')

