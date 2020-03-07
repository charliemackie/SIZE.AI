import os

from flask import Flask, render_template, request, redirect, url_for
from inference import get_prediction
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/dante/Documents/GitHub/SIZE.AI/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        absolute_path = os.path.abspath("../")
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if not file:
            return
        print("GETTING PREDICTION")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction = get_prediction(file) # Change this to 'file' PATH - ensure format
        return render_template('result.html', Prediction=prediction, File=filename) # Pass in the prediction
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
