PLATFORM = "twitter"
LENGTH = "280"
ZIELGRUPPE = "junges"
FORM = "berner-deutsch"
PERSPEKTIVE = "neutralen"

with open("Text.txt") as f:
    input_text = "".join(f.readlines())

prompt = f"""
   Du bist ein {PLATFORM}-Experte.
   Kannst du bitte folgenden Text in {LENGTH} Zeichen
   für ein {ZIELGRUPPE} Publikum 
   auf Sprache {FORM} mit einer ${PERSPEKTIVE} Perspektive zusammenfassen: [{input_text}]"""

print(prompt)