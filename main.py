import math
import numpy as np
from scipy.stats import norm
from csv import writer
#:int = 4000

def generate_points(num_points):
#generating a flat point cloud
    #distribution_x = norm(loc=0, scale=40)
    #distribution_y = norm(loc=0, scale=20)
    #distribution_z = norm(loc=0, scale=100)
    #x = distribution_x.rvs(size=num_points)
    #y = distribution_y.rvs(size=num_points)
    #z = distribution_z.rvs(size=num_points)

#generating point cloud cyclone
    t = np.random.uniform(0.0, 2.0*np.pi, 10000)
    r = 1 * np.sqrt(np.random.uniform(0.0, 6.0, 10000))
    x = (r * np.cos(t))
    y = r *np.sin(t)
    z = np.random.uniform(0, 10, num_points)

    points = zip(x, y, z)
    return points


if __name__== '__main__':
    cloud_points = generate_points(100000)
    with open('Points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points:
            csvwriter.writerow(p)