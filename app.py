from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    message = '''
    Du bist ein {PLATFORM}-Experte.
    Kannst du bitte aus folgenden Text 
    {VARIANTEN} Varianten für ein
    {OUTPUT_FORMAT}
    mit {LENGTH} Zeichen
    für ein {ZIELGRUPPE} Publikum 
    auf {SPRACHE} 
    mit einer {PERSPEKTIVE} Perspektive erzeugen
    : [{TEXT}]'''
    
    if request.method == 'POST':
        plattform = request.form.get('plattform')
        zielgruppe = request.form.get('zielgruppe')
        sprache = request.form.get('sprache')
        perspektive = request.form.get('perspektive')
        varianten = request.form.get('varianten')
        format_ = request.form.get('format')
        length = request.form.get('length')
        text = request.form.get('text')

        message = message.format(PLATFORM=plattform, ZIELGRUPPE=zielgruppe, SPRACHE=sprache, PERSPEKTIVE=perspektive, VARIANTEN=varianten, OUTPUT_FORMAT=format_, TEXT=text, LENGTH=length)

    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
