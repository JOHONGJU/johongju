#print("a" + "b")
#print("a", "b")

#방법 1
print("나는 %d살입니다." %20)
print("나는 %s을 좋아헤요." % "파이썬")
print("Apple 은 %c로 시작해요" % "A") #character -> 한글자만 받는다 

#방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color = "빨간"))

#방법4

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
