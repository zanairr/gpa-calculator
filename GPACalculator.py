import tkinter as tk
from tkinter import messagebox

class MyGui:
    def __init__(self):
        self.gpaUnitsList = []
        self.unitWeightList = []
        self.font = ('Elephant', 14)
        self.canCalculate = False

        self.root = tk.Tk()
        self.root.geometry('500x400')
        self.root.title('University of Alberta Engineering GPA Calculator')

        self.label = tk.Label(self.root, text= 'Letter grade:',font=self.font)
        self.label.place(x=10,y=30)
        self.label2 = tk.Label(self.root,text='Unit weight:',font=self.font)
        self.label2.place(x=10,y=85)

        self.textBox = tk.Text(self.root, height = 1,width = 20)
        self.textBox.place(x=10,y=57)
        self.weightText = tk.Text(self.root,height=1, width = 20)
        self.weightText.place(x=10,y= 110)

        self.addBtn = tk.Button(self.root,text='next', height = 1, width = 3, font= self.font, command=self.AddEntry)
        self.addBtn.place(x=175,y=50)
        self.calcBtn = tk.Button(self.root,text = 'calculate', height = 1, width = 9, font = self.font, command = self.CalcButton)
        self.calcBtn.place(x=250,y=50)
        self.newGpaBtn = tk.Button(self.root,text='calculate another gpa',height = 1, width = 17, font= self.font, command= self.CalcNewGPA)
        self.newGpaBtn.place(x = 175, y = 105)

        messagebox.showinfo(message='Instructions:\n\nplease enter the appropriate letter grade you received with its corresponding unit weight, eg: A- and 4.3. To add the results from another class press next after each entry. Once you have added all relevant information, press the calculate button to view your GPA. If you would like to calculate another GPA, press the calculate new GPA button to clear old information.')
        self.root.mainloop()
    def AddEntry(self):
        letterGradeEntry = self.textBox.get('1.0',tk.END)
        unitWeightEntry = self.weightText.get('1.0',tk.END)
        letterGradeEntry = letterGradeEntry.capitalize()

        letterToGpaDict = {
            'A+\n':4.0,
            'A\n':4.0,
            'A-\n':3.7,
            'B+\n':3.3,
            'B\n':3.0,
            'B-\n':2.7,
            'C+\n':2.3,
            'C\n':2.0,
            'C-\n':1.7,
            'D+\n':1.3,
            'D\n':1.0,
            'F\n':0     
        }
        if letterGradeEntry in letterToGpaDict.keys() and unitWeightEntry.strip('\n').replace('.','').isnumeric():
            num = letterToGpaDict[letterGradeEntry]
            self.gpaUnitsList.append(num*float(unitWeightEntry))
            self.unitWeightList.append(float(unitWeightEntry))
            self.canCalculate = True
        elif letterGradeEntry == '\n' and unitWeightEntry == '\n':
            self.canCalculate = True
        else:
            messagebox.showerror(message="Couldn't add this entry")
            self.canCalculate =False
        self.textBox.delete('1.0',tk.END)
        self.weightText.delete('1.0',tk.END)

    def CalcButton(self):
        self.AddEntry()
        gpaUnitSum = 0
        unitWeightSum = 0
        if self.canCalculate and len(self.unitWeightList) > 0:
            for x in self.unitWeightList:
                unitWeightSum +=float(x)
            for x in self.gpaUnitsList:
                gpaUnitSum +=float(x)
            messagebox.showinfo('average',message='GPA: ' + str(round(gpaUnitSum/unitWeightSum,2)))
        else:
            messagebox.showerror(message='Please enter at least one valid entry before attempting to calculate.')
    def CalcNewGPA(self):
        self.unitWeightList.clear()
        self.gpaUnitsList.clear()
    
MyGui()