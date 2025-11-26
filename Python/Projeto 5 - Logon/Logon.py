from customtkinter import *
from tkinter import messagebox
from PIL import Image
import pandas as pd
import subprocess
import datetime
import hashlib

def SenhaHash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()    

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry('+{}+{}'.format(x, y))

def Register():
    global df
    user  = entryuser.get().strip()
    password = entrypassword.get().strip()

    if not user or not password:
        messagebox.showwarning("Aviso", "Digite o seu nome de usuário e senha para registrar!")
        return

    if user in df['User'].values:
        messagebox.showerror("Erro", "Nome de usuário já existente. Tente outro.")
        return

    new_data = pd.DataFrame([[user, SenhaHash(password)]], columns=["User", "Password"])
    df = pd.concat([df, new_data], ignore_index=True)

    try:
        df.to_excel("C:/Users/User/Desktop/Cds/Programas para Project/logon/Users.xlsx", index=False)
        messagebox.showinfo("Registrado", f"Usuario {user} registrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar os dados: {str(e)}")

def Confirm(event=None):
    global User
    global logged
    User = entryuser.get().strip()
    password = entrypassword.get().strip()

    if not User or not password:
        messagebox.showwarning("Aviso","Digite o seu nome de usuario e senha!")
        return

    if ((df['User'] == User) & (df['Password'] == SenhaHash(password))).any():
        current_datetime = datetime.datetime.now()
        LoginTime = current_datetime.strftime("%H:%M:%S")
        print(f"[{LoginTime}] Login bem-sucedido de {User}!")
        logged = True
        frame.pack_forget()
        app.title(f"Info de {User}")
        app.unbind('<Return>')
        Inside()

    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def Abrirxl():
    caminho_arquivo = "C:/Users/User/Desktop/Cds/Programas para Project/logon/Users.xlsx"
    if os.path.exists(caminho_arquivo):
        try:
            subprocess.run(['start', caminho_arquivo], shell=True)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo. Erro: {e}")
    else:
        messagebox.showerror("Erro", "Arquivo não encontrado!")

def Logout():
    global User
    global logged
    logged = False
    InsideFrame.pack_forget()
    frame.pack(anchor="center", expand=True)
    app.title("Login")
    app.bind('<Return>', Confirm)
    buttonLogout.pack_forget()
    buttonDB.pack_forget()
    entryuser.delete(0,END)
    entrypassword.delete(0,END)
    current_datetime = datetime.datetime.now()
    LogoutTime = current_datetime.strftime("%H:%M:%S")
    print(f"[{LogoutTime}] Deslogando de {User}!")
    User = ""
    
def Inside():
    global User
    global logged
    InsideTitle.configure(text=(f"Bem vindo(a) {User}!"))
    InsideFrame.pack(fill="both", expand=True, padx=10, pady=(10,0))
    buttonLogout.pack(side=RIGHT, anchor="se",padx=15, pady=10)

    if logged and User=="admin":
        buttonDB.pack(side=LEFT, anchor="sw",expand=True,padx=15,pady=10)

app = CTk()
app.title("Login")
app.geometry("480x600")
app.configure(fg_color="#f5f2eb")
User = ""
logged = False

try:
    df = pd.read_excel("C:/Users/User/Desktop/Cds/Programas para Project/logon/Users.xlsx", dtype={"Password": str}) 
    print("Base de dados de usuarios conectada com sucesso!")

except FileNotFoundError:
    df = pd.DataFrame([{"User": "admin", "Password": SenhaHash(str(123))}])
    try:
        df.to_excel("C:/Users/User/Desktop/Cds/Programas para Project/logon/Users.xlsx", index=False)
        print("Arquivo de usuários não encontrado. Novo criado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar arquivo de usuários: {str(e)}")

icon_confirm = CTkImage(Image.open("C:/Users/User/Desktop/Cds/Programas para Project/logon/confirm.png"), size=(18, 18))
icon_register = CTkImage(Image.open("C:/Users/User/Desktop/Cds/Programas para Project/logon/register.png"), size=(18, 18))
icon_logout = CTkImage(Image.open("C:/Users/User/Desktop/Cds/Programas para Project/logon/logout.png"), size=(18, 18))
icon_db = CTkImage(Image.open("C:/Users/User/Desktop/Cds/Programas para Project/logon/db.png"), size=(18, 18))
icon_title = CTkImage(Image.open("C:/Users/User/Desktop/Cds/Programas para Project/logon/login.png"), size=(18, 18))

frame = CTkFrame(master=app, fg_color="#EAE4D5",border_color="#B6B09F",border_width=2)
frame.pack(anchor="center", expand=True)

label = CTkLabel(master=frame, text=" LOGIN", height=25, font=('Calisto MT',16,'bold'),image=icon_title,compound="left", text_color="#000000")
label.pack(anchor="n", padx=30, pady=(20,10))

entryuser = CTkEntry(master=frame, placeholder_text="User name",width=250)
entryuser.pack(anchor="center", padx=30, pady=(5,2))

entrypassword = CTkEntry(master=frame, placeholder_text="Password", width=250, show="*")
entrypassword.pack(anchor="center", padx=30, pady=(2,15))

buttonLogin = CTkButton(master=frame, text="Connect", width=100, height=35, command=Confirm,
                        fg_color="#66B3A4", hover_color="#4C9C8F", text_color="#FFFFFF",
                        image=icon_confirm, compound="left")
buttonLogin.pack(side=LEFT, anchor="s", padx=(45,0), pady=(0,10))

buttonRegister = CTkButton(master=frame, text="Register", width=100, height=35, command=Register,
                           fg_color="#66B3A4", hover_color="#4C9C8F", text_color="#FFFFFF",
                           image=icon_register, compound="left")
buttonRegister.pack(side=RIGHT, anchor="s", padx=(0,45), pady=(0,10))

buttonLogout = CTkButton(master=app, text="Logout", width=60, height=35, command=Logout,
                         fg_color="#6E6E6E", hover_color="#4C4C4C", text_color="#FFFFFF",
                         image=icon_logout, compound="left")

buttonDB = CTkButton(master=app, text="xl_db", width=60, height=35, command=Abrirxl,
                     fg_color="#FF9F1C", hover_color="#FF7F00", text_color="#FFFFFF",
                     image=icon_db, compound="left")

InsideFrame = CTkFrame(master=app, fg_color="#EAE4D5",border_color="#B6B09F",border_width=2)

InsideTitle = CTkLabel(master=InsideFrame, font=('Calisto MT',16,'bold'))
InsideTitle.pack(anchor="nw", padx=15, pady=(15, 2))

Tabs = CTkTabview(master=InsideFrame)
Tabs.pack(fill="both", expand=True, padx=15, pady=(0, 15))

Tabs.add("Notas")
Tabs.add("Outros")
Tabs.add("Configurações")
Tabs.set("Notas")

TextInside = CTkTextbox(master=Tabs.tab("Notas"), font=('Calisto MT',15))
TextInside.pack(fill="both",expand=True,padx=5,pady=(0,5))

app.bind('<Return>', Confirm)
app.after(20, lambda: center_window(app)) 
app.mainloop()