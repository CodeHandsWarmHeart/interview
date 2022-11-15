#题目大概是 输入abbaca 去掉连续重复的字母 第一步去掉a'bb'aca 中的bb, 得到aaca, 还是去掉重复的字母 即'aa'ca中的aa 得到最终结果 ca
#耗时的算法需要遍历一遍后 多次反复遍历已得结果， 时间复杂度是 n的平方
#我的答案特点是 只用遍历一遍 O(n) 就可以得出最终结果 
S ='acebbeca'
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
