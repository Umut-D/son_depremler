# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=import-error
import tkinter
from tkinter import ttk

from dosya.depremler import Depremler
from internet.baglanti import Baglanti


class Pencere(tkinter.Tk):
    def __init__(self, veriler):
        super().__init__()

        self.title("Son Depremler")
        self.geometry("850x600")

        # Üst menü
        menubar = tkinter.Menu(self)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Aç")
        filemenu.add_command(label="Kaydet")
        filemenu.add_separator()
        filemenu.add_command(label="Çıkış", command=self.quit)
        menubar.add_cascade(label="Dosya", menu=filemenu)
        self.config(menu=menubar)

        # Ana pencere
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Liste
        tree = ttk.Treeview(main_frame,
                            columns=("tarih", "konum", "siddet", "enlem", "boylam", "derinlik"),
                            show="headings")

        tree.column("#0", width=0)  # Hide the index column
        tree.column("tarih", width=70, anchor="center")
        tree.column("konum", width=280, anchor="w")  # Left-align location
        tree.column("siddet", width=20, anchor="center")
        tree.column("enlem", width=30, anchor="center")
        tree.column("boylam", width=30, anchor="center")
        tree.column("derinlik", width=20, anchor="center")
        tree.grid(row=0, column=0, sticky="nsew")

        # Set column headers text
        tree.heading("tarih", text="Tarih")
        tree.heading("konum", text="Konum")
        tree.heading("siddet", text="Şiddet")
        tree.heading("enlem", text="Enlem")
        tree.heading("boylam", text="Boylam")
        tree.heading("derinlik", text="Derinlik")

        for veri in veriler:
            tree.insert("", "end", values=veri)

        # Kaydırma çubukları
        vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=vsb.set)

        # Pencere boyutunu ayarla
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def on_button_click(self):
        pass


depremler = Depremler(baglanti=Baglanti())
json_veriler = depremler.json_veriler()
pencere = Pencere(json_veriler)
pencere.mainloop()
