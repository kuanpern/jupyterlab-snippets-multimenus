# Silly example data
bp_x1 = np.linspace(0, 2*np.pi, num=40, endpoint=True)
bp_y1 = np.sin(bp_x1)
bp_x2 = np.linspace(0, np.pi, num=40, endpoint=True)
bp_y2 = np.cos(bp_x2)

# Make the plot
fig, (ax1, ax2) = plt.subplots(ncols=2)
ax1.plot(bp_x1, bp_y1, linewidth=3, linestyle="--",
         color="blue", label=r"Legend label $\sin(x)$")
ax1.set_xlabel(r"Description of $x_{1}$ coordinate (units)")
ax1.set_ylabel(r"Description of $y_{1}$ coordinate (units)")
ax1.set_title(r"Title 1 here (remove for papers)")
ax1.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1.1, 1.1)
ax1.legend(loc="lower left")
ax2.plot(bp_x2, bp_y2, linewidth=3, linestyle="--",
         color="blue", label=r"Legend label $\cos(x)$")
ax2.set_xlabel(r"Description of $x_{2}$ coordinate (units)")
ax2.set_ylabel(r"Description of $y_{2}$ coordinate (units)")
ax2.set_title(r"Title 2 here (remove for papers)")
ax2.set_xlim(0, np.pi)
ax2.set_ylim(-1.1, 1.1)
ax2.legend(loc="lower left")
plt.show()