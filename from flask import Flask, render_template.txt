from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ""
    if request.method == 'POST':
        query = request.form['search']
        # Hier können Sie die Suche verarbeiten
    return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
