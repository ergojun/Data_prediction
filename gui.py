from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from  tkinter.filedialog import askopenfilename
import tkinter.messagebox
import joblib
import pymysql
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn import svm

root = Tk()
root.title("Panedwindow测试")
root.geometry("1000x600")

# 首先设置一个父Panedwindow p ，orient：控件排序方向，horizontal:水平方向
p = PanedWindow(root, orient=HORIZONTAL)
p.pack(fill=BOTH, expand=YES)

# 再添加一个子 panedwindow ，布局方向是垂直的。
# 为了添加两个垂直分布的标签：左上，左下
p1 = PanedWindow(p, orient=VERTICAL)
# 在父 panedwindow 添加子panedwindow p1
p.add(p1)

# 添加左上标签窗口
top = LabelFrame(p1, text='左上')
p1.add(top)

# 再窗口里添加一个窗口
scro = ScrolledText(top, state=DISABLED, width=110, height=30)
scro.pack(fill=BOTH, expand=YES)
frame = Frame(scro, width=800, height=430, bg='white')
frame.pack()
scro.window_create(INSERT, window=frame)

# 输入框
var_id = StringVar()
var_id.set('')
var_na = StringVar()
var_na.set('')
# ID,Name
label_id = Label(frame, text='ID:', width=10, bg='white')
label_id.place(x=-25, y=40)

entry_id = Entry(frame, width=10,textvariable=var_id)
entry_id.place(x=10,y=70)

label_n = Label(frame, text='Name:', width=10, bg='white')
label_n.place(x=-17, y=110)
entry_n = Entry(frame, width=10, textvariable=var_na)
entry_n.place(x=10, y=140)



#生成20个var i =StringVar()
# var i =set('')
for i in range(21):
    locals()['var'+str(i)]=StringVar()
for i in range(21):
    locals()['var'+str(i)].set('')


filds=['Gn起始量','HCG_E2','HCG用量','HCG卵泡数','左侧卵子数','右侧卵子数','获卵数','成熟卵子','受精','正常受精']
fildss=['正常卵裂','正常卵裂率','冷冻','可利用胚胎','优质胚胎','囊胚培养数','囊胚形成数','移植胚胎数','移植胚胎形态1','移植胚胎形态2']
for fd,i in zip(filds,range(10)):

    lab = Label(frame,width=10,text=fd,bg='white')
    ent = Entry(frame,width=15,textvariable=locals()['var'+str(i)])
    lab.place(x=200,y=i*40+10)
    ent.place(x=300,y=i*40+10)


for fds,k,l in zip(fildss,range(10,20),range(20)):

    lab1 = Label(frame,width=11,text=fds,bg='white')
    ent1 = Entry(frame,width=15,textvariable=locals()['var'+str(k)])
    lab1.place(x=450,y=l*40+10)
    ent1.place(x=540,y=l*40+10)

'''
def cont():

    #生成 get()方法
    for ii in range(2):
        #name1= 'get_entry'+str(ii)
        locals()['data'+str(ii)]=locals()['var'+str(ii)].get()
'''
def clean():
        var_id.set('')
        var_na.set('')
        var0.set('')
        var1.set('')
        var2.set('')
        var3.set('')
        var4.set('')
        var5.set('')
        var6.set('')
        var7.set('')
        var8.set('')
        var9.set('')
        var10.set('')
        var11.set('')
        var12.set('')
        var13.set('')
        var14.set('')
        var15.set('')
        var16.set('')
        var17.set('')
        var18.set('')
        var19.set('')
