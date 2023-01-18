# important variable which saves a copy of the filepath when it gets changed
fp = ""
# important variable which saves font size
p = 10


def main():

    # importing things
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    import tkinter.messagebox

    global fp

    # font size
    def size():
        global p
        try:
            p = int(epo.get())
            txt_edit.configure(font=("Consolas", p))
        except:
            tkinter.messagebox.showinfo("error occured", "error occured")

    # save the current file changes

    def savethis():
        global fp
        try:
            with open(fp, "w") as output_file:
                text = txt_edit.get("1.0", tk.END)
                output_file.write(text)
            window.title(f"pyText - {fp}")
            print(fp)
            tkinter.messagebox.showinfo("file saved", "file saved")
        except:
            tkinter.messagebox.showinfo("error occured", "error occured")

    # open a new window
    def new_win():
        main()

    # Save the current file as a new file.
    def save_file():
        global fp
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"pyText - {filepath}")
        tkinter.messagebox.showinfo("file saved", "file saved")
        fp = filepath

    # Open a file for editing.
    def open_file():
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"pyText - {filepath}")
        global fp
        fp = filepath

    # defining the grid and window and other properties
    # defining buttons
    window = tk.Tk()
    window.title("pyText")

    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    txt_edit = tk.Text(window)

    # menu frame design
    fr_buttons = tk.Frame(window)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
    btn_newwin = tk.Button(fr_buttons, text="new window", command=new_win)
    btn_savethis = tk.Button(fr_buttons, text="save current", command=savethis)
    btn_size = tk.Button(fr_buttons, text="change font size", command=size)

    fr_buttons.config(bg='#2A3132')
    textEntry = tk.StringVar()
    textEntry.set(str(p))
    epo = tk.Entry(fr_buttons, textvariable=textEntry)
    epo.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
    epo.focus_set()

    btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    btn_newwin.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    btn_savethis.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    btn_size.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")
    txt_edit.config(bg='#D9D8D7')

    window.minsize(700, 600)

    # find replace bar design
    repfind = tk.Frame(window)
    tk.Label(repfind, text='Find').grid(row=0, column=0, padx=5, pady=5)
    edit = tk.Entry(repfind)
    edit.grid(row=0, column=1)

    edit.focus_set()

    Find = tk.Button(repfind, text='Find')

    Find.grid(row=0, column=2, padx=5, pady=5, sticky="sew")

    tk.Label(repfind, text="Replace With ").grid(
        row=0, column=3, padx=5, pady=5)

    edit2 = tk.Entry(repfind)

    edit2.grid(row=0, column=4, padx=5, pady=5)
    edit2.focus_set()

    replace = tk.Button(repfind, text='Find and Replace')
    replace.grid(row=0, column=5, padx=5, pady=5)

    repfind.grid(row=1, column=1)
    repfind.config(bg='#2A3132')
    txt_edit.configure(font=("Consolas", p))

    # function to search string in text
    def find():

        # remove tag 'found' from index 1 to END
        txt_edit.tag_remove('found', '1.0', tk.END)

        # returns to widget currently in focus
        s = edit.get()

        if (s):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = txt_edit.search(s, idx, nocase=1,
                                      stopindex=tk.END)

                if not idx:
                    break

                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))

                # overwrite 'Found' at idx
                txt_edit.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as red

            txt_edit.tag_config('found', foreground='red',
                                font=('Consolas 10 underline'))
        edit.focus_set()

    def findNreplace():

        # remove tag 'found' from index 1 to END
        txt_edit.tag_remove('found', '1.0', tk.END)

        # returns to widget currently in focus
        s = edit.get()
        r = edit2.get()

        if (s and r):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = txt_edit.search(s, idx, nocase=1,
                                      stopindex=tk.END)
                print(idx)
                if not idx:
                    break

                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))

                txt_edit.delete(idx, lastidx)
                txt_edit.insert(idx, r)

                lastidx = '% s+% dc' % (idx, len(r))

                # overwrite 'Found' at idx
                txt_edit.tag_add('found', idx, lastidx)
                idx = lastidx

            # mark located string as red
            txt_edit.tag_config('found', foreground='green',
                                background='yellow')
        edit.focus_set()

    Find.config(command=find)
    replace.config(command=findNreplace)

    # adding scrollbar
    sb = tk.Scrollbar(
        window,
        orient=tk.VERTICAL
    )

    sb.grid(row=0, column=2, sticky=tk.NS)

    txt_edit.config(yscrollcommand=sb.set)
    sb.config(command=txt_edit.yview)

    p1 = tk.PhotoImage(file='pikq.png')
    # Setting icon of master window
    window.iconphoto(False, p1)

    window.mainloop()


main()
