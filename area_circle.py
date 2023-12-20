# 12 Team Activity: Using Objects
#Area of a Circle

import math
import tkinter as tk
from tkinter import Frame, Label, Button
from Number_entry import IntEntry

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()


def populate_main_window(frm_main):
    lbl_age = Label(frm_main, text="Radius (r):")
    ent_age = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=9999)
    lbl_age_units = Label(frm_main, text="in")
    lbl_rates = Label(frm_main, text="Area:")
    lbl_slow = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="in")
    btn_clear = Button(frm_main, text="Clear")

    lbl_age.grid(      row=0, column=0, padx=3, pady=3)
    ent_age.grid(      row=0, column=1, padx=3, pady=3)
    lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_slow.grid(      row=1, column=2, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    def calculate(event):
        try:
            """Area of a circle: a = π*r^2"""
            radius = ent_age.get()

            max_rate = (radius * radius)
            slow = max_rate * math.pi

            lbl_slow.config(text=f"{slow:.2f}")

        except ValueError:
            lbl_slow.config(text="")


    def clear():
        btn_clear.focus()
        ent_age.clear()
        lbl_slow.config(text="")
        ent_age.focus()

    ent_age.bind("<KeyRelease>", calculate)
    btn_clear.config(command=clear)
    ent_age.focus()


if __name__ == "__main__":
    main()
