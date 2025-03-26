import os
path = "/home/user/documents/report.pdf"
filename = os.path.splitext(os.path.basename(path))[0]
print(filename)  


