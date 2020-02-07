import wordcloud
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import imageio
import jieba
import os
from PIL import Image

window = tk.Tk()
#window.attributes("-fullscreen", True)
#窗口和图片的初始化大小
#SCR_WID=window.winfo_screenwidth()
#SCR_HET=window.winfo_screenheight()-100
SCR_WID=1024
SCR_HET=700

IMG_WID=1024
IMG_HET=768

def quit():
    res = messagebox.askyesno(message='Are you sure to exit?',icon='warning',title='Quit')
    if res == True:
        f = open("SperateWords.txt","w")
        txt=ent_9.get()
        f.write(txt)
        f.close()
        window.destroy()



def WC():
    moren=[1024,768,0,150,1,"simsun.ttf",200,"white",0,"",1]
    val=[]
    #Transfer the values to list
    val.append(int(ent_1.get()))  #[0]
    val.append(int(ent_2.get()))  #[1]
    val.append(int(ent_3.get()))  #ent_3 is the smallest font size 
    val.append(int(ent_4.get()))  #ent_4 is the largest font size
    val.append(int(ent_5.get()))  #ent_5 is font step
    val.append(int(ent_6.get()))  #[5]ent_6 is the max number of words
    val.append(ent_7.get())       #[6]ent_7 is color of background
    val.append(com_8.get())       #[7]com_8 is font name
    val.append(ent_9.get())       #[8]ent_9 is discard words separed by space
    val.append(mark.get())   #rad_10 is use image mask(0 is not, 1 is yes)    
    val.append(word.get())   #rad_11 is generate Wordcloud(0) or Sentense cloud(1)
    wc_content=ent_t.get("0.0", "end")
    val_sp=set(val[8].split(" ")) #val_sp分词的关键词
    print('val: ',val)
    print('val_sp: ',val_sp)
    print("fonts/"+val[7])
    
    if val[9] == 1:
        #imagepath = g.fileopenbox(title="选择模板图片")
        imagepath = "./img/moban.jpg"
        mk = imageio.imread(imagepath)
        c = wordcloud.WordCloud(width=val[0],height=val[1],\
                                min_font_size=val[2],max_font_size=val[3],font_step=val[4],\
                                max_words=val[5],background_color=val[6],\
                                font_path="fonts/"+val[7],mask=mk,stopwords=val_sp,\
                                prefer_horizontal=0.9,mode='RGBA',scale=2)
    else:
        c = wordcloud.WordCloud(width=val[0],height=val[1],\
                                min_font_size=val[2],max_font_size=val[3],font_step=val[4],\
                                max_words=val[5],background_color=val[6],\
                                font_path="fonts/"+val[7],stopwords=val_sp,\
                                prefer_horizontal=0.9,mode='RGBA',scale=2)

    if val[10] == 1:
        final_text = " ".join(jieba.lcut(wc_content))
    elif val[10] == 0:
        final_text = wc_content
    else:
        final_text = " ".join(jieba.lcut(wc_content))
    c.generate(final_text)
    c.to_file("temp.png")
    c.generate_from_text(final_text)
    c.to_file("temp_1.png")
    img_s = Image.open("temp.png")
    w,h=img_s.size
    rate=240/h
    out = img_s.resize((int(w*rate), int(h*rate)),Image.ANTIALIAS) #resize image with high-quality
    out.save("temp0.png", "png")
    img_png = tk.PhotoImage(file = 'temp0.png')
    can_r = tk.Label(window,image=img_png,\
                     width=500,height=240,bg='cornflowerblue')
    can_r.place(x=500,y=int((SCR_HET-50)/(12+1))+20+260,anchor='nw')
    window.mainloop()



#界面编写代码！！！
i=1
#X1为第一列控件的坐标
X1=330
window.title('词云制作程序——Tian@BISU')
window.geometry("%dx%d+0+0"%(SCR_WID, SCR_HET))

l = tk.Label(window, text='欢迎来到词云制作小程序！\n请将要分析的文本保存在text.txt文件中。\n', \
             justify='center', font=('Simsong', 16), width=50, height=3).place(x=int(SCR_WID/2),y=50,anchor='c')

