import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
from csv import writer

num_points = 10000

def generates_horizontal_points(num_points):
    distribution_x = norm(loc=0, scale=20)
    distribution_y = norm(loc=0, scale=0.1)
    distribution_z = norm(loc=0, scale=40)
    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points


def generates_vertical_points(num_points):
    distribution_x = norm(loc=0, scale=0.1)
    distribution_y = norm(loc=0, scale=30)
    distribution_z = norm(loc=0, scale=20)
    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points


def generates_cylindrical_points(num_points):
    t = np.random.uniform(0, 2.0*np.pi, 10000)
    r = 1 * np.sqrt(np.random.uniform(0.0, 6.0, 10000))
    x = (r * np.cos(t))
    y = r *np.sin(t)
    z = np.random.uniform(0, 10, num_points)

    points = zip(x, y, z)
    return points


if __name__== '__main__':
    horizontal_cloud_points = generates_horizontal_points(num_points)
    vertical_cloud_points = generates_vertical_points(num_points)
    cylindrical_cloud_points = generates_cylindrical_points(num_points)

    with open('horizontal_cloud_points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in horizontal_cloud_points:
            csvwriter.writerow(p)

    with open('vertical_cloud_points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in vertical_cloud_points:
            csvwriter.writerow(p)

    with open('cylindrical_cloud_points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cylindrical_cloud_points:
            csvwriter.writerow(p)