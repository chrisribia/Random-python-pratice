import os


try:
    os.remove('file.txt')
except:
    print("")


# create file
with open('file.txt','xt') as f:
    name = [f.write(x) for x in os.listdir('F:\movies\person of intrest') if x.endswith(".mp4")]
    f.close()


# read from a file
with open('file.txt','rt') as f:
   data = f.read()
   print(data)
   f.close()


