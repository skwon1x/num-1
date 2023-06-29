def is_palindrome(num_2):
    num_1 = len(num_2)
    for i in range(num_1 // 2):
        if num_2[i] != num_2[num_1 - i - 1]:
            return False
    return True

s1 = str(input('Введите слово:'))
s2 = str(input('Введите слово:'))

print(is_palindrome(s1)) 
print(is_palindrome(s2))
