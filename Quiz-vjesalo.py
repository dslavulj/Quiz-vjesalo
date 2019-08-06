from tkinter import*
from tkinter import ttk
from random import*


def main():
    x=start()
    if x!=0:
        major(x)


def halp():
    hlp = Tk()
    hlp.title('Help')
    hlp.geometry('500x150')
    tc1=Label(hlp,text='Program zadaje nepoznatu riječ.',font=("Helvetica", 9))
    tc1.place(x=10,y=10)
    tc2=Label(hlp,text='Igrač pogađa zadanu riječ upisivanjem malog slova hrvatske abecede i pritiskom entera.',font=("Helvetica", 9))
    tc2.place(x=10,y=30)
    tc3=Label(hlp,text='Broj pogodaka je duplo veći od različitih slova u riječi.',font=("Helvetica", 9))
    tc3.place(x=10,y=50)
    tc4=Label(hlp,text='Ne ubrajaju se neprihvatljivi znaci i već utipkana slova.',font=("Helvetica", 9))
    tc4.place(x=10,y=70)
    def closeh():
        hlp.destroy()
    bc= ttk.Button(hlp, text = 'OK', command=closeh)
    bc.pack(side='bottom')
    hlp.mainloop()

    
def about():
    abo = Tk()
    abo.title('O meni')
    abo.geometry('300x150')
    td1=Label(abo,text='Ime i prezime: Danijel Slavulj',font=("Helvetica", 9))
    td1.place(x=10,y=10)
    td2=Label(abo,text='Kontakt telefon: x',font=("Helvetica", 9))
    td2.place(x=10,y=30)
    td3=Label(abo,text='Kontakt email: danijel.slavulj@gmail.com',font=("Helvetica", 9))
    td3.place(x=10,y=50)
    def closea():
        abo.destroy()
    bd= ttk.Button(abo, text = 'OK', command=closea)
    bd.pack(side='bottom')
    abo.mainloop()


def start():
    pocetni = Tk()
    pocetni.title('Odabir')
    pocetni.geometry('210x330')
    ta=Label(pocetni, text = 'Odaberite temu',font=("Helvetica", 20))
    ta.pack(fill=X)
    global x
    def button1():
        global x
        x=1
        pocetni.destroy()
    def button2():
        global x
        x=2
        pocetni.destroy()
    def button3():
        global x
        x=3
        pocetni.destroy()
    def button4():
        global x
        x=4
        pocetni.destroy()
    def button5():
        global x
        x=5
        pocetni.destroy()
    def button6():
        global x
        x=6
        pocetni.destroy()
    def button7():
        global x
        x=7
        pocetni.destroy()
    def button8():
        global x
        x=8
        pocetni.destroy()
    def button9():
        global x
        x=9
        pocetni.destroy()
    def button10():
        global x
        x=10
        pocetni.destroy()
    ba1= ttk.Button(pocetni, text = 'Matematika', command=button1)
    ba1.place(x = 10, y = 75)
    ba2= ttk.Button(pocetni, text = 'Fizika', command=button2)
    ba2.place(x = 10, y = 125)
    ba3= ttk.Button(pocetni, text = 'Kemija', command=button3)
    ba3.place(x = 10, y = 175)
    ba4= ttk.Button(pocetni, text = 'Biologija', command=button4)
    ba4.place(x = 10, y = 225)
    ba5= ttk.Button(pocetni, text = 'Tjelesni', command=button5)
    ba5.place(x = 10, y = 275)
    ba6= ttk.Button(pocetni, text = 'Povijest', command=button6)
    ba6.place(x = 125, y = 75)
    ba7= ttk.Button(pocetni, text = 'Hrvatski', command=button7)
    ba7.place(x = 125, y = 125)
    ba8= ttk.Button(pocetni, text = 'Geografija', command=button8)
    ba8.place(x = 125, y = 175)
    ba9= ttk.Button(pocetni, text = 'Sociologija', command=button9)
    ba9.place(x = 125, y = 225)
    ba10= ttk.Button(pocetni, text = 'Logika', command=button10)
    ba10.place(x = 125, y = 275)
    pocetni.protocol('WM_DELETE_WINDOW', exit)

    menubar = Menu(pocetni)
    menubar.add_command(label="Help", command=halp)
    menubar.add_command(label="About", command=about)
    menubar.add_command(label="Quit", command=exit)
    pocetni.config(menu=menubar)
    
    pocetni.mainloop()
    return x


