from PyPDF4 import PdfFileMerger
import os
fileList = [f for f in os.listdir() if f.endswith('.pdf')]
if fileList == []:
    print('No PDF file!')
else:
    for i in range(len(fileList)):
        print(i+1, ':' + fileList[i])
    print('Please enter the merger order(enter D use default order):')
    mergerOrder = input()
    file = PdfFileMerger()
    if mergerOrder == 'D':
        for cFile in fileList:
            file.append(cFile)
    else:
        for i in range(len(mergerOrder)):
            file.append(fileList[int(mergerOrder[i]) - 1])
    file.write("MergerFile.pdf")
