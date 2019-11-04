import re
import os.path

with open("Paper.txt", "r") as myFile:
    data = myFile.read()

emails = re.findall('\S+@\S+', data)
email_file = open("email_file.txt", "w+")
email_file.write(str(emails))
email_file.close()