def cont():

    data0 = var0.get()
    data1 = var1.get()
    data2 = var2.get()
    data3 = var3.get()
    data4 = var4.get()
    data5 = var5.get()
    data6 = var6.get()
    data7 = var7.get()
    data8 = var8.get()
    data9 = var9.get()
    data10 = var10.get()
    data11 = var11.get()
    data12 = var12.get()
    data13 = var13.get()
    data14 = var14.get()
    data15 = var15.get()
    data16 = var16.get()
    data17 = var17.get()
    data18 = var18.get()
    data19 = var19.get()
    data20 = var20.get()
    data_id=var_id.get()
    data_na=var_na.get()
    data=[[data0,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14
        ,data15,data16,data17,data18,data19]]

    X=data
    #选择一个模型
    model_chooes=var.get()
    if model_chooes=='0.77':
        clf=joblib.load("0.7700170357751278.model")
    elif model_chooes=='0.75':
        clf=joblib.load("0.7597955706984668.model")
    elif model_chooes=='0.73':
        clf=joblib.load("0.7359454855195912.model")
    elif model_chooes=='其他':
        f = askopenfilename()
        clf=joblib.load(f)

    new_pre=clf.predict(X)
    print('预测结果：')
    print(new_pre)
    print('样本分类的概率：',clf.predict_proba(X))
    resul=clf.predict_proba(X)[:,1]
    print(resul)
    re=resul[0]
    print(re)

    print(clf)
    #连接数据库
    conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='predata',
            port=3306,
            charset='utf8'
            )
    # 获得游标
    cur = conn.cursor()
    # 创建插入SQL语句
    query = 'insert into train_data (Gn起始量,HCG日E2,HCG用量,HCG卵泡数,左侧卵子数,右侧卵子数,获卵数,成熟卵子,受精,正常受精,正常卵裂,正常卵裂率,冷冻,可利用胚胎,优质胚胎,囊胚培养数,囊胚形成数,移植胚胎数,移植胚胎形态1,移植胚胎形态2,妊娠概率) values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s,%s,%s)'
    Gn起始量 = X[0][0]
    HCG日E2 = X[0][1]
    HCG用量 = X[0][2]
    HCG卵泡数 = X[0][3]
    左侧卵子数 = X[0][4]
    右侧卵子数 = X[0][5]
    获卵数 = X[0][6]
    成熟卵子 = X[0][7]
    受精 = X[0][8]
    正常受精 = X[0][9]
    正常卵裂 = X[0][10]
    正常卵裂率 = X[0][11]
    冷冻 = X[0][12]
    可利用胚胎 = X[0][13]
    优质胚胎 = X[0][14]
    囊胚培养数 = X[0][15]
    囊胚形成数 = X[0][16]
    移植胚胎数 = X[0][17]
    移植胚胎形态1 = X[0][18]
    移植胚胎形态2 = X[0][19]
    妊娠概率=float(re)
    values = (Gn起始量,HCG日E2,HCG用量,HCG卵泡数,左侧卵子数,右侧卵子数,获卵数,成熟卵子,受精,正常受精,正常卵裂,正常卵裂率,冷冻,可利用胚胎,优质胚胎,囊胚培养数,囊胚形成数,移植胚胎数,移植胚胎形态1,移植胚胎形态2,妊娠概率)
    cur.execute(query, values)
    cur.close()
    conn.commit()
    conn.close()
    rows = str(len(X))
    scro.config(state=NORMAL)
    scro.insert(END,'评估结果---成功率为： %s\n'%(re))
    scro.insert(END,"成功添加 "  + rows + " 行数据到MySQL数据库!\n")
    #打印提示
    askprint=tkinter.messagebox.askokcancel(title='评估结果',
                                            message='Id= %s\n\n'
                                                    'Name= %s\n\n'
                                                    '妊娠成功率为  %s\n\n'
                                                    '是否打印？\n'
                                                    %(data_id,data_na,妊娠概率))
    if askprint :
        clean()
        scro.insert(END,'打印中。。。\n')

        print("打印中。。。。")
    scro.config(state=DISABLED)


#添加左下标签窗口
bt=LabelFrame(p1,text='左下',width=200,height=150)
p1.add(bt)
#在LabelFrame里加一个滚动文本框
scro = ScrolledText(bt)
scro.config(spacing1=10)
scro.pack(fill=BOTH,expand=YES)

'''
#给这个显示框加一个滚动条
scro = Scrollbar(bt)
scro.pack(side=RIGHT,fill=Y)
#添加一个多文本框到LableFrame里
text = Text(bt,yscrollcommand=scro.set)
text.pack(fill=BOTH,expand=YES)
scro.config(command=text.yview)
'''
#在父窗口的右边再加一个 右标签
right_lf=LabelFrame(p,text='右边',width=200,height=600)
p.add(right_lf)
#显示框

label_name=['ID：','Name：']

for label,m in zip(label_name,range(3)):
    lab2=Label(right_lf,text=label,width=8)
    lab2.place(x=10,y=m*30)
label_id=Label(right_lf,textvariable=var_id)
label_id.place(x=70,y=0)
label_na=Label(right_lf,textvariable=var_na)
label_na.place(x=70,y=30)
label_proba=Label(right_lf)
label_proba.place(x=70,y=60)

#选择模型
var=StringVar()
var.set('0.77')
op=OptionMenu(right_lf,var,'0.77','0.75','0.73','其他')
op.place(relx=0.4,rely=0.6,y=-50)

pre_btn=Button(right_lf,text='评估',width=10,command=cont)
pre_btn.place(relx=0.4,rely=0.6)

save_btn=Button(right_lf,text='清空',width=10,command=clean)
save_btn.place(relx=0.4,rely=0.7)

root.mainloop()



