from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    message = 'Plattform: {}, Zielgruppe: {}, Sprache: {}, Perspektive: {}, Varianten: {}, Format: {}, Text: {}'
    if request.method == 'POST':
        plattform = request.form.get('plattform')
        zielgruppe = request.form.get('zielgruppe')
        sprache = request.form.get('sprache')
        perspektive = request.form.get('perspektive')
        varianten = request.form.get('varianten')
        format_ = request.form.get('format')
        text = request.form.get('text')

        message = message.format(plattform, zielgruppe, sprache, perspektive, varianten, format_, text)

    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
