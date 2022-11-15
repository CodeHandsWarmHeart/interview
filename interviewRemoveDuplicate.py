#题目大概是 输入abbaca 去掉连续重复的字母 第一步去掉a'bb'aca 中的bb, 得到aaca, 还是去掉重复的字母 即'aa'ca中的aa 得到最终结果 ca
#耗时的算法需要遍历一遍后 多次反复遍历已得结果， 时间复杂度是 n的平方
#我的答案特点是 只用遍历一遍 O(n) 就可以得出最终结果, 通过动态规划，
#依然是新创建一个数组 命名new_s， 把当前已有的不重复字母存在其中(注意new_s中最后一个字母是否保留是待定的）
#举例 aebbe  两种特殊情况 1 啥也没有时来了一个字母， 则直接把它加进待选结果new_s; 2 当处理到最后一个字母时 要确定把new_s的末位敲定
     #先是 处理a -> 符合特殊情况1 -> 暂时存入new_s末尾, 结果是 new_s=[a]
     #处理e -> 因为与new_s末位不同 -> 暂时存入new_s末尾  结果是 new_s=[a,e]
     #处理b -> 因为与new_s末位不同 -> 暂时存入new_s末尾  结果是 new_s=[a,e,b] 
     #处理b -> 因为与new_s末位相同 -> 不存入new_s 并记录此处为第i个连续重复字母  结果是 new_s=[a,e,b] 且 duplicateFoundCount ++
#关键 处理e -> 因为与new_s末位不同 并且 duplicateFoundCount>0 -> 去掉new_s的末位 更新为 new_s=[a,e] 且 再次对比正在处理的字母e 与更新后的new_s末位
#                            解释一下 正上方这个值大于零 意味着之前存在连续字母 连续字母为 new_s的末位 
#所有逻辑和特殊情况都在代码里 就不多举例了
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
