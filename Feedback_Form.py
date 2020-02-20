
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):    
        
        #setting the title o thee root window
        master.title('Feedback Form')

        #setting the title o thee root window
        master.resizable(False,False)

        #setting the geometry of the root window
       # master.geometry('600x600')

        #setting the background of the root window
        master.config(background = 'beige')

        #creating the style object
        self.style = ttk.Style()
        self.style.configure('TFrame' , background = 'beige')
        self.style.configure('TButton' , background = 'beige')
        self.style.configure('TLabel' , background = 'beige',font = ('Arial' , 12))
        self.style.configure('Header.TLabel' , font = ('Arial' , 18 , 'bold' ))

        #creating the header frame
        self.frame_header = ttk.Frame(master)

        #creating the logo 
        self.logo = PhotoImage(file = 'C:\Python\\tour_logo.gif')

        #creating childs of first frame
        ttk.Label(self.frame_header , image = self.logo).grid(row = 0 ,column = 0 ,padx = 8 )
        ttk.Label(self.frame_header , text = 'Thanks for Exploring',  style = 'Header.TLabel').grid(row = 0 ,column = 1 , padx = 8)
        ttk.Label(self.frame_header , text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.") , wraplength = 300 ).grid(row = 1 ,column = 1,padx = 8)

        #creating the content frame 
        self.frame_contents = ttk.Frame(master)

        #creating the labels for content frame
        ttk.Label(self.frame_contents, text='Name :',  foreground = 'Brown' , background = 'beige' ).grid(row = 0 ,column = 0 , padx= 8 ,sticky = 'sw' )
        ttk.Label(self.frame_contents, text = 'Email :', foreground = 'Brown' , background = 'beige').grid(row = 0 ,column = 1 , padx = 8, sticky = 'sw')
        ttk.Label(self.frame_contents, text='Comments :',  foreground = 'Brown' , background = 'beige').grid(row = 2 ,column = 0 , padx = 8, sticky = 'sw')

        #creating the Entry variables
        self.name = ttk.Entry(self.frame_contents, width = 24 )
        self.email = ttk.Entry(self.frame_contents, width = 24 )

        #Creating the text entry widgets
        self.text = Text(self.frame_contents, width = 50 , height = 10, font = ('Arial' , 12))

        #creating the buttons
        self.submit = ttk.Button(self.frame_contents, text = 'Submit' , command = self.submit)
        self.clear = ttk.Button(self.frame_contents, text = 'Clear',command = self.clear_text)

        #Placing the widgets on the screen
        self.frame_header.pack()
        self.frame_contents.pack()
        
        self.name.grid(row = 1 , column = 0, padx = 8 )
        self.email.grid(row= 1 , column = 1, padx = 8)
        self.text.grid(row = 3, column = 0, columnspan = 2, padx = 8)
        self.submit.grid(row = 4, column = 0, padx = 8 ,sticky = 'e')
        self.clear.grid(row = 4, column = 1, padx = 8 ,sticky = 'w')

    def submit(self):
        print('Name : {}'.format(self.name.get()))
        print('Email : {}'.format(self.email.get()))
        print('Comments : {}'.format(self.text.get(1.0 ,'end')))
        self.clear_text()
        messagebox.showinfo(title = 'Explore California Feedback' , message = 'Comments are successfully submitted')

    def clear_text(self):
        self.name.delete(0,END)
        self.email.delete(0,END)
        self.text.delete(1.0,END)
            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
