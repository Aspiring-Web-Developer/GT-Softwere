# with open('newcontent.txt','w') as f:
#    f.write('THIS IS python class')


# with open('ademotext.txt','w') as f:
#    f.write('this is demo text')

# with open('ademotext.txt','w') as f:
#    f.write('deepak')


# with open('ademotext.txt','a') as f:
#    f.write('venkat ')
#    f.write('lakshmanan')

# with open('ademotext.txt','r') as f:
#     content=f.read()
#     print(content)



# with open('pyfiles.pdf','rb') as f: #we can read but unable to get in readable format
#     cnt=f.read()
#     print(cnt)

# pip install PyPDF2

# from PyPDF2 import PdfReader



# reader = PdfReader("pyfiles.pdf")
# with open('filehandlingrules.txt','a') as f:
#  for page in reader.pages:
#     text = page.extract_text()
#     print(text)
#     f.write(text)

with open('arjundas.txt','w') as f:
    f.write("Arjundas have multitalented person")

with open('arjundas.txt','a') as f:
    f.write(' even he is so handsomboy')

with open('arjundas.txt','r') as f:
    content=f.read()
    print(content)

from PyPDF2 import PdfReader

reader= PdfReader('pyfiles.pdf')

with open('arjundas.txt','a') as f:
    for pages in reader.pages:
        text=pages.extract_text()
        print(text)
        f.write(text)
