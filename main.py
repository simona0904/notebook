from notebook import Notebook

my_notebook = Notebook(50, "blue", 
    ["Day one", "Day two",])
print(my_notebook.empty_pages())
print(my_notebook.written_pages())

my_notebook.write_to_notebook("Day three")
print(my_notebook.empty_pages())
print(my_notebook.written_pages())

