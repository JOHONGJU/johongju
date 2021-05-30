#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

print("{0: > 10}".format(500))

#양수일 땐 +, 음수일땐 - 표시

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸을 밑줄로 채움 

print("{0:_<+10}".format(500))

#3자리 마다 콤마 찍어줌

print("{0:,}".format(10000000000))

#3자리 마다 콤마 찍어줌+부호
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))

#3자리 마다 콤마 찍어줌+부호, 자리수확보,
#빈자리는 ^로 채워주기

print("{0:^<+30,}".format(10000000000)) #< : 왼쪽정렬 

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리수까지 표시 (소수점 3째 자리에서 반올림 표시)
print("{0:.2f}".format(5/3)) #소수점 두번째자리까지 표시 