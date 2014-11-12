#########################################
#
#         85pt - Boundary detection
#
#########################################

# Add a button to move to the right and make them work as you'd expect (repeating lab12)
# This time - make sure that pressing left or right does nothing if you are going
# to hit a "boundary" - i.e. the edge of the screen.

from Tkinter import *
root = Tk()
# Create our drawpad and oval - use variables for our width and height so
# we can access them later on
drawpadwidth = 480
drawpadheight = 320
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		 #left button
       	        self.left = Button(self.myContainer1)
       	        self.left.configure(text="left", background= "blue")
       	        self.left.grid(row=2,column=0)
       	        # Bind an event to the first button
       	        self.left.bind("<Button-1>", self.leftClicked)
       	    
       	        #right button
       	        self.right = Button(self.myContainer1)
       	        self.right.configure(text="right", background= "red")
       	        self.right.grid(row=2,column=3)
       	        # Bind an event to the first button
       	        self.right.bind("<Button-1>", self.rightClicked)
		
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		 
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		
    
	
	# Add the button2Click method
		
myapp = MyApp(root)

root.mainloop()