from PyPDF2 import PdfFileReader

pdf = PdfFileReader('oops notes.pdf')

with open('pdf_to_text.text','w') as pt:
    for page_num in range(pdf.numPages):
        page = pdf.getPage(page_num)

        try:
            text = page.extractText()
        except:
            pass
        else:
            pt.write(f'page : {page_num}\n')
            pt.write('='*100)
            pt.write('\n')
            pt.write(text)
    pt.close()