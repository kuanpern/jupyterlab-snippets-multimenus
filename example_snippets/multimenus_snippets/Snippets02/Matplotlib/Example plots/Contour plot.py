# Silly example data
x_min, x_max, y_min, y_max = 0.0, 2*np.pi, 0.0, 2*np.pi
f = [[np.sin(x**2 + y**2) for x in np.linspace(x_min, x_max, num=200)]
     for y in np.linspace(y_min, y_max, num=200)]

# Make the plot
plt.figure()
plt.imshow(f, interpolation="bicubic", origin="lower",
           extent=[x_min, x_max, y_min, y_max])
plt.colorbar()
plt.title(r"Title here (remove for papers)")
plt.xlabel(r"Description of $x$ coordinate (units)")
plt.ylabel(r"Description of $y$ coordinate (units)")
plt.show()