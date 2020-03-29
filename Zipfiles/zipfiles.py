import zipfile

# Create a zip file

with zipfile.ZipFile('files.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('cat.jpg')
    my_zip.write('textfile.txt')

# Extract the zip file
with zipfile.ZipFile('files.zip','r') as my_zip:
    my_zip.extractall('files')
    print("Extracted!! ")

