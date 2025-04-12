import os
import tkinter as tk


class Stud():
    def __init__(self, ID, fstName, lstName):
        self.ID = ID
        self.fstName = fstName
        self.lstName = lstName
        self.creditNum = 0.0
        self.gpa = 0.0

    def addScore(self, grade, credit):
        self.gpa = (self.gpa * self.creditNum + grade * credit) / (self.creditNum + credit)
        self.creditNum = self.creditNum + credit


class Prof():
    def __init__(self, ID, fstName, lstName):
        self.ID = ID
        self.fstName = fstName
        self.lstName = lstName


class Unit():
    def __init__(self, code, profID, name, credit):
        self.code = code
        self.profID = profID
        self.name = name
        self.credit = int(credit)


studs = []
profs = []
units = []


def studReg():
    mainWindow.withdraw()

    def reg():
        fstName, lstName, ID = fstNameEnt.get(), lstNameEnt.get(), IDEnt.get()
        stud = Stud(ID, fstName, lstName)
        studs.append(stud)
        fstNameEnt.delete(0, 'end'), lstNameEnt.delete(0, 'end'), IDEnt.delete(0, 'end')
        statusLbl['text'] = str('دانشجو با کد ' + ID + ' ثبت شد')
        statusLbl.config(fg='green')

    def bck():
        studWindow.destroy()
        mainWindow.update()
        mainWindow.deiconify()

    studWindow = tk.Tk()
    studWindow.title("فرم ثبت دانشجو")
    studWindow.resizable(width=False, height=False)
    studWindow.protocol('WM_DELETE_WINDOW', bck)
    studMaiFrame = tk.Frame(master=studWindow)
    statusLbl = tk.Label(master=studMaiFrame, text=" ")
    IDLbl = tk.Label(master=studMaiFrame, text=":کد")
    fstNameLbl = tk.Label(master=studMaiFrame, text=":نام")
    lstNameLbl = tk.Label(master=studMaiFrame, text=":نام خانوادگی")
    IDEnt = tk.Entry(master=studMaiFrame, width=30)
    fstNameEnt = tk.Entry(master=studMaiFrame, width=30)
    lstNameEnt = tk.Entry(master=studMaiFrame, width=30)
    regButton = tk.Button(master=studMaiFrame, text="ثبت", command=reg)
    bckButton = tk.Button(master=studMaiFrame, text="بازگشت", command=bck)
    studMaiFrame.grid(row=0, column=0)
    statusLbl.grid(row=0, column=0, pady=5)
    IDLbl.grid(row=1, column=1, padx=10, sticky="e")
    IDEnt.grid(row=1, column=0, padx=10, sticky="e")
    fstNameLbl.grid(row=2, column=1, padx=10, pady=5, sticky="e")
    fstNameEnt.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    lstNameLbl.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    lstNameEnt.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    bckButton.grid(row=4, column=0, pady=5, sticky="e")
    regButton.grid(row=4, column=1, pady=5)
    studWindow.update()
    studWindow.deiconify()


def profReg():
    mainWindow.withdraw()

    def reg():
        fstName, lstName, ID = fstNameEnt.get(), lstNameEnt.get(), IDEnt.get()
        prof = Prof(ID, fstName, lstName)
        profs.append(prof)
        fstNameEnt.delete(0, 'end'), lstNameEnt.delete(0, 'end'), IDEnt.delete(0, 'end')
        statusLbl['text'] = str('استاد با کد ' + ID + ' ثبت شد')
        statusLbl.config(fg='green')

    def bck():
        profWindow.destroy()
        mainWindow.update()
        mainWindow.deiconify()

    profWindow = tk.Tk()
    profWindow.title("فرم ثبت استاد")
    profWindow.resizable(width=False, height=False)
    profWindow.protocol('WM_DELETE_WINDOW', bck)
    profMaiFrame = tk.Frame(master=profWindow)
    statusLbl = tk.Label(master=profMaiFrame, text=" ")
    IDLbl = tk.Label(master=profMaiFrame, text=":کد")
    fstNameLbl = tk.Label(master=profMaiFrame, text=":نام")
    lstNameLbl = tk.Label(master=profMaiFrame, text=":نام خانوادگی")
    IDEnt = tk.Entry(master=profMaiFrame, width=30)
    fstNameEnt = tk.Entry(master=profMaiFrame, width=30)
    lstNameEnt = tk.Entry(master=profMaiFrame, width=30)
    regButton = tk.Button(master=profMaiFrame, text="ثبت", command=reg)
    bckButton = tk.Button(master=profMaiFrame, text="بازگشت", command=bck)
    profMaiFrame.grid(row=0, column=0)
    statusLbl.grid(row=0, column=0, pady=5)
    IDLbl.grid(row=1, column=1, padx=10, sticky="e")
    IDEnt.grid(row=1, column=0, padx=10, sticky="e")
    fstNameLbl.grid(row=2, column=1, padx=10, pady=5, sticky="e")
    fstNameEnt.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    lstNameLbl.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    lstNameEnt.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    bckButton.grid(row=4, column=0, pady=5, sticky="e")
    regButton.grid(row=4, column=1, pady=5)
    profWindow.update()
    profWindow.deiconify()


