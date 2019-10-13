string = "To all you Noobs out there. I just want to say that I do not do ReadMe. Watch and Learn. Hacktober is more than this. I cannot believe someone is reading all this. Anyways it will get interesting in the next program."

print("For those interested in knowing how the previous program was done.\n")
print(string+ "\n")

tempString = string.split('.')
c = 0

listFinal = []
for i in tempString:
    c = 0
    x = i.split(' ')
    st = []
    en = []
    for j in x:
        c = c+1
        if (c<=3):
            en.append(j)
        else:
            st.append(j)
    
    st = st+en

    listFinal.append(' '.join(st))

finalString = '.'.join(listFinal)
print(finalString)
