# 1. Scrie o clasa care repr. o Agenda (Notebook).
# Atribute:
#     - nr pagini
#     - culoare
#     - continut - lista de stringuri ["continut pagina", "continut pag."]

# Metode:
#     - scrie in Agenda
#     - vezi nr de pag goale
#     - vezi nr pag scrise


class Notebook:


    def __init__(self, nr_of_pages, color, content):
        self.nr_of_pages = nr_of_pages
        self.color = color
        self.content = content


    def write_to_notebook(self, content):
        self.content.append(content)

    def empty_pages(self):   
        return self.nr_of_pages - len(self.content) 

    def written_pages(self):
        return len(self.content)    
         

    