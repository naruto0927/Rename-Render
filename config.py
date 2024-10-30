import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23861777")

API_HASH = os.environ.get("API_HASH", "16104c9a6a05c337237819a218d46c5d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8095772116:AAF6t3wwX4LMFj_bypU-EE-Poi6F6FHvRAI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "omniscient_reader_view_poinnt") 

DB_NAME = os.environ.get("DB_NAME", "renamenbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://patelbhart45y666:yUY67YQZis7FS1op@cluster0.zsmsb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/a095dc9dc288a142615b8-8d3f123470412ab17c.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6672752177').split()]

PORT = os.environ.get("PORT", "8080")

