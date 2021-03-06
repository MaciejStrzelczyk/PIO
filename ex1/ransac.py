import numpy as np
from scipy.stats import norm
import random
from csv import writer

ERROR = 0.2                                         # dla płaszczyzny około 0,2, dla cylindra 0,8
EXPECTED_NUMBER_OF_INLIERS = 250


#def generate_points(num_points):                    # generating a flat point cloud
#
#    distribution_x = norm(loc=0, scale=40)
#    distribution_y = norm(loc=0, scale=20)
#    distribution_z = norm(loc=0, scale=1)
#    x = distribution_x.rvs(size=num_points)
#    y = distribution_y.rvs(size=num_points)
#    z = distribution_z.rvs(size=num_points)

#    point = zip(x, y, z)
#    points = []
#    points.extend(point)

#    return points


def get_random_points(points):                      # generowanie trzech punktów z chmury punktów
                                    #####################do zrobienia losowanie z listy
    lista = list(points)
    random_points = random.choices(lista, k=3)
    return random_points


def generate_plane(random_points):                  # wyznaczenie równania płaszczyzny
    a = random_points[0]
    b = random_points[1]
    c = random_points[2]

    vec_va = np.subtract(a, c)
    vec_vb = np.subtract(b, c)

    vec_ua = vec_va / np.linalg.norm(vec_va)
    vec_ub = vec_vb / np.linalg.norm(vec_vb)
    vec_uc = np.cross(vec_ua, vec_ub)               # wyznaczneie wektora Uc wynikiem jest lista z wx, wy, wz
    vec_ucc = []
    vec_ucc.extend(vec_uc)

    d = np.abs(np.sum(np.multiply(vec_uc, c)))      # wyzanczenie odległości d od płaszczyzny

    return vec_ucc, d


def fit_to_plane_all_points(points, vec_ucc, d):    # wyzanczenie odległości poszczególnych punktów
                                                    # od płaszczyzny i określenie jak do niej pasują

    wx = vec_ucc[0]
    wy = vec_ucc[1]
    wz = vec_ucc[2]
    distance_all_points = [(np.abs(wx * point[0] + wy * point[1] + wz * point[2] + d) / np.linalg.norm(vec_ucc)) for point in points]
    return distance_all_points


def get_inliers(distance_all_points):
    inliers = []
    for i in range(0, len(distance_all_points)):
        if distance_all_points[i] <= ERROR:
            inliers.append(i)
    return inliers

if __name__ == '__main__':
    i = []
    color = []
    open("cylindrical_cloud_points.xyz").read()
    vertical = np.genfromtxt("cylindrical_cloud_points.xyz", delimiter=',')
    open("cylindrical_cloud_points.xyz").close()

    while True:
        random_points = get_random_points(vertical)
        vec_ucc, d = generate_plane(random_points)
        distance_all_points = fit_to_plane_all_points(vertical, vec_ucc, d)
        i = get_inliers(distance_all_points)
        if len(i) >= EXPECTED_NUMBER_OF_INLIERS:
            average_distance_all_points = np.average(distance_all_points)

            inliers = [vertical[inlier] for inlier in i]
            inliers_x, inliers_y, inliers_z = zip(*inliers)

            xy_sum = abs(sum(inliers_x)) + abs(sum(inliers_y))
            yz_sum = abs(sum(inliers_y)) + abs(sum(inliers_z))
            xz_sum = abs(sum(inliers_x)) + abs(sum(inliers_z))

            if (xy_sum > xz_sum or xy_sum > yz_sum) and average_distance_all_points <= 1:
                print('this is a cloud of vertical plane')
            elif (yz_sum > xy_sum or xz_sum > xy_sum) and average_distance_all_points <= 1:
                print('\nthis is a cloud of horizontal plane')
            else:
                print('it is not a cloud of plane')
            break

    print("\nilość inliersów:")
    print(len(i))
    print("\nWektor W: ")
    print(vec_ucc)
    print("\n")

    with open('inliers.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in inliers:
            csvwriter.writerow(p)