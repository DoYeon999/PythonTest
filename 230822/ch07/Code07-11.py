## Gif 읽기, 각 RGB 값 출력 ##

from tkinter import *

window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()
print('이미지 크기 : ', h, 'x', w)

photoR=[ [0 for _ in range(h)] for _ in range(w)]
print(f"photoR 의 값 : {photoR}")
photoG=[ [0 for _ in range(h)] for _ in range(w)]
print(f"photoG 의 값 : {photoG}")
photoB=[ [0 for _ in range(h)] for _ in range(w)]
print(f"photoB 의 값 : {photoB}")

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

print('[50][50] 위치의 RGB 값 : ', photoR[50][50], photoG[50][50], photoB[50][50] )
