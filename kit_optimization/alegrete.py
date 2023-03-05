import numpy as np


def compute_mse(theta_0, theta_1, data):
    x = data[:, 0]
    y = data[:, 1]
    y_pred = theta_0 + theta_1 * x
    mse = np.mean((y_pred - y) ** 2)
    return mse



def step_gradient(theta_0, theta_1, data, alpha):
    x = data[:, 0]
    y = data[:, 1]
    y_pred = theta_0 + theta_1 * x
    n = len(data)
    theta_0 -= alpha * (2 / n) * np.sum(y_pred - y)
    theta_1 -= alpha * (2 / n) * np.sum((y_pred - y) * x)
    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    theta_0_list = [theta_0]
    theta_1_list = [theta_1]
    
    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        theta_0_list.append(theta_0)
        theta_1_list.append(theta_1)
    
    return theta_0_list, theta_1_list
