## Csv 파일 읽기 콘솔 출력 한줄씩 ##

# CookAnalysis 폴더 만들어서 그 안에 다운받은 CSV 넣기
inFp = open("C:/CookAnalysis/CSV/singer1.csv", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()