import sys

#print("python", "Java", "Javascript", sep=" cs ", end="?")
print("python", "Java", file=sys.stdout) #표준출력
print("python", "Java", file=sys.stderr) #표준에러  

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ",") #왼쪽으로 8칸 확보하고 정렬


#은행대기순번표

#001, 002, 003 

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + str(answer) +   "입니다.")




