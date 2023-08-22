## Csv 읽기, 헤더 부분 분리해서 추가 ##

def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)