## 자동 닫기, with ##

with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :

    inStr = inFp.readline()
    print(inStr, end = "")

    inStr = inFp.readline()
    print(inStr, end = "")
