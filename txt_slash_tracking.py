# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

#%%
# 슬래시 기호 위치 추적하여 같은 위치에 슬래시 추가하기

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

# // 기호 파일 열기
def open_origin():
    global origin_file
    origin_file = filedialog.askopenfilename(parent = window, initialdir = './', title = 'Select Script',
                                             filetypes = [('Text files', '*.txt')])

# 적용할 파일 열기
def open_convert():
    global convert_file
    convert_file = filedialog.askopenfilename(parent = window, initialdir = './', title = 'Select Script',
                                              filetypes = [('Text files', '*.txt')])

# 변환 시작
def start():
    if (origin_file != '' and convert_file != ''):
        convert_list = []
        with open(origin_file, encoding = 'utf-8') as rf1, open(convert_file, encoding = 'utf-8') as rf2:
            for line1, line2 in zip(rf1, rf2):
                start_index = 0

                # 한 라인의 // 개수만큼 처리
                for _ in range(line1.count('//')):
                    start_index = line1.find('//', start_index, -1)
                    line2 = line2[:start_index] + '//' + line2[start_index:]
                    start_index += 1
                
                # 두 라인의 길이가 다르면 실패로 간주
                if (len(line1) == len(line2)):
                    print(f'line:{line1[:5]} OK!')
                else:
                    print(f'line:{line1[:5]} Fail!')

                # 변환된 라인 추가
                convert_list.append(line2)

        # 변환된 파일 저장
        if (len(convert_list)):
            with open(convert_file, 'w', encoding = 'utf-8') as wf1:
                wf1.writelines(convert_list)

window = tk.Tk()
window.title('슬래시 기호 위치 추적')

origin_file = ''
convert_file = ''

ttk.Button(window, text = ' // 기호 파일 호출 ', width = 20, command = open_origin).grid(row = 0, column = 0, padx = 5, pady = 5)
ttk.Button(window, text = ' 적용할 파일 호출 ', width = 20, command = open_convert).grid(row = 0, column = 1,padx = 5, pady = 5)
ttk.Button(window, text = ' 시작 ', command = start).grid(row = 0, column = 2, padx = 5, pady = 5)

window.mainloop()
