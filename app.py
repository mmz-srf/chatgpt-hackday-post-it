from flask import Flask, request, render_template
from string import Template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():

    form_data = {
        "plattform": "",
        "zielgruppe": "",
        "sprache": "",
        "perspektive": "",
        "varianten": "",
        "laenge": "",
        "format": "",
        "text": "",
    }

    template = '''
    Du bist ein ${plattform}-Experte.
    Erzeuge ein ${format} in
    ${varianten} Varianten
    mit ${laenge} Zeichen
    für ein ${zielgruppe} Publikum 
    auf ${sprache} 
    mit einer ${perspektive} Perspektive
    aus folgendem Text: [${text}]'''

    message = template
    
    if request.method == 'POST':
        for field in form_data.keys():
            form_data[field] = request.form.get(field)

        message = Template(template).substitute(form_data)

    return render_template('form.html', message=message, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
