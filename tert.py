import re

def readfile ():
    filename = input ('Print the way to the file ')
    ff = open (filename, 'r', encoding = 'utf-8')
    f = ff.readlines ()
    ff.close
    return f

def lookfornames (f):
    regex = ' ([А-Я]\. *[А-Я][а-я]+)'
    for line in f:
        res = re.findall (regex, line)
        for elem in res:
            print (elem)

def lookagain (f):
    regex2 = '[А-Я]\. [А-Я]\. [А-Я][а-я]+'
    regex3 = '[А-Я][а-я]+ [А-Я][а-я]+'
    for line in f:
        res2 = re.findall (regex2, line)
        res3 = re.findall (regex3, line)
        for name in res2:
            print (name)
        for match in res3:
            print (match)
    
def main ():
    fun1 = readfile ()
    fun2 = lookfornames (fun1)
    fun3 = lookagain (fun1)

if __name__ == '__main__':
    main ()
        
        
