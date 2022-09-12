from tkinter import *
from tkinter import messagebox
import pickle
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox 
import sqlite3
from datetime import datetime
from tkinter.ttk import Treeview

root= Tk()
root.geometry("300x500")
root.title('Учет домашних животных')

def registration():
    text = Label (text = "Для входа в систему - зарегистрируйтесь")
    text_log = Label(text = 'Введите ваш логин:')
    registr_lodin = Entry()
    text_password1 = Label(text="Введите ваш пароль")
    registr_password1 = Entry()
    text_password2 = Label(text="Повторите пароль")
    registr_password2 = Entry(show = "*" )
    button_registr = Button(text = "Зарегистрироваться", command = lambda: save())
    text.pack()
    text_log.pack()
    registr_lodin.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save[registr_lodin.get()]=registr_password1.get()
        f = open ("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text = ' Если вы зарегистрированы')
    text_enter_login=Label(text = "Введите ваш логин:")
    enter_login = Entry()
    text_enter_pass = Label(text = "Введите ваш пароль:")
    enter_password = Entry (show = "*")
    button_enter = Button(text="Войти", command = lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open ("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() ==  a[enter_login.get()]:
                start_window_1()
                #messagebox.showinfo("Добро пожаловать в систему", "а тут я еще не сделал")
            else:
                messagebox.showerror("Ошибка", 'Вы выели неверный логин или пароль')
        else:
            messagebox.showerror("Ошибка", 'Вы ввели неверный логин или пароль')

def start_window_1():
    new_window_1= Toplevel(root)
    new_window_1.title ("Выбор пользователя")
    new_window_1.resizable(0,0)
    new_window_1.geometry('300x500')
    text2 = Label (new_window_1, text = "Вы успешно зашли в систему")
    text3 = Label (new_window_1, text ="Выберете пользователя")
    text2.pack()
    text3.pack()
    b0= Button (new_window_1, text= "Персонал", command=start_window_2)
    b0.pack()
    b1= Button (new_window_1, text= "Клиент", command=start_window_3)
    b1.pack()
    b2= Button (new_window_1, text= "Администратор", command=start_window_21)
    b2.pack()

def start_window_21():
    new_window_21= Toplevel(root)
    new_window_21.title ("Администратор")
    new_window_21.resizable(0,0)
    new_window_21.geometry('300x500')
    text2 = Label (new_window_21, text = "Страница исключительно для администратора")
    text2.pack()
    text2 = Label (new_window_21, text = "Введите ключ доступа:")
    text2.pack()
    q="123"
    vvod = Entry (new_window_21,show = "*")
    vvod.pack()

    def clicked():
        if vvod.get() == q:
            start_window_22()
        else:
            messagebox.showerror("Ошибка")

    b21 = Button(new_window_21,text="Войти", command = clicked)
    b21.pack()

def start_window_22():
    new_window_22= Toplevel(root)
    new_window_22.title ("Администратор")
    new_window_22.resizable(0,0)
    new_window_22.geometry('300x500')
    text3 = Label (new_window_22, text = "Здравствуйте, хорошего рабочего дня")
    text3.pack()
    b111 = Button(new_window_22,text="Клиент", command = start_klient)
    b111.pack()
    b222 = Button(new_window_22,text="Персонал", command = start_pacient)
    b222.pack()
    b333 = Button(new_window_22,text="Заявка", command = start_zayavka)
    b333.pack()

def start_klient():
    new_window_klient= Toplevel(root)
    new_window_klient.title ("Клиенты")
    new_window_klient.resizable(0,0)
    new_window_klient.geometry('300x500')

def start_pacient():
    new_window_pacient= Toplevel(root)
    new_window_pacient.title ("Персонал")
    new_window_pacient.resizable(0,0)
    new_window_pacient.geometry('300x500')

def start_zayavka():
    new_window_zayavka= Toplevel(root)
    new_window_zayavka.title ("Заявки")
    new_window_zayavka.resizable(0,0)
    new_window_zayavka.geometry('600x500')
    uchet_table(new_window_zayavka)
    
    
def start_window_2():
    new_window_2= Toplevel(root)
    new_window_2.title ("Персонал")
    new_window_2.resizable(0,0)
    new_window_2.geometry('300x500')
    text2 = Label (new_window_2, text = "Страница для работников клиник")
    text2.pack()
    text2 = Label (new_window_2, text = "Введите ключ доступа:")
    text2.pack()
    q="12345"
    vvod = Entry (new_window_2,show = "*")
    vvod.pack()

    def clicked():
        if vvod.get() == q:
            start_window_11()
        else:
            messagebox.showerror("Ошибка")

    b11 = Button(new_window_2,text="Войти", command = clicked)
    b11.pack()

def start_window_11():

    def clicked():
        start_window_12()
        with sqlite3.connect('Desktop/Krs/database.db') as db:
            cursor = db.cursor()    
            query = f"""INSERT INTO Personal (familia, imya, otchestvo, doljnost, id_Klinika) 
                        VALUES ('{fam.get()}', '{name.get()}', '{otch.get()}', '{dol.get()}', '{kli.get().split('_')[0]}')"""
            cursor.execute(query)
            db.commit()

    with sqlite3.connect('Desktop/Krs/database.db') as db:
            cursor = db.cursor()
            data = cursor.execute("SELECT id, name FROM Klinika")
            kliniks = [f'{r[0]}_{r[1]}' for r in data]

    new_window_11= Toplevel(root)
    new_window_11.title ("Персонал")
    new_window_11.resizable(0,0)
    new_window_11.geometry('300x500')
    text3 = Label (new_window_11, text = "Введите свои личные данные")
    text3.pack()
    tfam = Label (new_window_11, text = "Фамилия:")
    fam = Entry(new_window_11,width=30)
    tname = Label (new_window_11, text = "Имя:")
    name = Entry(new_window_11,width=30)
    totch = Label (new_window_11, text = "Отчество:")
    otch = Entry(new_window_11,width=30)
    tdol = Label (new_window_11, text = "Должность:")
    dol = Entry(new_window_11,width=30)
    tkli = Label (new_window_11, text = "Клиника:")
    # kli = Entry(new_window_11,width=30)
    kli = Combobox(new_window_11, values=kliniks)
    tfam.pack()
    fam.pack()
    tname.pack()
    name.pack()
    totch.pack()
    otch.pack()
    tdol.pack()
    dol.pack()
    tkli.pack()
    kli.pack()


    b7= Button (new_window_11, text= "Ввод", command=clicked)
    b7.pack()


def start_window_12():
    new_window_12= Toplevel(root)
    new_window_12.title ("Персонал")
    new_window_12.resizable(0,0)
    new_window_12.geometry('300x500')
    text3 = Label (new_window_12, text = "Здравствуйте, хорошего рабочего дня")
    text3.pack()
    b1= Button (new_window_12, text= "Показать заявки", command=start_perszayavka)
    b1.pack()

def confirm_status(cs_window, table, zayavka_id):
    with sqlite3.connect('Desktop/Krs/database.db') as db:
        cursor = db.cursor()
        query = f"""UPDATE Uchet
                    SET status=1
                    WHERE id={int(zayavka_id)}"""
        cursor.execute(query)
        db.commit()
        cs_window.destroy()

def start_confirm_status_window(table, row):
    cs_window = Toplevel(root)
    cs_window.title ("Статус заявки")
    cs_window.resizable(0,0)
    cs_window.geometry('300x500')
    Button(cs_window, text="Выполнена", command=lambda: confirm_status(cs_window, table, row[0])).pack()
    Button(cs_window, text="Не выполнена", command=cs_window.destroy).pack()
    Button(cs_window, text="Удалить заявку").pack()


def item_selected(event, table):
    for selected_item in table.selection():
        item = table.item(selected_item)
        row = item['values']
        start_confirm_status_window(table, row)

def get_uchet():
    with sqlite3.connect('Desktop/Krs/database.db') as db:
        cursor = db.cursor()    
        _uchet = f"""SELECT 
                        u.id, u.data,
                        vl.familia, vl.imya, vl.otchestvo,
                        pi.vid, pi.poroda,
                        pr.naimenovanie,
                        kl.adres
                    FROM Uchet AS u
                    JOIN Vladelec AS vl 
                        ON u.id_Vladec=vl.id
                    JOIN Pitomec AS pi
                        ON u.id_Pitomec=pi.id
                    JOIN Procedur AS pr
                        ON u.id_Procedur=pr.id
                    JOIN Klinika AS kl
                        ON pr.id_Klinika=kl.id

                    """
        uchet = cursor.execute(_uchet)
        return [{
            'uid': row[0],
            'data': row[1],
            'vladelec_fio': f'{row[2]} {row[3]} {row[4]}',
            'pitomec_vid': row[5],
            'pitomec_poroda': row[6],
            'procedur_name': row[7],
            'klinika_address': row[8]
        } for row in uchet]

def start_perszayavka():
    new_perszayavka= Toplevel(root)
    new_perszayavka.title ("Статус Заявки")
    new_perszayavka.resizable(0,0)
    new_perszayavka.geometry('600x500')
    uchet_table(new_perszayavka)

def uchet_table(window):
    uchet = get_uchet() 
    columns = ('uid','data', 'fio', 'vid', 'poroda', 'procedur', 'address')

    table = Treeview(window, columns=columns, show='headings')
    table.pack()

    for col in columns:
        width = 0 if col == 'uid' else 80
        table.column(col, anchor=CENTER, width=width)

    table.heading('data', text='Дата')
    table.heading('fio', text='ФИО')
    table.heading('vid', text='Вид')
    table.heading('poroda', text='Порода')
    table.heading('procedur', text='Процедура')
    table.heading('address', text='Адрес')

    for row in uchet:
        table.insert('', END, values=list(row.values()), open=True)
    table.bind('<<TreeviewSelect>>', lambda event: item_selected(event, table))

    
def start_window_3():

    def clicked():
        with sqlite3.connect('Desktop/Krs/database.db') as db:
            cursor = db.cursor()    
            query = f"""INSERT INTO Vladelec (familia, imya, otchestvo, telefon) 
                        VALUES ('{fam.get()}', '{name.get()}', '{otch.get()}', '{tel.get()}')"""
            cursor.execute(query)
            db.commit()
            start_window_4(cursor.lastrowid)

    new_window_3= Toplevel(root)
    new_window_3.title ("Клиент")
    new_window_3.resizable(0,0)
    new_window_3.geometry('300x500')
    text2 = Label (new_window_3, text = "Вы успешно зашли в систему")
    text2.pack()
    text3 = Label (new_window_3, text = "Введите свои личные данные")
    text3.pack()
    tfam = Label (new_window_3, text = "Фамилия:")
    fam = Entry(new_window_3,width=30)
    tname = Label (new_window_3, text = "Имя:")
    name = Entry(new_window_3,width=30)
    totch = Label (new_window_3, text = "Отчество:")
    otch = Entry(new_window_3,width=30)
    ttel = Label (new_window_3, text = "Номер телефона:")
    tel = Entry(new_window_3,width=30)
    #kli = Combobox(new_window_3, values=kliniks)
    tfam.pack()
    fam.pack()
    tname.pack()
    name.pack()
    totch.pack()
    otch.pack()
    ttel.pack()
    tel.pack()
    b4= Button (new_window_3, text= "Ввод", command= clicked)
    b4.pack()

def start_window_4(vladelec_id):

    def clicked():
        with sqlite3.connect('Desktop/Krs/database.db') as db:
            cursor = db.cursor()    
            query = f"""INSERT INTO Pitomec (vid ,poroda, vozrast, klichka, pol, okras, id_Vladelec) 
                        VALUES ('{vid.get()}', '{por.get()}', '{vozr.get()}', '{kli.get()}', '{pol.get()}',  '{ocr.get()}', {vladelec_id})"""
            cursor.execute(query)
            pitomec_id = cursor.lastrowid
            db.commit()
            start_window_5(vladelec_id, pitomec_id)

    new_window_4= Toplevel(root)
    new_window_4.title ("Питомец")
    new_window_4.resizable(0,0)
    new_window_4.geometry('300x500')
    text2 = Label (new_window_4, text = f"Ваши данные сохранены")
    text2.pack()
    text3 = Label (new_window_4, text = "Теперь введите данный питомца")
    text3.pack()
    tvid = Label (new_window_4, text = "Вид:")
    vid = Entry(new_window_4,width=30)
    tpor = Label (new_window_4, text = "Порода:")
    por = Entry(new_window_4,width=30)
    tvozr = Label (new_window_4, text = "Возраст:")
    vozr = Entry(new_window_4,width=30)
    tkli = Label (new_window_4, text = "Кличка:")
    kli = Entry(new_window_4,width=30)
    tpol = Label (new_window_4, text = "Пол:")
    pol = Combobox(new_window_4, values=['Выберете пол', 'М', 'Ж'])
    pol.current(0) 
    tocr = Label (new_window_4, text = "Окрас:")
    ocr = Entry(new_window_4,width=30)
    tvid.pack()
    vid.pack()
    tpor.pack()
    por.pack()
    tvozr.pack()
    vozr.pack()
    tkli.pack()
    kli.pack()
    tpol.pack()
    pol.pack()
    tocr.pack()
    ocr.pack()

    b5= Button (new_window_4, text= "Ввод", command= clicked)
    b5.pack()
    
def start_window_5(vladelec_id, pitomec_id):

    def uslugi_select(event):
        if combo.get():
            uid = int(combo.get().split('_')[0])
            stoimost_text = next(filter(lambda x: x['uid'] == uid, uslugi))['stoimost']
            stoimost.config(text=f'Стоимость услуги: {stoimost_text}')

    with sqlite3.connect('Desktop/Krs/database.db') as db:
        cursor = db.cursor()    
        query = f"""SELECT * FROM Procedur"""
        data = cursor.execute(query)
        uslugi = [{'uid': r[0], 'name': r[1], 'stoimost': r[2], 'kid': r[3]} for r in data]
        db.commit()

    new_window_5= Toplevel(root)
    new_window_5.title ("Услуги")
    new_window_5.resizable(0,0)
    new_window_5.geometry('300x500')
    text2 = Label (new_window_5, text = "Данные вашего питомца сохранены")
    text2.pack()
    text3 = Label (new_window_5, text = "Выберете услугу")
    text3.pack()
    combo = Combobox(new_window_5, values=[f"{u['uid']}_{u['name']}" for u in uslugi])
    combo.current(0)
    combo.pack()
    combo.bind("<<ComboboxSelected>>", uslugi_select)
    stoimost = Label (new_window_5)
    stoimost.pack()

    def save_uslugi():
        messagebox.showerror("Спасибо", "Ваша заявка успешно сохранена")
        with sqlite3.connect('Desktop/Krs/database.db') as db:
            cursor = db.cursor()
            uid = combo.get().split('_')[0]
            query = f"""INSERT INTO Uchet (data, id_Pitomec, id_Personal, id_Procedur, id_Vladec) 
                        VALUES ('{datetime.now()}', {pitomec_id}, {1}, {uid}, {vladelec_id})"""
            # personal = random.choice(['id1', 'id2', ...])
            cursor.execute(query)
            db.commit()
    
    b6= Button (new_window_5, text= "Ввод", command = save_uslugi)
    b6.pack() 

registration()
login()

root.mainloop()

