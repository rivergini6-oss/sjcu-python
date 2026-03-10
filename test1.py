#새로운 파일에 데이터 쓰기
file=open("test.txt","w")
for data in range(1,11):
    file.write(f'{data} line');
file.close()

#기록한 데이터 읽기
file=open("test.txt","r")
while True:
    line=file.readline()
    if not line:
        break
    print(line)
file.close

#이미 존재하는 파일에 데이터 추가하기
file = open("test.txt", "a")
for data in range(1,11):
    file.write(f'{data} line\n');
file.close() 
