import numpy as np
import matplotlib.pyplot as plt

num_stars = 100000
radius = 300  
spiral_arms = 3 

theta = np.linspace(0, 2 * np.pi, num_stars)  
r = np.sqrt(np.random.rand(num_stars)) * radius  

theta += spiral_arms * np.sin(r / radius * 2 * np.pi)

x = r * np.cos(theta)
y = r * np.sin(theta)

colors = np.random.rand(num_stars, 3) 

plt.figure(figsize=(10, 10))
plt.scatter(x, y, c=colors, s=1, alpha=0.7)
plt.gca().set_facecolor('black')  
plt.axis('off') 
plt.title("Colorful Galaxy", fontsize=20, color='white')


plt.show()