def major(x):
    glavni = Tk()
    glavni.title('Pogadanje')
    glavni.geometry('800x300')
    glavni.protocol('WM_DELETE_WINDOW', exit)
    def tema(x):
        if x==1:
            l=['broj','funkcija','krug','hiperbola','četverokut','trokut']
        elif x==2:
            l=['frekvencija','amplituda','energija','otpor','sila','zvuk']
        elif x==3:
            l=['metal','atom','aluminij','bakar','elektroliza','elektron']
        elif x==4:
            l=['bolest','čovjek','biljka','životinja','adrenalin','hormon']
        elif x==5:
            l=['sklekovi','trbušnjaci','oprema','trčanje','razgibavanje','lopta']
        elif x==6:
            l=['bitka','godina','teritorij','država','plemstvo','feudalizam']
        elif x==7:
            l=['aorist','romantizam', 'predikat', 'glagoljica','objekt','nominativ']
        elif x==8:
            l=['europa','beltovi','marikultura','planine','klif','polje']
        elif x==9:
            l=['društvo','kultura','simbol','norme','rituali','vrijednosti']
        elif x==10:
            l=['pojam','opseg','sadržaj','sud','zaključak','konjunkcija']
        a=randint(0,5)
        t=l[a]
        return t
    def ispis(x,t):
        if x==1:
            tb=Label(glavni, text = '{}'.format('Tema: Matematika') ,font=("Helvetica", 20))
        elif x==2:
            tb=Label(glavni, text = '{}'.format('Tema: Fizika'),font=("Helvetica", 20))
        elif x==3:
            tb=Label(glavni, text = '{}'.format('Tema: Kemija'),font=("Helvetica", 20))
        elif x==4:
            tb=Label(glavni, text = '{}'.format('Tema: Biologija'),font=("Helvetica", 20))
        elif x==5:
            tb=Label(glavni, text = '{}'.format('Tema: Tjelesni'),font=("Helvetica", 20))
        elif x==6:
            tb=Label(glavni, text = '{}'.format('Tema: Povijest') ,font=("Helvetica", 20))
        elif x==7:
            tb=Label(glavni, text = '{}'.format('Tema: Hrvatski'),font=("Helvetica", 20))
        elif x==8:
            tb=Label(glavni, text = '{}'.format('Tema: Geografija'),font=("Helvetica", 20))
        elif x==9:
            tb=Label(glavni, text = '{}'.format('Tema: Sociologija'),font=("Helvetica", 20))
        elif x==10:
            tb=Label(glavni, text = '{}'.format('Tema: Logika'),font=("Helvetica", 20))
        tb.pack(fill=X)
        
        tb1=Label(glavni,text='Nepoznata riječ :',font=("Helvetica", 14))
        tb1.place(x=10,y=150)
        tb2=Label(glavni,text='   '+len(t)*'___  ',font=("Helvetica", 14))
        tb2.place(x=160,y=150)
        
        tb3=Label(glavni,text='Unesi slovo:  ',font=("Helvetica", 12))
        tb3.place(x=10,y=210)
    def unos(t):
        u = Entry(glavni,width=5)
        u.place(x=100, y=215)
        global sp,sk,li,pokusaji
        li=['  ' for i in range(len(t))]
        sp=set('')
        sk=set('')
        pokusaji=2*len(set(t))
        def pokusaj(event):
            global sp,sk,li,t,pokusaji
            s=u.get()
            u.delete(0,100)
            t=list(t)
            
            if s in 'abcčćdđefghijklmnoprsštuvzž' and len(s)==1:
                if s in sk or s in sp:
                    de=Label(glavni,text=' '*200)
                    de.place(x=10,y=250)
                    tb9=Label(glavni,text='ERROR: Slovo {} je vec upisano.'.format(s),font=("Helvetica", 9))
                    tb9.place(x=10,y=250)
                else:
                    de=Label(glavni,text=' '*200)
                    de.place(x=10,y=250)
                    if s in t:
                        pokusaji=pokusaji-1
                        sp.add(s)
                        for i in range(len(li)):
                            if s==t[i]:
                                li[i]=t[i]
                    else:
                        pokusaji=pokusaji-1
                        sk.add(s)
                
                sps=','.join(sp)
                tb9=Label(glavni,text='Pogođena slova: {}'.format(sps),font=("Helvetica", 9))
                tb9.place(x=600,y=50)
                sks=','.join(sk)
                tb9=Label(glavni,text='Promašena slova: {}'.format(sks),font=("Helvetica", 9))
                tb9.place(x=600,y=70)
            elif s==' ':
                de=Label(glavni,text=' '*200)
                de.place(x=10,y=250)
                tb9=Label(glavni,text='ERROR: Znak {} nije znak hrvatske abecede.'.format('  (space)'),font=("Helvetica", 9))
                tb9.place(x=10,y=250)
            else:
                de=Label(glavni,text=' '*200)
                de.place(x=10,y=250)
                tb9=Label(glavni,text='ERROR: Znak {} nije znak hrvatske abecede.'.format(s),font=("Helvetica", 9))
                tb9.place(x=10,y=250)
            de=Label(glavni,text=' '*100)
            de.place(x=600,y=100)
            tb11=Label(glavni,text='Broj preostalih pokušaja: {}'.format(pokusaji))
            tb11.place(x=600,y=100)
                
            z='     '
            for i in range(len(li)):
                z=z+li[i]+'       '
            tb10=Label(glavni,text=z,font=("Helvetica", 14))
            tb10.place(x=160,y=145)
            if len(sp)==len(set(t)) or len(sp)+len(sk)==2*len(set(t)):
                def nista(event):
                    return
                glavni.bind('<Return>',nista)
                u.config(state='disabled')
                menubar.entryconfig("Restart", state="disabled")
                menubar.entryconfig("Quit", state="disabled")
                noti = Tk()
                noti.title('Igra završena')
                noti.geometry('150x100')
                def da():
                    noti.destroy()
                    glavni.destroy()
                    main()
                def ne():
                    exit()
                tc=Label(noti,text='Ponoviti igru?',font=("Helvetica", 14))
                tc.pack(fill=X)
                bc1= ttk.Button(noti, text = 'Da', command=da , width=5)
                bc1.place(x = 30, y = 50)
                bc2= ttk.Button(noti, text = 'Ne', command=ne , width=5)
                bc2.place(x = 80, y = 50)
                noti.protocol('WM_DELETE_WINDOW', exit)
                noti.mainloop()

        
        glavni.bind('<Return>',pokusaj)
    def restart():
        glavni.destroy()
        main()
    menubar = Menu(glavni)
    menubar.add_command(label="Help", command=halp)
    menubar.add_command(label="About", command=about)
    menubar.add_command(label="Restart", command=restart)
    menubar.add_command(label="Quit", command=exit)
    glavni.config(menu=menubar)
        
    global t
    t=tema(x)
    ispis(x,t)
    unos(t)
    glavni.mainloop()
if __name__ == '__main__':
    main()
