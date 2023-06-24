# RDAITA2 SOFTWARE FOR EDUCATION \
# Librery 
from pytube import YouTube,Playlist
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as MSB
import os
from os import listdir
from os.path import  isfile ,join
import json
import re

from urllib import request

# json read data 
with open("Log/data.json")as f:
    data=json.load(f)
ver_data=(data["Version"])
build_data=(data["build"])
code_data=(data["Code_Name"])
Patch =(data["Patch"])
Patch_txt=re.sub("[']",'',Patch[0])

version=re.sub("[']","",ver_data[0])
build=re.sub("[']","",build_data[0])
code_name=re.sub("[']","",code_data[0])
# color system
bg0=(data["style_default"])
fg0 =(data["style_default"])
format_f=(data["Format"])
bg0_C=re.sub("[']","",bg0[0])
fg0_C=re.sub("[']","",fg0[1])

# main  software 
class main:
 
    def __init__(self,root) -> None:
        self.BT_start()
        self.title()
        self.Menu0()
       
        
        self.CK_internet=False
        
        self.format_file=re.sub("[']","",format_f[0])
        self.txt=tk.Label(root,text='URL: ',bg=bg0_C,fg=fg0_C)
        self.txt.place(x=340,y=320)
        self.url= tk.Entry(root,bg=fg0_C,fg=bg0_C,borderwidth=0,font=("italy"))
        self.url.place(x=340,y=350,width=250)
    
    def Menu0(self):
      def sel_mp3():
           self.show_vall.set(False)
           mp3_val=self.show_vall1.get()
           if mp3_val == True:
                self.show_vall1.set(True)
                self.val_on0=0
                self.val_off0=1
                
           else:
                self.show_vall1.set(False)
                self.format_file=re.sub("[']","",format_f[0])
            
      def sel_wav():
           self.show_vall1.set(True)
          
           wav_val=self.show_vall.get()
           if wav_val == True:
                self.show_vall.set(True)
                self.val_on=1
                self.val_off=0
                self.format_file=re.sub("[']","",format_f[1])
              
              

           else:
                self.show_vall.set(False)

           
           
      self.show_vall1=tk.BooleanVar() # checkbutton mp3 boolean valor
      self.show_vall1.set(False)
      self.val_on0=0
      self.val_off0=1

      self.show_vall=tk.BooleanVar() # checkbutton wev boolean valor
      self.show_vall.set(False)
     

      self.val_on=1 # checkbutton wev boolean valor on
      self.val_off=0
      menu =tk.Menu(root)
      root.config(menu=menu)
      fileMenu = Menu(menu,bg="white",fg=fg0_C,borderwidth=0)
      second_fileMenu=Menu(fileMenu,bg="white",fg=fg0_C,borderwidth=0)
      second_fileMenu.add_checkbutton(label="mp3",onvalue=self.val_on0,offvalue=self.val_off0,variable=self.show_vall1,command=sel_mp3)
      second_fileMenu.add_checkbutton(label="Wav",onvalue=self.val_on,offvalue=self.val_off,variable=self.show_vall,command=sel_wav)
      fileMenu.add_command(label= "Info",command=self.info)
      menu.add_cascade(label="Menu", menu=fileMenu)
      fileMenu.add_separator(background=bg0_C)
      fileMenu.add_cascade(label="Setting Format file",menu=second_fileMenu)
       

         
        
         
    def info(self):
         MSB.showinfo(title='Info software ',message="Author : Pop Mario Denis (RDAITA2)   ")
         
    def  BT_CANCEL(self):
           
        def CANCEL():
            self.bt.destroy()
            self.bt_c.destroy()
            self.BT_start()
            self.url.configure(state='normal')
            self.url.delete(0,'end')
        self.bt_c=tk.Button(root,text='Cancel',font=('Italy',16),command=CANCEL,borderwidth=0,bg=bg0_C,fg=fg0_C,activebackground=fg0_C,activeforeground=bg0_C)
        self.bt_c.place(x=470,y=400,height=40,width=150)

    def START(self):
      
        self.url.configure(state='disabled')
        self.bt_st.destroy()
        self.BT_CANCEL()
        self.DOWN()
        
    def BT_start(self):

        self.bt_st=tk.Button(root,text='Start',font=('Italy',16),command=self.START,borderwidth=0,bg=bg0_C,fg=fg0_C,activebackground=fg0_C,activeforeground=bg0_C)
        self.bt_st.place(x=390,y=400,height=40,width=150)

    def title(self):
        txt=tk.Label(root,text='YouTube Download Felix version 0.1-DEMO',font=("italy",20),bg=bg0_C,foreground=fg0_C) 
        txt.place(x=200,y=40)

         
         
    def pyTB(self):
       
            self.link=self.url.get()
            if self.link == '' :
                ERROR_Url=MSB.showerror(message='Error URL: not found')
        
            else:
           
                        
                try:      
                        yt=YouTube(self.link)
                        self.title0=yt.title
                     

                        
                        MSB.showinfo(message="""DO NOT TOUCH UNTIL THE BUTTON DOWNLOAD  IS MISSED
                        
                        INFO:Download File Format %s
                        title:%s
                        DIR Pach:%s
                                
                        
                        """%(self.format_file,self.title0,Patch_txt))
                        
                     
                     
                      
                        yt_s=yt.streams.filter(only_audio=True)
                        yt_s=yt_s.first()
                        out_file=yt_s.download(Patch_txt)
                        base ,ext =os.path.splitext(out_file)

                        new_file=base +self.format_file
                        os.rename(out_file,new_file)

                        self.bt.destroy()
                except:
                     MSB.showerror(message='ERRORS:  network or wrong syntax')
                     
                       
                        
                       

                        

                    
               
                        
                
            
       



    
   
    def DOWN(self):
        self.bt=tk.Button(root,text='Download',font=('Italy',16),command=self.pyTB,borderwidth=0,bg=bg0_C,fg=fg0_C,activebackground=fg0_C,activeforeground=bg0_C)
        self.bt.place(x=300,y=400,height=40,width=150)

        

    pass




root=tk.Tk()
root.geometry('900x700')
root.resizable(False,False)
root.title('YouTube DOWNLOAD code name: %s, Version: %s  Build :%s'%(code_name,version,build))
root.configure(bg=bg0_C)


if __name__ == "__main__":
    Main=main(root)
    root.mainloop()
