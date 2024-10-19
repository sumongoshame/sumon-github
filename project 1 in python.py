# two ta pdf k add ar jonno
from PyPDF2 import PdfMerger

AllPDF = ["1.pdf","2.pdf"]

ourMerger = PdfMerger()

for NewPDF in AllPDF:
    ourMerger.append(NewPDF)

ourMerger.write("add.pdf")
ourMerger.close()

