#!/etc/bin/env python
# -*- coding: utf-8 -*-
#

from Tkinter import Label, Button, END
from Tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')	# asserts that Tix module is available to the application

lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number:', integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'cat', 'hamster', 'python'):
	cb.insert(END, animal)
	
cb.pack()

qb = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()

