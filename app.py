from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    message = ''
    if request.method == 'POST':
        plattform = request.form.get('plattform')
        zielgruppe = request.form.get('zielgruppe')
        sprache = request.form.get('sprache')
        perspektive = request.form.get('perspektive')
        varianten = request.form.get('varianten')
        format_ = request.form.get('format')
        text = request.form.get('text')

        message = f'Plattform: {plattform}, Zielgruppe: {zielgruppe}, Sprache: {sprache}, Perspektive: {perspektive}, Varianten: {varianten}, Format: {format_}, Text: {text}'

    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
