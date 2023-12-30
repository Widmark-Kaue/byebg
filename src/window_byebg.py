import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
from pathlib import Path

from rembg import remove
from PIL import Image

class Tela:
    def __init__(self, master) -> None:
        self.PATH_EXE = Path().absolute()
        self.images = []
        
        self.nossaTela  = master
        self.barra_menu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu = self.barra_menu)
        
        self.barra_menu.add_command(label="Carregar arquivos", command=self.carregarArquivos)
        
        self.button = tk.Button(self.nossaTela, 
                                text='Executar', bd = '5', command=self.removerFundo)
        self.button.pack(side = 'bottom')
        pass
    
    def carregarArquivos(self)-> None:
        self.images = fd.askopenfilenames(
            initialdir=self.PATH_EXE.as_posix(),
            title="Selecione uma ou mais imagens",
            filetypes=[("Arquivo de Imagem", ["*.jpg", "*.jpeg", "*.png"])],
            )
        if self.images:
            mb.showinfo(message='Carregamento completo!')
        
        
    
    def removerFundo(self) -> None:
        if self.images:
            for img in self.images:
                img_path = Path(img)
                try:
                    outputpath = img_path.with_name(f'{img_path.stem}_byebg.png')
                    self.byebg(img, outputpath=outputpath.as_posix())
                except Exception as e:
                    var = f'Erro do tipo: {type(e)}\nArgumentos: {e.args}\n{e}'
                    mb.showerror(message=var)

            mb.showinfo(message='Execução completa!')      
        else:
            mb.showwarning(message='Não há imagens carregadas!')                    
        
    def byebg(self, input_path, outputpath):
        original_img = Image.open(input_path)
        no_bg_img = remove(original_img)
        no_bg_img.save(outputpath)
        

janelaRaiz = tk.Tk()
janelaRaiz.title('Remover background')
janelaRaiz.geometry('500x100')
Tela(janelaRaiz)
janelaRaiz.mainloop()