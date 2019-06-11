#いろいろインポート
import tkinter as tk
from mutagen.mp3 import MP3 as mp3
import pygame
import time

from tkinter import messagebox as mbox

# ウィンドウを作成 
win = tk.Tk()
win.geometry("700x650") # サイズ指定

# OKボタンを押した時
def ok_click():

    filename = 'alert.mp3' #再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename) 
    mp3_length = mp3(filename).info.length 
    pygame.mixer.music.play(-1) #再生開始。-1の部分を変えるとn回再生(この時は無限ループになっている。)
    time.sleep(mp3_length -1) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
 
    endButton.when_pressed = lambda: any(s.stop() for s in (filename))

# ボタンを作成 ---
alertButton = tk.Button(win, text='OK', command=ok_click)
alertButton.pack()

endButton = tk.Button(win, text='stop')
endButton.pack()


                    # ウィンドウを動かす
win.mainloop()
