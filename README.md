# TelegramChatBot
My first chat bot telegram\

Pentru inceput creem un Bot in telegram, cautam user-ul @BotFather, dupa care inseram comanda /newbot si urmam pasii 

Pentru a functiona codul trebuie de urmat urmatorii pasi:
-- instalam mediul virtual
python -m venv .venv
--pentru activarea mediului virtual folosim urmatorul cod:
.venv\Scripts\activate
--iar pentru a dezactiva mediul virtual folosim:
deactivate
-- Acum trebuie sa instalam Aiogram
pip install aiogram

--Iar pentru baza de date folosim:
pip install sqlalchemy aiosqlite

Iar pentru a merge acest proiect trebuie sa instalam si dotenv, aici se ascunde TOKEN-ul:
pip install python-dotenv


-------------Life hack-------------
Se poate de scris toate odata:
pip install aiogram sqlalchemy aiosqlite python-dotenv
------------------------------------

Pentru a face scraping de date avem nevoie sa instalam librariile
pip install requests

----pentru instalarea librariilor---
pip freeze > requirements.txt 
pip install -r .\requirements.txt