# 큰따옴표로 양쪽 둘러싸기
print("Hello World")
print("--------------------")

# 작은따옴표로 양쪽 둘러싸기
print('Python is fun')
print("--------------------")

# 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")
print("--------------------")

# 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')
print("--------------------")

# 문자열에 작은따옴표 포함하기
# food = 'Python's favorite food is perl' 에러코드
# print(food)
print("에러코드 예시 작은따옴표")
print("--------------------")

# 문자열에 큰따옴표 포함하기
say = '"Python is very easy." he says.'
print(say)
print("--------------------")

# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")
print("--------------------")

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
print("Life is too short\nYou need python")
print("--------------------")

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
mult = '''
Life is too short 
You need python '''
print(mult)
mult2 = """
Life is too short 
You need python """
print(mult2)
print("--------------------")

# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head+tail)
print("--------------------")

# 문자열 곱하기
a = "python"
print(a*2)
print("--------------------")

# 문자열 곱하기를 응용하기
print("=" * 50)
print("My Program")
print("=" * 50)
print("--------------------")


# 문자열 길이 구하기
print(len("Life is too short")) 
print("--------------------")

# 문자열 인덱싱
a1 = "Life is too short, You need Python"
print(a1[3])
print("--------------------")

# 문자열 인덱싱 활용하기
print(a1[0])
print(a1[12])
print(a1[-1])

print(a1[-0])
print(a1[-2])
print(a1[-5])
print("--------------------")

# 문자열 슬라이싱
print(a1[0:4])
print(a1[0:3])
print("--------------------")

# 문자열을 슬라이싱하는 방법
print(a1[0:5])
print(a1[0:2])
print(a1[5:7])
print(a1[12:17])
print(a1[:17])
print(a1[:])
print(a1[19:-7])
print("--------------------")

# 슬라이싱으로 문자열 나누기
b = "20230331Rainy"
data = b[:8]
weather = b[8:]
print(data)
print(weather)
year = b[:4]
day = b[4:8]
weather = b[8:]
print(year)
print(day)
print(weather)
print("--------------------")


# 숫자 바로 대입
print("I eat %d apples." % 3)
print("--------------------")

# 문자열 바로 대입
print("I eat %s apples." % "five")
print("--------------------")

# 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)
print("--------------------")

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("--------------------")


# 문자열  포맷 코드
print("I have %s apples" % 3)
print("rate is %s" % 3.234)
print("--------------------")



# 정렬과 공백
print("%10s" % "hi")
print("--------------------")

# 소수점 표현하기
print("%0.4f" % 3.42134234)
print("--------------------")


# 숫자 바로 대입하기
print("I eat {0} apples".format(3))
print("--------------------")

# 문자열 바로 대입하기
print("I eat {0} apples".format("five"))
print("--------------------")

# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))
print("--------------------")

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("--------------------")

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("--------------------")

# 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print("--------------------")

# 왼쪽 정렬
print("{0:<10}".format("hi"))
print("--------------------")

# 오른쪽 정렬
print("{0:>10}".format("hi"))
print("--------------------")

# 가운데 정렬
print("{0:^10}".format("hi"))
print("--------------------")

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("--------------------")

#소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("--------------------")

# { 또는 } 문자 표현하기
print("{{ and }}".format())
print("--------------------")

# f 문자열 포맷팅
name='홍길동'
age=30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print("--------------------")


# 문자 개수 세기 - count
a = "hobby"
print(a.count('b'))
print("--------------------")

# 위치 알려 주기 1 - find
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

print("--------------------")

# 위치 알려 주기 2 - index
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) 에러코드 
print("--------------------")

# 문자열 삽입 - join
print(",".join('abcd'))
print("--------------------")

# 소문자를 대문자로 바꾸기 - upper
a = "hi"
print(a.upper())
print("--------------------")

# 대문자를 소문자로 바꾸기 - lower
a = "HI"
print(a.lower())
print("--------------------")

# 왼쪽 공백 지우기 - lstrip
a = " hi "
print(a.lstrip())
print("--------------------")

# 오른쪽 공백 지우기 - rstrip
print(a.rstrip())
print("--------------------")

# 양쪽 공백 지우기 - strip
print(a.strip())
print("--------------------")

# 문자열 바꾸기 - replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))
print("--------------------")

# 문자열 나누기 - split
a = "Life is too short"
print(a.split())
print("--------------------")