import docx
import docx2txt
import re
with open('file_5.docx', 'rb') as f:
    text = docx2txt.process(f)
    ad = re.split(r"።", text)
    for i in ad:
        if i  != '\n':
            print(i+'።')
