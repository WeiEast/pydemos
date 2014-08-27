from PyQt5.uic import compileUi
with open('untitled.ui', encoding='utf-8')as f:
    with open('qtui.py', 'w', encoding='utf-8') as ff:
        compileUi(f, ff)
