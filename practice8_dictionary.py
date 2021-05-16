cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5))

#print(cabinet[5])   #오류 뜸
print(cabinet.get(5)) #none이라고 출력가능함
print(cabinet.get(5, "사용가능"))
print("hi")


print(3 in cabinet)  #key in 변수 3이라는 key가 cabinet에 있으면 -> true
print(5 in cabinet) #false 


cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#손님 감
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)