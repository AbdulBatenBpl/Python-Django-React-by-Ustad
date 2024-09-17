
"""
import zipfile
# creating zip file
with zipfile.ZipFile("new.zip", "w") as zip:
    zip.write("hello.txt")
    zip.write("hi.text")

"""
""" 
import zipfile
# Extract from zip
with zipfile.ZipFile("new.zip","r") as zip:
    zip.extractall()
    extracted_files = zip.namelist()
    print(extracted_files)
"""

import shutil
shutil.make_archive("text", "zip", "new")