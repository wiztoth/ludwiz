import os
from dotenv import load_dotenv

# Carica il file .env
load_dotenv()

#spells credentials
db_user_spell = os.getenv("DB_SPELL_USER")
db_psw_spell = os.getenv("DB_SPELL_PASS")
db_name_spell = os.getenv("DB_SPELL_NAME")
#weapons credentials
db_user_weapons = os.getenv("DB_WEAPONS_USER")
db_psw_weapons = os.getenv("DB_WEAPONS_PASS")
db_name_weapons = os.getenv("DB_WEAPONS_NAME")






