string = "Noobs out there To all you.want to say that I do not do ReadMe  I just.Learn  Watch and.more than this  Hacktober is.believe someone is reading all this  I cannot.will get interesting in the next program  Anyways it."

print(string + "\n")

print("Enter any key to unscramble")

trap = input()

listString = string.split('.')

finalList  = []
for i in listString:
    tempList = i.split(' ')
    st = []
    en = []

    count = 0
    for j in tempList:
        count = count+1
        if(len(tempList) - count<3):
            st.append(j)

        else:
            en.append(j)

    finalList.append(' '.join(st+en))

finalString = '.'.join(finalList)

print(finalString)

