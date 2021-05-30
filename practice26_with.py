# import pickle 

# with open("profile.pickle", "rb") as profile_file: #rb=read binary
#     print(pickle.load(profile_file))


#with문 탈출하면서 자동으로 종료됨

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요") as

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())


