# done:
# - cascading menus work
# - files open with os default apps
# - close submenu on rightclick
#
# todo:
# - display edge awareness (open in correct direction - left/right, up/down)
# - build previewer
#   - tie in pre-written
#   - write for human-readable (printable chars only)
# - make pretty with LabelFrame
# - ignore self executable
# - add scrollers to the menus (mouse scroll?)
# - kbd nav?
# - handle permission denied to folder - mitigated with try/except
# - prevent duplicate submenus
# - add "open folder"

import tkinter as tk
import win32api
import os
# import subprocess

background_c = "#333333"
foreground_c = "#88CCFF"
selected_c ="#FFCC00"
boxwidth = 200
#tk preset from font
entry_height = 21
initpath = os.getcwd()
pos = win32api.GetCursorPos()

class ItemEntry(tk.Frame):
    def __init__(self, tkparent, name, type, path, corners):
        tkparent.overrideredirect(True)
        print("making ItemEntry: " + name)
        tk.Label.__init__(self, tkparent)
        self.corners = corners
        self.name = name
        self.type = type
        self.path = path
        # self.tkparent = tkparent
        var = tk.StringVar()
        self.label = tk.Label(self, width=boxwidth, textvariable=var, background=background_c, foreground=foreground_c, justify=tk.RIGHT, anchor="e")
        var.set(self.name)
        self.configure(width=boxwidth, borderwidth=0, highlightthickness=0)
        self.label.pack()

        self.label.bind("<Enter>", self.on_enter)
        self.label.bind("<Leave>", self.on_leave)
        self.label.bind("<Button-1>", self.on_leftclick)

    def on_enter(self, event):
        self.label.configure(foreground=selected_c)
    def on_leave(self, enter):
        self.label.configure(foreground=foreground_c)
        self.label.configure(relief=tk.FLAT)
    def on_leftclick(self, event):
        self.label.configure(relief=tk.SUNKEN)
        if self.type == "file":
            # preview file - future
            # print("preview file")
            os.startfile(self.path)
            quit()

        else:
            # create cascade from dir
            print("pop another dir window")
            cascadeTopLevel = tk.Toplevel()
            pop_menu(cascadeTopLevel, self.path, self.corners['ne'][0], self.corners['ne'][1])

def pop_menu(tkparent, path, posx, posy):
    print("making menu at " + path)
    entries = []
    try:
        dir_contents = os.scandir(path=path)
        for file_entry in (dir_contents): # read folder contents
            if not file_entry.name.startswith('.'): # hide dotfiles
                if file_entry.is_dir():
                    entryname = file_entry.name + " >"
                    entrytype = "dir"
                else:
                    entryname = file_entry.name
                    entrytype = "file"
                corners = {
                    'nw': (posx,posy+len(entries)*entry_height),
                    'ne': (posx+boxwidth,posy+len(entries)*entry_height),
                    # 'se': (posx+boxwidth,posy+entry_height+len(entries)*entry_height), # unnecessary?
                    # 'sw': (posx,posy+entry_height+len(entries)*entry_height)           #
                }
                tampa = ItemEntry(tkparent, entryname, entrytype, file_entry.path, corners)
                entries.append(tampa)
                tampa.pack()
    except:
        print("can't open")
    
    boxheight = len(entries)*entry_height
    tkparent.geometry(str(boxwidth) + "x" + str(boxheight) + "+" + str(posx) + "+" + str(posy))#("%dx%d+%d+%d", %())
    tkparent.configure(bg=background_c)
    tkparent.bind("<Button-3>", on_rightclick)

    menus.append(tkparent)

def kill_last_menu():
    menus.pop().destroy()

def quit():
    for menu in menus:
        menu.destroy()
    exit()

def on_rightclick(self):
    kill_last_menu()
menus = [] # build list of submenus to keep track and manage
root = tk.Tk()
pop_menu(root, initpath, pos[0], pos[1])
root.bind("<Button-3>", on_rightclick)
# undecorate
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