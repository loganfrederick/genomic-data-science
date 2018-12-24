import os

def get_extension1(filename):
    return(filename.split(".")[-1])

def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])

def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]

print(get_extension1("myfile.tar.gz"))
print(get_extension2("myfile.tar.gz"))
print(get_extension3("myfile.tar.gz"))

filenames = os.listdir('mydir')
f= open(filenames[0])
print(f)
