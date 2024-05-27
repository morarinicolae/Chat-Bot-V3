
# Telegram Chatbot pentru Găsirea Locurilor de Petrecut Timpul Liber

Acest proiect este un chatbot pentru Telegram care ajută utilizatorii să găsească locuri unde să petreacă timpul liber. Botul primește cerințele utilizatorilor și oferă sugestii bazate pe acestea.

## Descriere

Chatbot-ul pentru Telegram este proiectat să răspundă la cerințele utilizatorilor privind locuri de petrecut timpul liber, cum ar fi restaurante, parcuri, muzee și alte atracții. Utilizatorii pot trimite mesaje cu preferințele lor, iar botul va răspunde cu sugestii relevante.

## Funcționalități

- Primește cerințele utilizatorilor despre locurile pe care le caută
- Răspunde cu sugestii de locuri pentru petrecerea timpului liber
- Extensibil pentru a integra API-uri pentru informații despre locații

## Tehnologii utilizate


- Python
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Aiogram](https://github.com/aiogram/aiogram)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- os (modulele standard din Python)

## Instalare

1. Clonează repository-ul:
   ```bash
   git clone https://github.com/morarinicolae/Chat-Bot-V3.git
   cd telegram-chatbot-leisure-places
2. Creează și activează un mediu virtual:
   ```bash
    python -m venv .venv
    .venv\Scripts\activate # pe Windows
    source .venv/bin/activate # pe macOS/Linux   
   
3. Instalează dependențele:
   ```bash
    pip install -r requirements.txt

4. Creează un bot pe Telegram folosind @BotFather și obține un token de autentificare.

5. Creează un fișier .env în directorul principal și adaugă token-ul botului
   ```bash
    TELEGRAM_TOKEN=your-telegram-bot-token

## Utilizare

1. Activează mediul virtual dacă nu este deja activat:
   ```bash
    .venv\Scripts\activate # pe Windows
    source .venv/bin/activate # pe macOS/Linux
2. Rulează scriptul principal:
   ```bash
    python bot.py
    Trimite comanda /start pentru a începe interacțiunea cu botul și urmează instrucțiunile pentru a primi sugestii de locuri de petrecut timpul liber.

3. Rulează testul:
   ```bash
    python test_handlers.py


## Scopuri în viitor

1. De adăugat mai multe localuri.

2. De adăugat logare pentru utilizatori în acest bot (acum la moment se înregistrează doar id-ul de pe Telegram) - asta e pentru a face o rezervare.

3. De adăugat câteva imagini.

4. De adăugat câteva funcționalități (locația, apelarea directă de pe Telegram, feedback).

   

