# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
s = input()
sub1, sub2 = s.split(',')

print(len(sub1) > len(sub2))
print(sub1 == sub2)
print(sub2 in sub1)
# ---------- ЗАДАНИЕ 2 ----------
def task1(s):
    s = input()

print(s.strip())
print(len(s))
print(s.count('a'))
print(s.replace('a', '@'))
print(s.istitle())

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
   s = input()

print(s[1:-1])
print(s[::2])
print(s.lower()[::-1])

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    numbers = list(map(int, input().split()))

print(sorted(numbers))
print(sum(numbers))
print(min(numbers), max(numbers))


# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    s = input()

# Проверяем оба условия одновременно с помощью and
result = s.lower() == s.lower()[::-1] and ' ' not in s
print(result)
# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    n = int(input())
hex_str = hex(n)[2:]  # Убираем префикс '0x'

print(hex_str)
print(len(hex_str))
print('a' in hex_str)
# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

n = int(input())
print(months[n-1])
