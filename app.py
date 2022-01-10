import re
import pytesseract
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = './vendor/tesseract-ocr/bin/tesseract'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print('file uploaded')
        img = Image.open(uploaded_file)
        data = pytesseract.image_to_string(img)

        res = data.split()
        pan_number = ''
        for word in res:
            if len(word) == 10 and word.isalnum():
                pan_number = pan_number + word + ' '
        if len(pan_number) >= 10:
            print("pan number is :" + pan_number)
        else:
            print("pan number not read")
        pat = pan_number

        return render_template('index.html',
                               msg='Successfully processed',
                               extracted_text=pat)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)

