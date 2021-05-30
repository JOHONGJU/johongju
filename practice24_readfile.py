# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# #한줄한줄 열어서 표기하는 방식
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#몇줄일지 모를 때 
# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(linem, end=" "), #줄바꿈 안할려면 end 쓰면 됨 
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() #list형태로 저장 
for line in lines:
    print(line, end="")

score_file.close()


  