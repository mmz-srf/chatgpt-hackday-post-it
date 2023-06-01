PLATFORM = "twitter"
LENGTH = "280"
ZIELGRUPPE = "junges"
SPRACHE = "berner-deutsch"
PERSPEKTIVE = "neutralen"
VARIANTEN = 3
OUTPUT_FORMAT = "Tweet"

with open("Text.txt") as f:
    input_text = "".join(f.readlines())

prompt = f"""
   Du bist ein {PLATFORM}-Experte.
   Kannst du bitte aus folgenden Text 
   {VARIANTEN} Varianten für ein
   {OUTPUT_FORMAT}
   mit {LENGTH} Zeichen
   für ein {ZIELGRUPPE} Publikum 
   auf {SPRACHE} 
   mit einer {PERSPEKTIVE} Perspektive erzeugen
   : [{input_text}]"""

with open("prompt.txt", 'w') as f:
    f.write(prompt)
