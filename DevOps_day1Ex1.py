
calculations = open("calcs2.txt", mode="r").read().splitlines()

calcsDict={}
'''for index, i in enumerate(calculations, start=1):
    line=i.split(" ")


    calcsDict[index]=line'''

lineNumber=0
lineNumbers=[]
print(calculations[0])
while(True):
    line=calculations[lineNumber].split(" ")
    if "goto" in line:
        line=line[1:]
    if "calc"in line:
        operator=line[1]
        n1=int(line[2])
        n2=int(line[3])
        if operator=="+":
            lineNumber=int(int(n1)+int(n2))-1
        elif operator=="-":
            lineNumber=int(int(n1)-int(n2))-1
        elif operator=="x":
            lineNumber=int(int(n1)*int(n2))-1
        elif operator=="/":
            lineNumber=int(int(n1)/int(n2))-1
    else:
        lineNumber=int(line[0])-1
    if lineNumber in lineNumbers:
        print("Line "+str(lineNumber)+" has been reached a second time.")
        break
    else:
        lineNumbers.append(lineNumber)
    print("Output was "+ str(lineNumber)+".")

    #change in the code