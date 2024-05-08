filename = "./text.txt" #zde určete vstupní soubor

#----

file = open(filename, "r")

text = file.read()

file.close()

split = text.split("\n")

csv = ""

dataBlock = ""

i = 0
while i < len(split):
    if "18. stol" in split[i]:
        csv += split[i]+"\n"
        i+=1

        while "19. stol" not in split[i]:

            csv += split[i]+","+split[i+1]+","+split[i+2]+","+split[i+3]+","+split[i+4]+"\n"
            i+=5
        

        csv += split[i]+"\n"
        i+=1
        while "20. a 21." not in split[i]:

            csv += split[i]+","+split[i+1]+","+split[i+2]+","+split[i+3]+","+split[i+4]+"\n"
            i+=5
        
        
        csv += split[i]+"\n"
        i+=1
        while "20. a 21." not in split[i]:

            csv += split[i]+","+split[i+1]+","+split[i+2]+","+split[i+3]+","+split[i+4]+"\n"
            i+=5

        csv += split[i]+"\n"
        i+=1

        while i < len(split):

            csv += split[i]+","+split[i+1]+","+split[i+2]+","+split[i+3]+","+split[i+4]+"\n"
            i+=5

print(csv)

newFile = open("result.csv", "w")
newFile.write(csv)
newFile.close