def unitReg():
    mainWindow.withdraw()

    def reg():
        code, profID, name, credit = codeEnt.get(), profIDEnt.get(), nameEnt.get(), float(creditEnt.get())
        unit = Unit(code, profID, name, credit)
        units.append(unit)
        codeEnt.delete(0, 'end'), profIDEnt.delete(0, 'end'), nameEnt.delete(0, 'end'), creditEnt.delete(0, 'end')
        statusLbl['text'] = str('درس با کد ' + code + ' ثبت شد')
        statusLbl.config(fg='green')

    def bck():
        unitWindow.destroy()
        mainWindow.update()
        mainWindow.deiconify()

    unitWindow = tk.Tk()
    unitWindow.title("فرم ثبت درس")
    unitWindow.resizable(width=False, height=False)
    unitWindow.protocol('WM_DELETE_WINDOW', bck)
    unitMaiFrame = tk.Frame(master=unitWindow)
    statusLbl = tk.Label(master=unitMaiFrame, text=" ")
    codeLbl = tk.Label(master=unitMaiFrame, text=":کد درس")
    profIDLbl = tk.Label(master=unitMaiFrame, text=":کد استاد مربوطه")
    nameLbl = tk.Label(master=unitMaiFrame, text=":نام درس")
    creditLbl = tk.Label(master=unitMaiFrame, text=":تعداد واحد")
    codeEnt = tk.Entry(master=unitMaiFrame, width=30)
    profIDEnt = tk.Entry(master=unitMaiFrame, width=30)
    nameEnt = tk.Entry(master=unitMaiFrame, width=30)
    creditEnt = tk.Entry(master=unitMaiFrame, width=30)
    regButton = tk.Button(master=unitMaiFrame, text="ثبت", command=reg)
    bckButton = tk.Button(master=unitMaiFrame, text="بازگشت", command=bck)
    unitMaiFrame.grid(row=0, column=0)
    statusLbl.grid(row=0, column=0, pady=5)
    codeLbl.grid(row=1, column=1, padx=10, sticky="e")
    codeEnt.grid(row=1, column=0, padx=10, sticky="e")
    profIDLbl.grid(row=2, column=1, padx=10, pady=5, sticky="e")
    profIDEnt.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    nameLbl.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    nameEnt.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    creditLbl.grid(row=4, column=1, padx=10, pady=5, sticky="e")
    creditEnt.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    bckButton.grid(row=5, column=0, pady=5, sticky="e")
    regButton.grid(row=5, column=1, pady=5)
    unitWindow.update()
    unitWindow.deiconify()


