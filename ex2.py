# algorytm k-means

from sklearn.cluster import KMeans
import numpy as np

num_points = 10000;

divided_clusters = []
points1 = []
points2 = []
points3 = []


def divide_into_clusters(num_points, cloud):
    global C1
    global C2
    global C3
    clusterer = KMeans(n_clusters=3)
    X = np.array(cloud)
    y_pred = clusterer.fit_predict(X)
    y_pred_r = [0] * num_points
    y_pred_g = [0] * num_points
    y_pred_b = [0] * num_points

    for p in range(0, num_points):
        if (y_pred[p] == 0):
            y_pred_r[p] = 250
            y_pred_g[p] = 0
            y_pred_b[p] = 0
        elif (y_pred[p] == 1):
            y_pred_r[p] = 0
            y_pred_g[p] = 250
            y_pred_b[p] = 0
        elif (y_pred[p] == 2):
            y_pred_r[p] = 0
            y_pred_g[p] = 0
            y_pred_b[p] = 250

    C1 = y_pred_r
    C2 = y_pred_g
    C3 = y_pred_b

    x, y, z = zip(*cloud)
    color = zip(x, y, z, C1, C2, C3)
    divided_clusters.extend(color)
    return divided_clusters


if __name__ == '__main__':
    open("vertical_cloud_points.xyz").read()
    points1 = np.genfromtxt("vertical_cloud_points.xyz", delimiter=',')
    clusters1 = divide_into_clusters(num_points, points1)
    np.savetxt('vertical_clusters.xyz', clusters1, delimiter=',', fmt='%.8f')
    open("vertical_cloud_points.xyz").close()
    divided_clusters = []

    open("horizontal_cloud_points.xyz").read()
    points2 = np.genfromtxt("horizontal_cloud_points.xyz", delimiter=',')
    clusters2 = divide_into_clusters(num_points, points2)
    np.savetxt('horizontals_clusters.xyz', clusters2, delimiter=',', fmt='%.8f')
    open("horizontal_cloud_points.xyz").close()
    divided_clusters = []

    open("cylindrical_cloud_points.xyz").read()
    points3 = np.genfromtxt("cylindrical_cloud_points.xyz", delimiter=',')
    clusters3 = divide_into_clusters(num_points, points3)
    np.savetxt('cylindrical_clusters.xyz', clusters3, delimiter=',', fmt='%.8f')
    open("cylindrical_cloud_points.xyz").close()
    divided_clusters = []

