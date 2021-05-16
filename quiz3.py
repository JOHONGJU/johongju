# print("http://naver.com")
# print("http://\b\b\b\b\b\b\bnaver.com")

url = "http://naver.com"
my_str = url.replace("http://", " ") #규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] #my_str[0:5] -> 0~5직전까지
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{} 의 비밀번호는 {} 입니다.".format(url,password))


#다시해보기 
