from tkinter import *

class Toolbar:
  def __init__(
    self,
    master,
    root,
    on_add_new_node,
    on_sizes_click,
    on_degrees_click,
    on_remove_min_click,
    on_min_root_click,
    on_reset_click,
    on_remove_node_click
  ):
    # validate inputs
    vcmd = master.register(self.validate_num)
    self.vcmd = vcmd

    root.grid_columnconfigure(0, minsize=80)
    root.grid_columnconfigure(1, minsize=20)
    root.grid_columnconfigure(2, minsize=80)
    root.grid_columnconfigure(3, minsize=80)
    
    for i in range(0, 6):
      root.grid_rowconfigure(i, minsize=30)

    self.make_entry_field(
      root,
      label="Add nodes",
      btn_label="Add",
      submit_handler=on_add_new_node,
      row=0,
      column=0
    )
    
    self.make_entry_field(
      root,
      label="Remove nodes",
      btn_label="Remove",
      submit_handler=on_remove_node_click,
      row=3,
      column=0
    )

    # Sizes
    size_btn = Button(root, text="Sizes", command=on_sizes_click)
    size_btn.grid(row=1, column=2, sticky="WE") 

    # Degrees
    size_btn = Button(root, text="Degrees", command=on_degrees_click)
    size_btn.grid(row=2, column=2, sticky="WE") 

    # Min
    min_btn = Button(root, text="Min root", command=on_min_root_click)
    min_btn.grid(row=3, column=2, sticky="WE") 

    # Remove min
    size_btn = Button(root, text="Remove min", command=on_remove_min_click)
    size_btn.grid(row=1, column=3, sticky="WE") 

    # Reset
    reset_btn = Button(root, text="Reset", command=on_reset_click)
    reset_btn.grid(row=2, column=3, sticky="WE") 


  def make_entry_field(
    self,
    root,
    label,
    btn_label,
    submit_handler,
    row,
    column,
  ):
    Label(root, text=label).grid(row=row, column=column, sticky="W")
    entry = Entry(root, validate='all', validatecommand=(self.vcmd, '%P'), width=10)
    entry.grid(row=row+1, column=column, sticky="WENS")
    btn = Button(
      root,
      text=btn_label,
      command=self.on_entry_submit(entry, submit_handler),
    )
    btn.grid(row=row+2, column=column, sticky="WENS")

  def validate_num(self, str):
    return all(
      item == '' or item.isdigit() for item in str.split(",")
    )
  
  def on_entry_submit(self, entry, callback):
    def handle():
      entry_value = entry.get()
      if entry_value:
        str_values = filter(lambda x: x.isdigit(), entry_value.split(","))
        values = [int(item) for item in str_values]
        callback(values)
        entry.delete(0, END)
      
    return handle


