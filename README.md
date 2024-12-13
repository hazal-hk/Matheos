This is a calculator code written by me and this is my calculator's screen.

<img width="442" alt="Ekran görüntüsü 2024-12-13 212646" src="https://github.com/user-attachments/assets/6aae7e23-a7f3-4660-8ac9-790dc400187d" />

Now I will tell you all about the code I wrote.
Firstly, I created the main tkinter window
root = Tk()
root.title("CALCULATOR")

These are state variables.

expression = StringVar()
result = StringVar()

This is for display.

Label(root, font=('Times', 25, 'bold'), textvariable=expression, height=2).grid(columnspan=4, ipadx=120)

Label(root, font=('Times', 25, 'bold'), textvariable=result, height=2).grid(columnspan=4, ipadx=120)

These are for button click handler.


    def onButtonClick(entry):
      if entry == "AC":
    
        expression.set("")
        
        result.set("")
        
    elif entry == "=":
    
        try:
        
            res = eval(expression.get())
            
            result.set(res)
            
            expression.set(str(res))  # To allow further calculations
            
        except:
        
            result.set("Error")
            
            expression.set("")
            
    elif entry == "sqrt":
    
        try:
        
            res = math.sqrt(float(expression.get()))
            
            result.set(res)
            
            expression.set(str(res))
            
        except:
        
            result.set("Error")
            
            expression.set("")

            
    else:
    
        expression.set(expression.get() + str(entry))
        

This is for button labels and grid placement.




    buttons = [
    
    ("AC", "sqrt", "%", "/"),
    
    ("7", "8", "9", "*"),
    
    ("4", "5", "6", "-"),
    
    ("1", "2", "3", "+"),
    
    ("0", ".", "=", None) 
    
    ]
    

Then I created the buttons dynamically.
  
      for i, row in enumerate(buttons): 
       for j, text in enumerate(row):
    
        if text:
        
            Button(root, text=text, font=('Times', 15, 'bold'), padx=16, pady=16, height=2, width=9,
            
                   command=lambda t=text: onButtonClick(t)).grid(row=i + 3, column=j, sticky=E)


That's all.
                   

Finally, we should run the tkinter main loop.


root.mainloop()