#SCR_HET-50
#ent_1 is width,ent_2 is height
lab_1 = tk.Label(window, text='Width: ', font=('Arial', 14),justify = 'right',\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_1 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_1.insert(0, '1024')
ent_1.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_2 = tk.Label(window, text='Height: ', font=('Arial', 14),justify='right',\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_2 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_2.insert(0, '768')
ent_2.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

#ent_3 is the smallest font size, ent_4 is the largest, ent_5 is font step
i+=1
lab_3 = tk.Label(window, text='The smallest font size: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_3 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_3.insert(0, '1')
ent_3.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_4 = tk.Label(window, text='The largest font size: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_4 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_4.insert(0, '150')
ent_4.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_5 = tk.Label(window, text='The step of font change: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_5 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_5.insert(0, '1')
ent_5.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

#ent_6 is the max number of words, ent_7 is color of background, com_8 is font name
i+=1
lab_6 = tk.Label(window, text='The max number of words: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_6 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_6.insert(0, '200')
ent_6.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_7 = tk.Label(window, text='The color of background: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_7 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_7.insert(0, 'white')
ent_7.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_8 = tk.Label(window, text='The font name: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
number = tk.StringVar()
com_8 = ttk.Combobox(window, width= 8, textvariable=number, font=('Arial', 14), state='readonly')
#增加代码识别字体文件名！
font_files = os.listdir("fonts")
font_files.insert(0,'simsun.ttf')
com_8['value'] = (font_files)
com_8.current(0)
com_8.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

#ent_9 is discard words separed by space, rad_10 is use image mask(0 is not, 1 is yes)
#rad_11 is generate Wordcloud(1) or Sentense cloud(0).
#Read SperateWords from file
f = open("SperateWords.txt","r")
spew = f.read() 
f.close()

i+=1
lab_9 = tk.Label(window, text='Discard words separed by space: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
ent_9 = tk.Entry(window, show=None, font=('Arial', 14),width=10)
ent_9.insert(0, spew)
ent_9.place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_10 = tk.Label(window, text='Whether use the mask image: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
mark = tk.IntVar()
mark.set(0)
rad_10_1 = tk.Radiobutton(window, text="Yes", variable=mark, value=1, font=('Arial', 14))\
           .place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')
rad_10_1 = tk.Radiobutton(window, text="No", variable=mark, value=0, font=('Arial', 14))\
           .place(x=X1+90,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
lab_11 = tk.Label(window, text='Wordcloud or Sentence cloud: ', font=('Arial', 14),\
                 width=30, height=1).place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='ne')
word = tk.IntVar()
word.set(1)
rad_11_1 = tk.Radiobutton(window, text="Word", variable=word, value=1, font=('Arial', 14))\
           .place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')
rad_11_1 = tk.Radiobutton(window, text="Sentence", variable=word, value=0, font=('Arial', 14))\
           .place(x=X1+90,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

i+=1
but_12 = tk.Button(window, text="Exit",font=('Arial', 14), command=quit)\
         .place(x=X1,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')
but_13 = tk.Button(window, text="Gene Wordcloud",font=('Arial', 14), command=WC)\
         .place(x=X1+150,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')

#Read the text content from file
f = open("text.txt","r")
s = f.read() 
f.close()

#ent_t is analysis text input module, can_r use to show the result of image.
i=1
lab_t = tk.Label(window, text='请将文本粘贴到下面的文本框中: ', font=('Simsun.ttf', 14),\
                 ).place(x=500,y=int((SCR_HET-50)/(12+1)*i)+20,anchor='nw')
scroll = tk.Scrollbar()
scroll.pack(side=tk.RIGHT, fill=tk.Y)
scroll.place(x=1000,y=int((SCR_HET-50)/(12+1)*i)+45,anchor='nw',width=20,height=200)
ent_t = tk.Text(window, show=None, font=('Simsun.ttf', 12),background='cornflowerblue',yscrollcommand=scroll.set)
scroll.config(command = ent_t.yview)
ent_t.insert('insert',s)
ent_t.place(x=500,y=int((SCR_HET-50)/(12+1)*i)+45,anchor='nw', width=500,height=200)

lab_i = tk.Label(window, text='下面的输出结果是否满意？', font=('Simsun.ttf', 14),\
                 ).place(x=500,y=int((SCR_HET-50)/(12+1)*i)+20+230,anchor='nw')

img_s = Image.open("temp.png")
w,h=img_s.size
rate=240/h
out = img_s.resize((int(w*rate), int(h*rate)),Image.ANTIALIAS) #resize image with high-quality
out.save("temp0.png", "png")
img_png = tk.PhotoImage(file = 'temp0.png')
can_r = tk.Label(window,image=img_png,\
                      width=500,height=240,bg='cornflowerblue')
can_r.place(x=500,y=int((SCR_HET-50)/(12+1)*i)+20+260,anchor='nw')

window.mainloop()
