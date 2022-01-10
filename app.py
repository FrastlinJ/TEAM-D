import re
import pytesseract
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# pytesseract.pytesseract.tesseract_cmd = './vendor/tesseract-ocr/bin/tesseract'

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
    app.run(debug=True)






# def read_data(file):
#     data = Image.open(file)
#     text = pytesseract.image_to_string(data, lang='eng')
#     print(text)
#     return text
#
#
# def pan_read_data(text):
#     name = None
#     fname = None
#     dob = None
#     pan = None
#     nameline = []
#     dobline = []
#     panline = []
#     text0 = []
#     text1 = []
#     text2 = []
#     lines = text.split('\n')
#
#     for lin in lines:
#         s = lin.strip()
#         s = lin.replace('\n','')
#         s = s.rstrip()
#         s = s.lstrip()
#         text1.append(s)
#         text1 = list(filter(None, text1))
#         lineno = 0
#     for wordline in text1:
#         xx = wordline.split('\n')
#         if ([w for w in xx if re.search('(INCOMETAXDEPARWENT|INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$', w)]):
#             text1 = list(text1)
#             lineno = text1.index(wordline)
#             break
#         text0 = text1[lineno+1:]
# try:
#     # Cleaning first names
#     name = text0[0]
#     name = name.rstrip()
#     name = name.lstrip()
#     name = name.replace("8", "B")
#     name = name.replace("0", "D")
#     name = name.replace("6", "G")
#     name = name.replace("1", "I")
#     name = re.sub('[^a-zA-Z] +', ' ', name)
#     # Cleaning Father's name
#     fname = text0[1]
#     fname = fname.rstrip()
#     fname = fname.lstrip()
#     fname = fname.replace("8", "S")
#     fname = fname.replace("0", "O")
#     fname = fname.replace("6", "G")
#     fname = fname.replace("1", "I")
#     fname = fname.replace("\"", "A")
#     fname = re.sub('[^a-zA-Z] +', ' ', fname)
#     # Cleaning DOB
#     dob = text0[2][:10]
#     dob = dob.rstrip()
#     dob = dob.lstrip()
#     dob = dob.replace('l', '/')
#     dob = dob.replace('L', '/')
#     dob = dob.replace('I', '/')
#     dob = dob.replace('i', '/')
#     dob = dob.replace('|', '/')
#     dob = dob.replace('\"', '/1')
#     dob = dob.replace(" ", "")
#     # Cleaning PAN Card details
#     text0 = findword(text1, '(Pormanam|Number|umber|Account|ccount|count|Permanent|ermanent|manent|wumm)$')
#     panline = text0[0]
#     pan = panline.rstrip()
#     pan = pan.lstrip()
#     pan = pan.replace(" ", "")
#     pan = pan.replace("\"", "")
#     pan = pan.replace(";", "")
#     pan = pan.replace("%", "L")
# except:
#     pass
# # data = {}
# # data['Name'] = name
# # data['Father Name'] = fname
# # data['Date of Birth'] = dob
# # data['PAN'] = pan
# # data['ID Type'] = "PAN"
# # return data
#
# def findword(textlist, wordstring):
#     lineno = -1
#     for wordline in textlist:
#         xx = wordline.split( )
#         if ([w for w in xx if re.search(wordstring, w)]):
#             lineno = textlist.index(wordline)
#             textlist = textlist[lineno+1:]
#             return textlist
#     return textlist
#
#
pan_read_data(read_data('Whatsapp Image 2020-07-24 at 10.41.28.jpeg'))