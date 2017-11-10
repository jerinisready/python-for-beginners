from zipfile import ZipFile
zip = ZipFile("sample.zip", 'w')
zip.write("mysample.pdf", "zip-sample.pdf")
zip.close()
