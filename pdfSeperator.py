# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader, PdfFileWriter

# 文件名
filename = 'document'
# 分割数量
seprate = 3

inputname = filename+'.pdf'

input1 = PdfFileReader(file(inputname),'rb')

pageNumber = input1.getNumPages()

print pageNumber
lastpage = 0
for s in range(1, seprate+1):
    topage = pageNumber*s/seprate
    print "fromlastpage: %s topage %s" % (lastpage, topage)
    output = PdfFileWriter()

    # 如果不是第一部分,添加封面
    if s > 1:
        output.addPage(input1.getPage(0))

    for page in range(lastpage, topage):
        output.addPage(input1.getPage(page))

lastpage = topage
    outfileName = "%s-%d.pdf" % (filename, s)
    outputStream = file(outfileName, "wb")
    output.write(outputStream)
    outputStream.close()








