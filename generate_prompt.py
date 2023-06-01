PLATFORM = "twitter"
LENGTH = "280"
ZIELGRUPPE = "junges"
FORM = "berner-deutsch"
PERSPEKTIVE = "neutralen"
VARIANTEN = 3

with open("Text.txt") as f:
    input_text = "".join(f.readlines())

prompt = f"""
   Du bist ein {PLATFORM}-Experte.
   Kannst du bitte folgenden Text 
   in {LENGTH} Zeichen
   für ein {ZIELGRUPPE} Publikum 
   auf Sprache {FORM} 
   mit einer ${PERSPEKTIVE} Perspektive zusammenfassen
   in {VARIANTEN} Varianten: [{input_text}]"""

with open("prompt.txt", 'w') as f:
    f.write(prompt)
