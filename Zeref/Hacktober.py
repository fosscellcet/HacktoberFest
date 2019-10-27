string = "Noobs out there To all you.want to say that I do not do ReadMe  I just.Learn  Watch and.more than this  Hacktober is.believe someone is reading all this  I cannot.will get interesting in the next program  Anyways it."

print(string + "\n")

print("Enter any key to unscramble")

trap = input()

listString = string.split('.')

finalList1  = []
for j in listString:
    tempList = j.split(' ')
    st = []
    en = []

    count = 0
    for i in tempList:
        count = count+1
        if(len(tempList) - count<3):
            st.append(i)

        else:
            en.append(i)

    finalList1.append(' '.join(st+en))

finalString1 = '.'.join(finalList1)

print(finalString1)

