"""
Вариант - 7
Red Hat OpenShift; Репозиторий: github.com/openshift/origin*
"""
import json
import requests
from tkinter import*
def buttonAction():
    with open("D:\\Практические\\Задание 11\\ffwd.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        enum = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in enum:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Data recorded has been SUCCESSFULLY")
root = Tk()
root.title('GIT request')
root.geometry('600x300')
root["bg"] = "blue"

head = Label(root, bg = "blue", fg = "gold", text = 'Введите никнейм', font = ('Franklin Gothic Medium', 22))
head.pack(expand=True)
txtField = Entry(root,width=40,font=('Franklin Gothic Medium', 18))
txtField.pack(expand=True)
button = Button(root, bg = "blue", fg = "gold", text = 'CLICK ON ME',command = buttonAction)
button.pack(expand=True)

root.mainloop()