S ='abccebbeca'
Slist= [i for i in S]
new_s = []
duplicateFoundCount = 0
new_s.append(Slist[0])
for index, char in enumerate (Slist[1:]):
    if len(new_s) == 0:
        new_s.append(char)
    else:
        if char == new_s[-1]:
            if index == len(Slist) -2:
                new_s.pop()
                break
            duplicateFoundCount += 1
                
        else:#come in a different char
            if duplicateFoundCount == 0:
                new_s.append(char)
            else:
                new_s.pop()
                duplicateFoundCount = 0
                if len(new_s) >= 1 and new_s[-1] == char:
                    if index == len(Slist) -2:
                        new_s.pop()
                        break
                    duplicateFoundCount += 1
                else:
                    new_s.append(char)
                    duplicateFoundCount = 0

print(new_s)
