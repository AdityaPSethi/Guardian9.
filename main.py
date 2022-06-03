#EVENT REGISTRATION EVENT


import tkinter as tk
Mainscreen=tk.Tk()
Mainscreen.title("EVENT REGISTRATION")
#CANVAS
Mainscreen_canvas=tk.Canvas(Mainscreen,width=550,height=525,bg="SlateBlue2")
Mainscreen_canvas.pack()
#LABEL1
Name_label=tk.Label(Mainscreen,text="Name:")
Name_label.config(font=("MicrosoftYaHei",11,"italic"),bg="SlateBlue2",fg="White")
Mainscreen_canvas.create_window(80,69,window=Name_label)
#LABEL2
Age_label=tk.Label(Mainscreen,text="Age:")
Age_label.config(font=("MicrosoftYaHei",11,"italic"),bg="SlateBlue2",fg="White")
Mainscreen_canvas.create_window(80,118,window=Age_label)
#LABEL3
Phone_label=tk.Label(Mainscreen,text="Phone")
Phone_label.config(font=("MicrosoftYaHei",11,"italic"),bg="SlateBlue2",fg="White")
Mainscreen_canvas.create_window(80,167,window=Phone_label)
#LABEL4
Email_label=tk.Label(Mainscreen,text="Email")
Email_label.config(font=("MicrosoftYaHei",11,"italic"),bg="SlateBlue2",fg="White")
Mainscreen_canvas.create_window(80,217,window=Email_label)
#LABEL5
Remove_opt=tk.Label(Mainscreen,text="Delete registration number")
Remove_opt.config(font=("MicrosoftYaHei",12,"bold"),bg="SlateBlue2",fg="White")
Mainscreen_canvas.create_window(180,480,window=Remove_opt)
RegistrationNoField=tk.Text(Mainscreen,height=1,width=1,font=('LucidaConsole'))
Mainscreen_canvas.create_window(330,480,window=RegistrationNoField)
#ENTRY1
Name_entry=tk.Entry(Mainscreen,width=25,font=("LucidaConsole",12,"bold"),bg="LightSalmon2",fg="White")
Mainscreen_canvas.create_window(280,69,window=Name_entry)
#ENTRY2
Age_entry=tk.Entry(Mainscreen,width=25,font=("LucidaConsole",12,"bold"),bg="Salmon3",fg="White")
Mainscreen_canvas.create_window(280,118,window=Age_entry)
#ENTRY3
Phone_entry=tk.Entry(Mainscreen,width=25,font=("LucidaConsole",12,"bold"),bg="Salmon3",fg="White")
Mainscreen_canvas.create_window(280,167,window=Phone_entry)
#ENTRY4
Email_entry=tk.Entry(Mainscreen,width=25,font=("LucidaConsole",12,"bold"),bg="LightSalmon2",fg="White")
Mainscreen_canvas.create_window(280,217,window=Email_entry)
#TEXT AREA1
TextArea=tk.Text(Mainscreen,height=5,width=40,font=("LucidaConsole"),bg="LightGrey",fg="Black")
Mainscreen_canvas.create_window(275,379,window=TextArea)
#BUTTON1
Submit_button=tk.Button(text="SUBMIT",command="InsertTask",font=("MicrosoftYaHei",16,"bold","italic"),bg="MidnightBlue",fg="CadetBlue")
Mainscreen_canvas.create_window(275,269,window=Submit_button)
#BUTTON2
Delete_button=tk.Button(text="DELETE",command="deleteTask",font=("MicrosoftYaHei",16,"bold","italic"),bg="MidnightBlue",fg="CadetBlue")
Mainscreen_canvas.create_window(450,480,window=Delete_button)
#VARIABLES
counter=0
RegistrationList=[]
#DEFINE- InsertTask
def InsertTask():
  global counter
  if Name_entry.get()!= "" and Age_entry.get()!="" and Phone_entry.get()!='' and Email_entry.get()!="":
    Content=Name_entry.get()+'|'+Age_entry.get()+"|"+Phone_entry.get()+"|"+Email_entry.get()+'|'+'\n'+"\n"
    RegistrationList.append(Content)
    TextArea.insert("end -1 chars","["+str(counter)+"]"+ Content)
    counter+=1
    Name_entry.delete(0,-1)
    Age_entry.delete(0,-1)
    Phone_entry.delete(0,-1)
    Email_entry.delete(0,-1)
def deleteTask():
  global counter
  Number=RegistrationNoField.get(1.0,-1)
  taskNo=int(Number)
  RegistrationNoField.delete(0.0,-1)
  RegistrationList.pop(taskNo - 1)
  counter-=1
  TextArea.delete(1.0,-1)
  for i in range(len(RegistrationList)):
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] "+RegistrationList[i])
Mainscreen.mainloop()