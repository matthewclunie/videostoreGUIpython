"""
Program: videostoreGUI.py
Author: Matthew 11/10/2021


*** Note: the file breezypythongui.py MUST be in the
same directory as this file for the application to work
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class videostoreGUI(EasyFrame):
	def __init__(self):
		"""Sets up the window and the widgets."""

		EasyFrame.__init__(self, title = "Video Store", width = 380, height = 260, background = "DarkSeaGreen")
		self.addLabel(text = "Welcome to Five Star Retro Video", row = 0, column = 0, columnspan = 2, background = "DarkSeaGreen", font = Font(family = "Times New Roman", size = 18))
		self.addLabel(text = "Price for Old Videos: $2.00", row = 1, column = 0, background = "DarkSeaGreen")
		self.addLabel(text = "Price for New Videos: $5.00", row = 2, column = 0, background = "DarkSeaGreen")
		self.addLabel(text = "No. of old videos:", row = 3, column = 0, background = "DarkSeaGreen")
		self.oldRental = self.addIntegerField(value = 0, row = 3, column = 1)
		self.addLabel(text = "No. of new videos:", row = 4, column = 0, background = "DarkSeaGreen")
		self.newRental = self.addIntegerField(value = 0, row = 4, column = 1)
		self.addButton(text = "Calculate", row = 5, column = 0, columnspan = 2, command = self.compute)
	

	def compute(self):
		"""Calculates the total price."""

		#The initial prices of the videos.
		OLD_VIDEO = 2.00
		NEW_VIDEO = 5.00

		#Grabs the input values from the entry fields.
		oldNum = self.oldRental.getNumber()
		newNum = self.newRental.getNumber()

		#Calculation Phase.
		totalCost = (NEW_VIDEO * newNum) + (OLD_VIDEO * oldNum)


		#Output the video quantities to the output statement
		self.messageBox(message = "You got " + str(oldNum) + " old movies. You got " + str(newNum) + " new movies. The total cost is: $" + str(format(totalCost,".2f")))

#Definition of the main() function for program entry
def main(): 
	"""Instantiates and pops up the window."""
	videostoreGUI().mainloop()

#Global call to trigger the main function
if __name__ == "__main__":
	main()


