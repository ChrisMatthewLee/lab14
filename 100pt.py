#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 5


class MyApp:

	
        def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		#up
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "white")
		self.up.grid(row=0,column=1)
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.upClick)
		
		#down
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "white")
		self.down.grid(row=3,column=1)
		# "Bind" an action to the first button												
		self.down.bind("<Button-1>", self.downClick)
		
		#left
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "white")
		self.left.grid(row=2,column=0)
		# "Bind" an action to the first button												
		self.left.bind("<Button-1>", self.leftClick)
		
		#right
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "white")
		self.right.grid(row=2,column=2)
		# "Bind" an action to the first button												
		self.right.bind("<Button-1>", self.rightClick)  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
                self.animateTarget()

        def animateTarget(self):
            global direction
            # Get the x and y co-ordinates of the circle
            x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > drawpad.winfo_width(): 
                direction = - 5
            elif x1 < 0:
                direction = 5
    #Move our oval object by the value of direction
            drawpad.move(target,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
            drawpad.after(1, self.animateTarget)
        
        

	

		
	def upClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if y1 > 0:
		  drawpad.move(player,0,-10)

        def downClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if y2 < 320:
		  drawpad.move(player,0,10)
		  
	def leftClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if x1 > 0:
		  drawpad.move(player,-10,0)

        def rightClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global drawpadwidth 
		global drawpadheight 
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
		if x2 < drawpad.winfo_width():
		  drawpad.move(player,10,0)



                if (x1 >= targetx1 and x2 <= targetx2) and (y1 >= targety1 and y2 <= targety2):
	            drawpad.itemconfig(target,fill='red')
	        else:
	            drawpad.itemconfig(target,fill='blue')

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)

                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()