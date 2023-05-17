import tkinter as tk
import win32api
import os
import subprocess

background_c = "#333333"
foreground_c = "#88CCFF"
selected_c ="#FFCC00"
boxwidth = 200
#tk preset from font
entry_height = 21
initpath = os.getcwd()
pos = win32api.GetCursorPos()

class ItemEntry(tk.Frame):
    def __init__(self, tkp, n, t, p):
        tk.Label.__init__(self)
        self.name = n
        self.type = t
        self.path = p
        self.tkparent = tkp
        var = tk.StringVar()
        self.label = tk.Label(self, width=boxwidth, textvariable=var, background=background_c, foreground=foreground_c, justify=tk.RIGHT, anchor="e")
        var.set(n)
        self.configure(width=boxwidth, borderwidth=0, highlightthickness=0)
        self.label.pack()

        self.label.bind("<Enter>", self.on_enter)
        self.label.bind("<Leave>", self.on_leave)
        self.label.bind("<ButtonPress>", self.on_click)

    def on_enter(self, event):
        self.label.configure(foreground=selected_c)
    def on_leave(self, enter):
        self.label.configure(foreground=foreground_c)
        self.label.configure(relief=tk.FLAT)
    def on_click(self, event):
        if self.type == "file":
            # preview file
            print("preview file")
        else:
            # create cascade from dir
            print("pop another dir window!")
            self.cascadeTopLevel = tk.Toplevel()
            pop_menu(self.cascadeTopLevel, self.path)
            self.cascadeTopLevel.pack(self.tkparent)
        self.label.configure(relief=tk.SUNKEN)

def pop_menu(tkparent, path, posx, posy):
    entries = []
    # if (isinstance(tkparent, tk.Tk)):
    #     print("root is tk.Tk")
    # else:
    for file_entry in (os.scandir(path=path)): # read folder contents
        if not file_entry.name.startswith('.'): # hide dotfiles
            if file_entry.is_dir():
                entryname = file_entry.name + " >"
                entrytype = "dir"
            else:
                entryname = file_entry.name
                entrytype = "file"
            entrypath = file_entry.path
            tampa = ItemEntry(tkparent, entryname, entrytype, entrypath)
            entries.append(tampa)
            tampa.pack(tkparent)
    boxheight = len(entries)*entry_height
    tkparent.geometry(str(boxwidth) + "x" + str(boxheight) + "+" + str(posx) + "+" + str(posy))
    tkparent.configure(bg=background_c)

# Create object
root = tk.Tk()
pop_menu(root, initpath, pos[0], pos[1])
# Use overrideredirect() method
# root.overrideredirect(True)

# Execute tkinter
if __name__ == "__main__":
    root.mainloop()


# fpath = "cascade.py"
# f = open(fpath, "r")
# for c in f.read(100):
#     if ord(c) not in range(0,127):
#         print("nonprintable!")

# def on_enter(event):
#     event.widget.configure(foreground=selected_c)
# root.bind_all("<Enter>", on_enter)