import tkinter
from tkinter.constants import END



root = tkinter.Tk()
root.title("Temple Eats")
root.geometry("400x400")



#background color
root['background']='#FFFAF0'

#text
text = tkinter.Label(root, text="Hello! What Would You Like To Eat Today?",height = 5, bg="#FFFAF0")
text.place(x=100,y=0)

class Veg_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for c in range(total_columns):
                  self.e = tkinter.Entry(root,width=70, fg='blue',font=('Arial',12,'bold'),bg='#FFFAF0')
                  self.e.grid(row=r, column=c,)
                  self.e.insert(END, Veg_lst[r][c])

#window functions
def openwindow1():
    t = Veg_Table(root)
    root.geometry('1100x1500')

#take the data
Veg_lst = [('VEG RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('dev food truck','debit/credit/cash'),
('tommy lunch truck','debit/credit/cash'),
('little lulu','debit/credit/cash'),
('tasty eats','debit/credit/cash'),
('4 brothers','debit/credit/cash'),
('new york gyro','debit/credit/cash'),
('mountain pizza','debit/credit/cash'),
('philly halal gyro','debit/credit/cash'),
('mexican grill stand','debit/credit/cash'),
('halal gyro express','debit/credit/cash'),
('famous ny gyro','debit/credit/cash'),
('caribbean feast','debit/credit/cash'),
('sunny halal food','debit/credit/cash'),
('eddies','debit/credit/cash'),
('sexy green truck','debit/credit/cash'),
('cha cha','debit/credit/cash'),
('eppys truck','debit/credit/cash'),
('ernies','debit/credit/cash'),
('the fruit salad & smoothie truck','debit/credit/cash'),
('e&e gourmet express','debit/credit/cash'),
('chicken heaven','debit/credit/cash'),
('chop chop','debit/credit/cash'),
('fruit salad','debit/credit/cash'),
('kobawoo express','debit/credit/cash'),
('jamaican ds','debit/credit/cash'),
('philly fellas gyro halal','debit/credit/cash'),
('brother pizza','debit/credit/cash'),
('temple teppanyaki','debit/credit/cash'),
('foot long','debit/credit/cash'),
('honey','debit/credit/cash'),
('richie lunch box','debit/credit/cash'),
('cloud','debit/credit/cash'),
('samosa deb','debit/credit/cash'),
('top bap','debit/credit/cash'),
('ray truck','debit/credit/cash'),
('the creperie truck','debit/credit/cash'),
('burger tank','debit/credit/cash'),
('el guaco loco','debit/credit/cash'),
('korea house','debit/credit/cash'),
('vegan tree','debit/credit/cash'),
('subway','debit/credit/cash,diamond dollars'),
('zen','meal equivalency,debit/credit/cash,diamond dollars'),
('esposito dining center','meal plan,meal equivalency,debit/credit/cash,diamond dollars'),
('twisted taco','meal equivalency,debit/credit,cash,diamond dollars'),
('morgan dining hall','meal plan,meal equivalency,debit/credit,cash,diamond dollars'),
('burgerfi','meal equivalency,debit/credit/cash,diamond dollars'),
('saladworks','meal equivalency,debit/credit/cash,diamond dollars'),
('starbucks','debit/credit/cash,diamond dollars'),
('pita and Co.','meal equivalency,debit/credit/cash,diamond dollars'),
('panda express','meal equivalency,debit/credit/cash,diamond dollars'),
('jamba','debit/credit/cash'),
('java city','debit/credit/cash'),
('stella café','debit/credit/cash')]          

total_rows = len(Veg_lst)
total_columns = len(Veg_lst[0])

class Vegan_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for c in range(total_columns):
                  self.e = tkinter.Entry(root, width=70, fg='green',font=('Arial',12,'bold'))
                  self.e.grid(row=r, column=c)
                  self.e.insert(END, Vegan_lst[r][c])

def openwindow2():
    t = Vegan_Table(root)

Vegan_lst =[('VEGAN RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('dev food truck','debit/credit/cash'),
('new york gyro','debit/credit/cash'),
('mountain pizza','debit/credit/cash'),
('philly halal gyro','debit/credit/cash'),
('mexican grill stand','debit/credit/cash'),
('halal gyro express','debit/credit/cash'),
('famous ny gyro','debit/credit/cash'),
('sunny halal food','debit/credit/cash'),
('ernies','debit/credit/cash'),
('the fruit salad & smoothie truck','debit/credit/cash'),
('chicken heaven','debit/credit/cash'),
('fruit salad','debit/credit/cash'),
('philly fellas gyro halal','debit/credit/cash'),
('samosa deb','debit/credit/cash'),
('ray truck','debit/credit/cash'),
('vegan tree','debit/credit/cash'),
('subway','diamond dollars , debit/credit/cash'),
('esposito dining center','meal plan , meal equivalency , debit/credit/cash , diamond dollars'),
('twisted taco','meal equivalency , debit/credit/cash , diamond dollars'),
('morgan dining hall','meal plan , meal equivalency , debit/credit/cash , diamond dollars'),
('burgerfi','meal equivalency , debit/credit/cash , diamond dollars'),
('saladworks','meal equivalency , debit/credit/cash , diamond dollars'),
('starbucks','debit/credit/cash , diamond dollars'),
('pita and co.','meal equivalency , debit/credit/cash , diamond dollars'),
('panda express','meal equivalency , debit/credit/cash , diamond dollars'),
('jamba','debit/credit/cash'),
('java city','debit/credit/cash'),
('stella café','debit/credit/cash')]


total_rows = len(Vegan_lst)
total_columns = len(Vegan_lst[0])

class NonVeg_Table:
      
    def __init__(self,root):
          
        #code for creating table
        for r in range(total_rows):
            for c in range(total_columns):
                   self.e = tkinter.Entry(root, width=70, fg='red',font=('Arial',12,'bold'))
                   self.e.grid(row=r, column=c)
                   self.e.insert(END, NonVeg_lst[r][c])

def openwindow3():
    t = NonVeg_Table(root)
    root.geometry('1100x1500')


NonVeg_lst = [('NON-VEG RESTAURANTS','ACCEPTED PAYMENT TYPES'),
('dev food truck','debit/credit/cash'),
('tommy lunch truck','debit/credit/cash'),
('little lulu','debit/credit/cash'),
('tasty eats','debit/credit/cash'),
('4 brothers','debit/credit/cash'),
('new york gyro','debit/credit/cash'),
('mountain pizza','debit/credit/cash'),
('philly halal gyro','debit/credit/cash'),
('mexican grill stand','debit/credit/cash'),
('halal gyro express','debit/credit/cash'),
('famous ny gyro','debit/credit/cash'),
('caribbean feast','debit/credit/cash'),
('sunny halal food','debit/credit/cash'),
('eddies','debit/credit/cash'),
('sexy green truck','debit/credit/cash'),
('cha cha','debit/credit/cash'),
('eppys truck','debit/credit/cash'),
('ernies','debit/credit/cash'),
('e&e gourmet express','debit/credit/cash'),
('chicken heaven','debit/credit/cash'),
('chop chop','debit/credit/cash'),
('kobawoo express','debit/credit/cash'),
('jamaican ds','debit/credit/cash'),
('philly fellas gyro halal','debit/credit/cash'),
('brother pizza','debit/credit/cash'),
('temple teppanyaki','debit/credit/cash'),
('foot long','debit/credit/cash'),
('honey','debit/credit/cash'),
('richie lunch box','debit/credit/cash'),
('samosa deb','debit/credit/cash'),
('top bap','debit/credit/cash'),
('ray truck','debit/credit/cash'),
('burger tank','debit/credit/cash'),
('el guaco loco','debit/credit/cash'),
('korea house','debit/credit/cash'),
('esposito dining center','meal plan, meal equivalency, debit/credit/cash, diamond dollars'),
('morgan dining hall','meal plan, meal equivalency, debit/credit/cash, diamond dollars'),
('burgerfi','meal equivalency, debit/credit/cash, diamond dollars'),
('saladworks','meal equivalency, debit/credit/cash, diamond dollars'),
('which wich','meal equivalency, debit/credit/cash, diamond dollars'),
('chick-fil-a','meal equivalency, debit/credit/cash, diamond dollars'),
('twisted taco','meal equivalency, debit/credit/cash, diamond dollars'),
('panda express','meal equivalency, debit/credit/cash, diamond dollars'),
('bento sushi','meal equivalency, debit/credit/cash, diamond dollars'),
('così','debit/credit/cash'),
('zaydee kosher delicatessen','debit/credit/cash')]

total_rows = len(NonVeg_lst)
total_columns = len(NonVeg_lst[0])


#buttons 
button1= tkinter.Button(root, text='Vegetarian', width=30, height=3, command = openwindow1)
button1.pack()
button2 = tkinter.Button(root, text='Vegan', width=30, height=3,command = openwindow2)
button2.pack()
button3 = tkinter.Button(root, text='Non-Veg', width=30, height=3,command = openwindow3)
button3.pack()

#button postitions 
button1.place(x=50,y=100)
button2.place(x=50,y=175)
button3.place(x=50,y=250)


#Grid Options



root.mainloop()
