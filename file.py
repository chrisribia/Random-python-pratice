import os
from datetime import datetime
from datetime import timedelta
# Delete The File
now = datetime.now()
try:
    os.remove('file.txt')
except:
    print("")

# create file
with open('file.txt','xt') as f:
    f.write(now)
    f.close()




# read from a file
with open('file.txt','rt') as f:
   data = f.read()
   print(data)
   f.close()
