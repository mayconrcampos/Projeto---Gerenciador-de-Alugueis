from tkcalendar import Calendar, DateEntry
from tkinter import *

class Calendario:
    def calendario_data_assinatura_aba_04(self):
        self.calendario_dt_ass_aba_04 = Calendar(self.aba_04, bg="#454545", locale="pt_br")
        self.calendario_dt_ass_aba_04['font'] = "Arial", 9
        self.calendario_dt_ass_aba_04.place(relx=0.416, rely=0.42)

        self.btn_calendar_data_ass_aba_04 = Button(self.aba_04, text="Inserir Data", command=self.print_calendario_data_assinatura_aba_04)
        self.btn_calendar_data_ass_aba_04['font'] = "Arial", 12
        self.btn_calendar_data_ass_aba_04.place(relx=0.416, rely=0.74, relwidth=0.223, relheight=0.04)

    def print_calendario_data_assinatura_aba_04(self):
        dataIni = self.calendario_dt_ass_aba_04.get_date()
        self.calendario_dt_ass_aba_04.destroy()

        self.entry_data_ass_aba_04.delete(0, END)
        self.entry_data_ass_aba_04.insert(END, dataIni)
        self.btn_calendar_data_ass_aba_04.destroy()
    
    def calendario_data_caucao_aba_04(self):
        self.calendario_dt_caucao_aba_04 = Calendar(self.aba_04, bg="#454545", locale="pt_br")
        self.calendario_dt_caucao_aba_04['font'] = "Arial", 9
        self.calendario_dt_caucao_aba_04.place(relx=0.416, rely=0.515)

        self.btn_calendar_data_caucao_aba_04 = Button(self.aba_04, text="Inserir Data", command=self.print_calendario_data_caucao_aba_04)
        self.btn_calendar_data_caucao_aba_04['font'] = "Arial", 12
        self.btn_calendar_data_caucao_aba_04.place(relx=0.416, rely=0.835, relwidth=0.223, relheight=0.04)

    def print_calendario_data_caucao_aba_04(self):
        dataIni = self.calendario_dt_caucao_aba_04.get_date()
        self.calendario_dt_caucao_aba_04.destroy()

        self.entry_data_caucao_aba_04.delete(0, END)
        self.entry_data_caucao_aba_04.insert(END, dataIni)
        self.btn_calendar_data_caucao_aba_04.destroy()
    
    def calendario_data_entrega_aba_04(self):
        self.calendario_dt_entrega_aba_04 = Calendar(self.aba_04, bg="#454545", locale="pt_br")
        self.calendario_dt_entrega_aba_04['font'] = "Arial", 9
        self.calendario_dt_entrega_aba_04.place(relx=0.579, rely=0.423)

        self.btn_calendar_data_entrega_aba_04 = Button(self.aba_04, text="Inserir Data", command=self.print_calendario_data_entrega_aba_04)
        self.btn_calendar_data_entrega_aba_04['font'] = "Arial", 12
        self.btn_calendar_data_entrega_aba_04.place(relx=0.579, rely=0.742, relwidth=0.224, relheight=0.04)

    def print_calendario_data_entrega_aba_04(self):
        dataIni = self.calendario_dt_entrega_aba_04.get_date()
        self.calendario_dt_entrega_aba_04.destroy()

        self.entry_data_entrega_aba_04.delete(0, END)
        self.entry_data_entrega_aba_04.insert(END, dataIni)
        self.btn_calendar_data_entrega_aba_04.destroy()
    
    def calendario_data_pagto_aba_05(self):
        self.calendario_dt_pagto_aba_05 = Calendar(self.aba_05, bg="#454545", locale="pt_br")
        self.calendario_dt_pagto_aba_05['font'] = "Arial", 9
        self.calendario_dt_pagto_aba_05.place(relx=0.72, rely=0.095)

        self.btn_calendar_data_pagto_aba_05 = Button(self.aba_05, text="Inserir Data", command=self.print_calendario_data_pagto_aba_05)
        self.btn_calendar_data_pagto_aba_05['font'] = "Arial", 12
        self.btn_calendar_data_pagto_aba_05.place(relx=0.72, rely=0.415, relwidth=0.224, relheight=0.04)

    def print_calendario_data_pagto_aba_05(self):
        dataIni = self.calendario_dt_pagto_aba_05.get_date()
        self.calendario_dt_pagto_aba_05.destroy()

        self.entry_data_pagto_aba_05.delete(0, END)
        self.entry_data_pagto_aba_05.insert(END, dataIni)
        self.btn_calendar_data_pagto_aba_05.destroy()
