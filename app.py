from flask import Flask, render_template, request
import os
from detect import detect_people

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return render_template('index.html', result="No file uploaded!")

    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', result="No selected file!")

    # Save uploaded file
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(upload_path)

    # Detect people
    output_path = detect_people(upload_path)

    # Make path relative to 'static' and convert '\' → '/'
    relative_path = os.path.relpath(output_path, 'static').replace('\\', '/')

    return render_template('index.html', result_image=relative_path)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
