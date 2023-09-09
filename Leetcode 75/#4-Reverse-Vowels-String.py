string1 = "hello"
string2 = "leetcode"

def reverse_vowels(s:str):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)
    left, right = 0, len(s)-1
    while left < right:
        if s[left] in vowels:
            while s[right] not in vowels and left <= right:right -= 1
            s[left], s[right] = s[right], s[left]
        left += 1
    return "".join(s)

print(reverse_vowels(string1))
print(reverse_vowels(string2))
