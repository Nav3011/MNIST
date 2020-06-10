import matplotlib.pyplot as plt

class Plot:
	def __init__(self):
		print("Plotting...")
	@staticmethod
	def visualize_digit(digit):
		#here digit is a list
		digit_matrix = list()
		digit = [float(i) for i in digit]
		for i in range(28):
			a = list(digit[28*i:28*(i+1)-1])
			digit_matrix.append(a)
		plt.imshow(digit_matrix, cmap="Greys", interpolation="None")
  		plt.show()
