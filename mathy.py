responses = ["Welcome to Smart Calculator","My Name is Munna","Thanks","Sorry, this is beyond my ability"]

def extract_num_from_string(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def lcm(a,b):
    L = a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        else:
             L=L+1
def hcf(a,b):
    H = a if a<b else b
    while H>=1:
        if a%H ==0 and b%H==0:
            return H
    else:
        H=H-1
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def multiply(a,b):
    return a*b
def div(a,b):
    return a/b
def end():
     print(responses[2])
     input("Press enter key to exit!!!")
     exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])

operations = {"ADDITION":add,"PLUS":add,"ADD":add,"SUM":add,"SUBTRACT":sub,"DIFFERENCE":sub,"SUB":sub,
              "MINUS":sub,"PRODUCT":multiply,"MULTIPLY":multiply,"MUL":multiply,"MULTIPLIER":multiply,"DIVIDE":div,"DIVISION":div,
              "DIV":div,"LCM":lcm,"LEAST COMMON MULTIPLY":lcm,"HCF":hcf,"HIGHEST COMMON FACTOR":hcf}

commands = {"NAME":myname,"CLOSE":end,"EXIT":end,"END":end}