#ex 1

#lines="int x=5;"

#file  = open("./add.c", 'r')
#lines = file.readlines()

lines=""

keywords    = ["void", "main", "int", "float", "bool", "if", "for", "else", "while", "char", "return"]
operators   = ["=", "==", "+", "-", "*", "/", "++", "--", "+=", "-=", "!=", "||", "&&"]
punctuations= [";", "(", ")", "{", "}", "[", "]"]

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False







def parsefn(b):
    a=""
    for line in b:
        for i in line.strip().split(" "):
            a+="\n"
            if i in keywords:
                a=a+" "+i+" is a keyword"
            elif i in operators:
                a=a+" "+i+" is an operator"
            elif i in punctuations:
                a=a+" "+i+" is a punctuation"
            elif is_int(i):
                a=a+" "+i+" is a number"
            else:
                a=a+" "+i+" is an identifier"
    return(a)

    
##
##for line in lines:
##    for i in line.strip().split(" "):
##        if i in keywords:
##            print (i, " is a keyword")
##        elif i in operators:
##            print (i, " is an operator")
##        elif i in punctuations:
##            print (i, " is a punctuation")
##        elif is_int(i):
##            print (i, " is a number")
##        else:
##            print (i, " is an identifier")
