# Silly example data
x = np.linspace(0.1, 4, num=10)
y = np.exp(-x)
dx = 0.1 - x/25.0
dy = 0.2 + x/15.0

# Make the plot
plt.figure()
plt.errorbar(x, y, xerr=dx, yerr=dy)
plt.title(r"Title here (remove for papers)")
plt.xlabel(r"Description of $x$ coordinate (units)")
plt.ylabel(r"Description of $y$ coordinate (units)")
plt.show()