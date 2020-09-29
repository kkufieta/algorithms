import unittest

def string_compression(s):
    if len(s) < 2:
        return s

    a = []
    i = 0
    current_letter = s[0]
    count = 0
    while i < len(s):
        if len(a) > 0 and len(a) >= i:
            return s
        if s[i] == current_letter:
            count += 1
        else:
            a.append(current_letter)
            a.extend(str(count).split())
            current_letter = s[i]
            count = 0
        i += 1
    if len(a) == 0:
        a = [current_letter]
        a.extend(str(count).split())
    if len(a) == len(s):
        return s
    else:
        return ''.join(a)

if __name__ == '__main__':
    print("'': ", string_compression(''))
    print("'a': ",string_compression('a'))
    print("'ab': ", string_compression('ab'))
    print("'aa': ", string_compression('aa'))
    print("'aabbcccccaa': ", string_compression('aabbcccccaa'))
    unittest.main()
