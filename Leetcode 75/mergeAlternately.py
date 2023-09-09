list1 = "abc"
list2 = "ggggggg"


def merge(list1:str, list2:str):
    pointer = min(len(list1), len(list2))
    ans = "".join(list1[i]+list2[i] for i in range(0, pointer))
    ans += list1[pointer:]
    ans += list2[pointer:]
    return ans

print(merge(list1, list2))