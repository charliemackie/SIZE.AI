import os

from flask import Flask, render_template, request, redirect

from inference import get_prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        print("GETTING PREDICTION")
        prediction = get_prediction(file) # Change this to 'file' PATH - ensure format

        return render_template('result.html', Prediction=prediction) # Pass in the prediction
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
