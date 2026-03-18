#int()정수, float()실수, str()문자열 변환,
##%s문자열 출력,%d정수형 숫자,%f실수형 숫자출력
variable=input()
print("input string %s, int %d" % (variable, float(variable)))

#문자열 테스트
variable=input("안녕하세요")
print()

#연습
variable=1234
print(variable)

variable=1.234E2
print(variable)

variable=1.234e-2
print(variable)

variable=0x1f
print(variable)

variable=3/4
print(variable)

#2에 3승
variable=2**3
print(variable)

#나누기의 나머지값
variable=5%2
print(variable)

#나누기의 몫
variable=5//2
print(variable)

#나누기 값
variable=5/2
print(variable)

# 문자열 데이터 포맷팅
variable="%d books" % 3
print(variable)

variable="%s books"%"5신나고 재미있는"
print(variable)

#Format 함수 이용
variable="I have {0}{1}".format(3,"books")
print(variable)

variable="I have {0}{1}".format(5, "cars")
print(variable)

#f문자열 포맷팅 이용
number=3
variable=f'I have {number+3}books'
print(variable)