def gradReg():
    mainWindow.withdraw()
    unitFound = None
    profFound = None

    def sch():
        global unitFound, profFound
        try:
            code = codeEnt.get()
            for unit in units:
                if (unit.code == code):
                    unitFound = unit
            for prof in profs:
                if (unitFound.profID == prof.ID):
                    profFound = prof
            unitLbl['text'] = str(unitFound.name)
            profLbl['text'] = str(profFound.fstName + " " + profFound.lstName)
            statusLbl['text'] = 'درس مورد نظر یافت شد'
            statusLbl.config(fg='green')
        except:
            unitFound = None
            statusLbl['text'] = str("درس یا استاد مربوطه یافت نشد")
            codeEnt.delete(0, 'end')
            statusLbl.config(fg='red')
            profLbl['text'] = '     '
            unitLbl['text'] = '     '

    def reg():
        global unitFound
        try:
            for i in range(len(studs)):
                studs[i].addScore(float(gradEnts[i].get()), float(unitFound.credit))
                gradEnts[i].delete(0, 'end')
            statusLbl['text'] = 'نمرات این درس ثبت شد'
            statusLbl.config(fg='green')
            unitFound = None
            profLbl['text'] = '     '
            unitLbl['text'] = '     '
            codeEnt.delete(0, 'end')
        except:
            statusLbl['text'] = str("نمرات وارد شده معتبر نمیباشند")
            statusLbl.config(fg='red')

    def bck():
        gradWindow.destroy()
        mainWindow.update()
        mainWindow.deiconify()

    gradWindow = tk.Tk()
    gradWindow.title("فرم ثبت نمره")
    gradWindow.resizable(width=False, height=False)
    gradWindow.protocol('WM_DELETE_WINDOW', bck)
    gradMaiFrame = tk.Frame(master=gradWindow)
    gradStdFrame = tk.Frame(master=gradWindow)
    statusLbl = tk.Label(master=gradMaiFrame, text=" ")
    codeLbl = tk.Label(master=gradMaiFrame, text=":کد درس")
    codeEnt = tk.Entry(master=gradMaiFrame, width=30)
    codeButton = tk.Button(master=gradMaiFrame, text="جست و جو", command=sch)
    unitNameLbl = tk.Label(master=gradMaiFrame, text=":نام درس")
    profNameLbl = tk.Label(master=gradMaiFrame, text=":نام و نام خانوادگی استاد")
    unitLbl = tk.Label(master=gradMaiFrame, text="     ")
    profLbl = tk.Label(master=gradMaiFrame, text="     ")
    gradListLbl = tk.Label(master=gradMaiFrame, text="لیست نمرات")
    regButton = tk.Button(master=gradMaiFrame, text="ثبت همه نمرات", command=reg)
    bckButton = tk.Button(master=gradMaiFrame, text="بازگشت", command=bck)
    canvas = tk.Canvas(gradStdFrame)
    scrollbar = tk.Scrollbar(gradStdFrame, orient="vertical", command=canvas.yview)
    scrollableFrame = tk.Frame(canvas)
    scrollableFrame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    fstNameLbl = tk.Label(master=scrollableFrame, text="نام")
    lstNameLbl = tk.Label(master=scrollableFrame, text="نام خانوادگی")
    gradLbl = tk.Label(master=scrollableFrame, text="نمره")
    gradLbl.grid(row=0, column=0, sticky="e")
    lstNameLbl.grid(row=0, column=1, padx=30, sticky="e")
    fstNameLbl.grid(row=0, column=2, sticky="e")
    gradEnts = []
    lstNameEnts = []
    fstNameEnts = []
    for i in range(len(studs)):
        gradEnts.append(tk.Entry(master=scrollableFrame, width=8))
        lstNameEnts.append(tk.Label(master=scrollableFrame, text=studs[i].lstName))
        fstNameEnts.append(tk.Label(master=scrollableFrame, text=studs[i].fstName))
        gradEnts[i].grid(row=i + 1, column=0, sticky="e")
        lstNameEnts[i].grid(row=i + 1, column=1, sticky="e")
        fstNameEnts[i].grid(row=i + 1, column=2, sticky="e")
    gradMaiFrame.grid(row=0, column=0)
    gradStdFrame.grid(row=1, column=0, sticky="e")
    statusLbl.grid(row=0, column=1)
    codeButton.grid(row=1, column=0, padx=10, sticky="e")
    codeEnt.grid(row=1, column=1, padx=10, sticky="e")
    codeLbl.grid(row=1, column=2, padx=10, sticky="e")
    unitLbl.grid(row=2, column=1, padx=10, sticky="e")
    unitNameLbl.grid(row=2, column=2, padx=10, sticky="e")
    profLbl.grid(row=3, column=1, padx=10, sticky="e")
    profNameLbl.grid(row=3, column=2, padx=10, sticky="e")
    gradListLbl.grid(row=4, column=2, padx=10, pady=20, sticky="e")
    regButton.grid(row=4, column=1, sticky="e")
    bckButton.grid(row=4, column=0, sticky="e")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    gradWindow.update()
    gradWindow.deiconify()


def saveReg():
    f = open('output.txt', 'w+')
    for stud in studs:
        f.write(str(str(stud.fstName) + " " + str(stud.lstName) + ": " + str(round(stud.gpa, 2)) + '\r\n'))
    f.close()
    os.startfile('output.txt')
    exit()


mainWindow = tk.Tk()
mainWindow.title("منوی اصلی")
mainWindow.resizable(width=False, height=False)
mainFrame = tk.Frame(master=mainWindow)

studButton = tk.Button(master=mainFrame, text="فرم ثبت دانشجو", command=studReg)
profButton = tk.Button(master=mainFrame, text="فرم ثبت استاد", command=profReg)
unitButton = tk.Button(master=mainFrame, text="فرم ثبت درس", command=unitReg)
gradButton = tk.Button(master=mainFrame, text="فرم ثبت نمرات", command=gradReg)
saveButton = tk.Button(master=mainFrame, text="ذخیره فایل گزارش", command=saveReg)

mainFrame.grid(row=0, column=0, padx=20, pady=20)
studButton.grid(row=0, column=0, pady=5)
profButton.grid(row=1, column=0, pady=5)
unitButton.grid(row=2, column=0, pady=5)
gradButton.grid(row=3, column=0, pady=5)
saveButton.grid(row=4, column=0, pady=5)
mainWindow.mainloop()
