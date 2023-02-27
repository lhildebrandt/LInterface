from tkinter import *
from tkinter import ttk

def key_check(method):
    def inner(*args,**kwargs):
        if args[1] in args[0].entries.keys() or args[1] in args[0].buttons.keys():
            raise Exception('Key {} already exist'.format(args[1]))
        else:
            return method(*args,**kwargs)
    return inner

class Linterface:
    root=None
    windows_size=None
    main_frame=None
    frame_entries=None
    frame_content=None
    frame_buttons=None
    text_frame=None
    entries={}
    buttons={}

    def __init__(self):
        self.root = Tk()
        self.frame_entries = LabelFrame(self.root,text="Inputs")
        self.frame_content = Frame(self.root)
        self.frame_buttons = Frame(self.root)

        self.frame_entries.grid(row=0,column=0,sticky=(N,E,W),padx=5,pady=5)
        self.frame_content.grid(row=1,column=0,sticky=(N,E,W,S))
        self.frame_buttons.grid(row=2, column=0, sticky=(N,E,W,S))

        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

    @property
    def title(self):
        return self.root.title()

    @title.setter
    def title(self,value):
        self.root.title(value)

    @property
    def size(self):
        return self.root.geometry()

    @size.setter
    def size(self,size):
        if size == "M":
            self.root.geometry("700x675")
        elif size == "L":
            self.root.geometry("1024x675")
        elif size == "S":
            self.root.geometry("200x200")

    def get_root(self):
        return self.root

    def start(self):
        _list_entries = self.frame_entries.winfo_children()
        row_frame = 0
        column_frame = 0
        for item in _list_entries:
            item.grid(row=row_frame,column=column_frame,padx=5,pady=5,sticky=(N,E,W,S))
            self.frame_entries.columnconfigure(column_frame,weight=1)
            self.frame_entries.rowconfigure(row_frame,weight=1)
            column_frame += 1
            if(column_frame == 2):
                column_frame = 0
                row_frame += 1
            children_items = item.winfo_children()
            child_item_columns = 0
            item.rowconfigure(0,weight=1)
            for child_item in children_items:
                child_item.grid(row=0, column=child_item_columns,sticky=(N,E,W))
                if (isinstance(child_item,Entry)):
                    item.columnconfigure(child_item_columns,weight=3)
                else:
                    item.columnconfigure(child_item_columns, weight=1)
                child_item_columns+=1
        _list_buttons = self.frame_buttons.winfo_children()
        button_columns=0
        self.frame_buttons.rowconfigure(0,weight=1)
        for item_button in _list_buttons:
            item_button.grid(row=0,column=button_columns)
            self.frame_buttons.columnconfigure(button_columns,weight=1)
            button_columns+=1
        if(not self.text_frame):
            self.frame_content.destroy()
        self.root.mainloop()

    @key_check
    def add_input(self,key,label_name,passw=False):
        _frame = Frame(self.frame_entries)
        _label = Label(_frame, text=label_name, width=10, padx=5)
        if passw:
            self.entries[key] = Entry(_frame,font=("Helvetica",18),show= '*')
        else:
            self.entries[key] = Entry(_frame, font=("Helvetica", 18))

    @key_check
    def add_combobox(self,key,label_name,list_values):
        _frame = Frame(self.frame_entries)
        _label = Label(_frame,text=label_name,width=10,padx=5)
        self.entries[key] = ttk.Combobox(_frame,font=("Helvetica",18))
        self.entries[key]["values"] = list_values
        self.entries[key]["state"] = 'readonly'

    def add_checkbox(self,key,label,label_name,onchange=None):
        _frame = Frame(self.frame_entries)
        self.entries[key] = Checkbutton(_frame,text=label_name,command = onchange)

    def add_text(self):
        text_scroll = Scrollbar(self.frame_content,orient='vertical')
        hor_scroll = Scrollbar(self.frame_content, orient='horizontal')
        self.text_frame = Text(self.frame_content, yscrollcommand=text_scroll.set, wrap=None,xscrollcommand=hor_scroll.set())
        text_scroll.config(command=self.text_frame.yview)
        hor_scroll.config(command=self.text_frame.xview)
        self.text_frame.grid(column=0,row=0,sticky=(N,S,E,W))
        text_scroll.grid(column=1,row=0,sticky=(N,S,E))
        hor_scroll.grid(column=1,row=0,sticky=(N,S,W))
        self.frame_content.rowconfigure(0,weight=1)
        self.frame_content.columnconfigure(0,weight=1)
        self.text_frame.config(state=DISABLED)

    @key_check
    def add_button(self,key,label,f=None):
        self.buttons[key] = Button(self.frame_buttons,text=label,font=("Helvetica",20),fg="#3a3a3a",command=F)

    def clear_field(self,key):
        self.entries[key].delete(0,END)

    def clear_text(self):
        self.text_frame.config(state=NORMAL)
        self.text_frame.delete(0.0,END)
        self.text_frame.config(state=DISABLED)

    def add_text_content(self,content):
        self.text_frame.config(state=NORMAL)
        if content:
            self.text_frame.insert(INSERT,content)
        self.text_Frame.config(state=DISABLED)

    def get_input_value(self,key):
        return self.entries[key].get()

    def remove_field(self,key):
        self.entries[key].destroy()


if __name__ == "__main__":
    new_interface = Linterface()
    new_interface.title = "Application"
    new_interface.add_input("inp1","Input")
    new_interface.add_input("inp2", "Input")
    new_interface.start()
