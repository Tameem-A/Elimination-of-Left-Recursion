import os
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tf

var1 = ""
var2 = {" Non left recursive grammar "}
var3 = ""
var4 = ""

window = tk.Tk()
window.title(' Eliminate left recursion ')
window.minsize(500, 500)


# The converted coordinates are displayed as tuples
def getIndex(text, pos):
    return tuple(map(int, str.split(text.index(pos), ".")))


def func(x, y):
    if not len(y):
        pass
    else:
        if x == y[0]:
            var2.discard(" Non left recursive grammar ")
            # Handle direct left recursion
            word1 = y.split('|')
            word2 = []
            word3 = []
            for item in word1:
                if x in item:
                    item = item[1:]
                    textt = str(item) + str(x) + "'"
                    word2.append(textt)
                else:
                    text = str(item) + str(x) + "'"
                    word3.append(text)
            if not word3:  # Handle A -> Ax The situation of
                word3.append(str(x + "'"))
            str1 = str(x) + " -> " + "|".join(word3)
            str2 = str(x) + "'" + " -> " + "|".join(word2) + "|є"
            text_output.insert('insert', ' Direct left recursive grammar ', 'tag1')
            text_output.insert('insert', '\n')
            text_output.insert('insert', str1, 'tag2')
            text_output.insert('insert', '\n')
            text_output.insert('insert', str2, 'tag2')
        '''  In addition, it will judge the output of non recursive production , However, it will lead to indirect left recursion and cannot delete redundant production  else: h =" unchanged ： " + x + " -> " + y text_output.insert('insert',' Non left recursive grammar ','tag1') text_output.insert('insert','\n') text_output.insert('insert',h,'tag2') '''
        text_output.insert('insert', '\n')


def func2(x, y):
    if not len(y):
        pass
    else:
        if x == y[0]:
            var2.discard(" Non left recursive grammar ")
            # Handle direct left recursion
            word1 = y.split('|')
            word2 = []
            word3 = []
            for item in word1:
                if x in item:
                    item = item[1:]
                    textt = str(item) + str(x) + "'"
                    word2.append(textt)
                else:
                    text = str(item) + str(x) + "'"
                    word3.append(text)
            str1 = str(x) + " -> " + "|".join(word3)
            str2 = str(x) + "'" + " -> " + "|".join(word2) + "|є"
            text_output.insert('insert', " Indirect left recursive grammar ", 'tag1')
            text_output.insert('insert', '\n')
            text_output.insert('insert', str1, 'tag2')
            text_output.insert('insert', '\n')
            text_output.insert('insert', str2, 'tag2')

        text_output.insert('insert', '\n')


def func2(xk, yi, yk):
    s1 = []
    s2 = []
    s3 = ""
    s4 = ""
    s5 = ""
    s6 = []
    if xk in yi:
        word4 = yk.split('|')
        word5 = yi.split('|')  # Separate non terminality from non terminality
        for ba in word5:
            if xk in ba:
                s1.append(ba)
            else:
                s2.append(ba)

        s3 = "|".join(s1)

        for item in word4:
            s5 = s3.replace(xk, item)  # Replace
            s6.append(s5)
        s4 = "|".join(s2)  # Re merger
        global var1
        var1 = "|".join(s6) + "|" + s4


# The function executed after clicking the button
def changeString():
    text_output.delete('1.0', 'end')
    text = text_input.get('1.0', 'end')
    text_list = list(text.split('\n'))  # Line by line grammar
    text_list.pop()
    if not text_list[0]:
        print(tkinter.messagebox.showerror(title=' Something went wrong ！', message=' Input cannot be empty '))
    else:
        for cfg in text_list:

            x, y = cfg.split('->')  # Separate grammar from left and right
            x = ''.join(x.split())  # Eliminate spaces
            y = ''.join(y.split())
            if not (len(x) == 1 and x >= 'A' and x <= 'Z'):
                pos = text_input.search(x, '1.0', stopindex="end")
                result = tkinter.messagebox.showerror(title=' Something went wrong ！',
                                                      message=' Non context free grammar ! coordinate %s' % (
                                                      getIndex(text_input, pos),))
                #  The return value is ：ok
                print(result)
                return 0
            else:
                func(x, y)

        for i in range(len(text_list)):
            for k in range(i):
                xi, yi = text_list[i].split('->')
                xi = ''.join(xi.split())  # Eliminate spaces
                yi = ''.join(yi.split())

                xk, yk = text_list[k].split('->')
                xk = ''.join(xk.split())  # Eliminate spaces
                yk = ''.join(yk.split())

                func2(xk, yi, yk)
                func2(xk, var1, yk)
                global var3
                var3 = xi
        func2(var3, var1)

        for item in var2:
            text_output.insert('insert', item, 'tag1')

        # Create text input boxes and buttons


text_input = tk.Text(window, width=80, height=16)
text_output = tk.Text(window, width=80, height=20)
# Simple style
ft = tf.Font(family=' Microsoft YaHei ', size=12)
text_output.tag_config("tag1", background="yellow", foreground="red", font=ft)
text_output.tag_config('tag2', font=ft)
# Button
button = tk.Button(window, text=" Eliminate left recursion ", command=changeString, padx=32, pady=4, bd=4)

text_input.pack()
text_output.pack()
button.pack()
window.mainloop()
