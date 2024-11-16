def inneholder(str1, str2):
    chars = set()
    for c in str2:
        chars.add(c)

    for c in str1:
        if c not in chars:
            return False

    chars2 = {}
    for c in str2:
        if c not in chars2:
            chars2[c] = 1
        else:
            chars2[c] += 1

    chars1 = {}
    for c in str1:
        if c not in chars1:
            chars1[c] = 1
        else:
            chars1[c] += 1

    for c in chars1:
        if not chars1[c] <= chars2[c]:
            return False

    return True


def anagram(str1, str2):
    l1 = []
    l2 = []

    for c in str1:
        l1.append(c)
    for c in str2:
        l2.insert(0, c)

    if l1 == l2:
        return True
    else:
        return False




input1 = input()
input2 = input()

print(inneholder(input1, input2))
print(anagram(input1, input2))
