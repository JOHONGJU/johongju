def std_weight(height, gender): #키 = m단위(실수), gender = "남자"/"여자"
    if gender == "남자":
        return  height * height * 22 
    else :
        return height * height * 21
 
height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height/ 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height, gender, weight))




