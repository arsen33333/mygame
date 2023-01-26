import tkinter as tk
root = tk.Tk()
root.title("bvbvbbv")
root.geometry("500x500")
root.resizable(False, False)
root.config(background="black")

label = tk.Label(text="Заполните анкету", background="white", font="Comic 30")
label.pack(anchor="center")

entry_fio = tk.Entry(font ="Comic 25")
entry_age = tk.Entry(font= "Comic 25")
entry_class = tk.Entry(font= "Comic 25")
entry_fio.pack(anchor= "center", pady=10)
entry_age.pack(anchor= "center", pady=10)
entry_class.pack(anchor= "center", pady=10)
root.mainloop()

