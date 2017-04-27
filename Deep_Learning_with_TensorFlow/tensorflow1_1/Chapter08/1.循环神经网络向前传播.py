# coding=utf8
import numpy as np

# 1. 定义RNN的参数。
X = [1,2]
state = [0.0, 0.0]
w_cell_state = np.asarray([[0.1, 0.2], [0.3, 0.4]])
w_cell_input = np.asarray([0.5, 0.6])
b_cell = np.asarray([0.1, -0.1])
w_output = np.asarray([[1.0], [2.0]])
b_output = 0.1

# 2. 执行前向传播过程。
for i in range(len(X)):
    before_activation = np.dot(state, w_cell_state) + X[i] * w_cell_input + b_cell
    state = np.tanh(before_activation)
    final_output = np.dot(state, w_output) + b_output
    print "before activation: ", before_activation
    print "state: ", state
    print "output: ", final_output


'''
before activation:  [ 0.6  0.5]
state:  [ 0.53704957  0.46211716]
output:  [ 1.56128388]
before activation:  [ 1.2923401   1.39225678]
state:  [ 0.85973818  0.88366641]
output:  [ 2.72707101]

Process finished with exit code 0'''