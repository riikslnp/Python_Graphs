import base64
from io import BytesIO
from flask import Flask, render_template, request, url_for, render_template_string
from matplotlib.figure import Figure
import json


app = Flask(__name__)


@app.route('/')
def index():
    """Renders the page."""
    return render_template('index.j2.html', title='Dynamic graphs with Python')


@app.route('/add', methods=['POST'])
def add_point():
    """ Adds clicked points into a graph"""
    try:
        # Get data from request
        data = json.loads(request.data)

        # Create the figure
        fig = Figure()
        ax = fig.subplots()
        if len(data['data']) <= 1: 
            ax.plot([data['data'][0][0]], [['data'][0][1]], marker='o', color="red")
        else:
            xs = []
            ys = []
            for i in range(0, len(data['data'])):
                xs.append(data['data'][i][0])
                ys.append(data['data'][i][1])
            ax.plot(xs, ys)
        
        # Make fig into sendable image buffer data
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        post = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template_string(f"<img id='rendered_image' src='data:image/png;base64,{post}' alt='line plot graph' />")
    except Exception as e:
        print("Error in adding points: %s", e)
        return render_template('index.j2.html', title='Dynamic graphs with Python', message="Point couldn't be added.")

	
if __name__ == '__main__':
    app.run(debug=True)