from flask import Flask, render_template, escape, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the page."""
    return render_template('index.j2.html', title='Dynamic graphs with Python')

	
if __name__ == '__main__':
    app.run(debug=True)