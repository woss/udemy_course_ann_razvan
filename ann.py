from utils import make_matrix, between


use_bias = 1


class ANN:
    def __init__(self):
        pass

    def train(self):
        pass

    def predict(self):
        pass

    def update_weigths(self):
        pass


class Layer:
    def __init__(self, id, layer_size, prev_layer_size):
        self.id = id
        self.n_neurons = layer_size
        self.bias_val = 1

        # this is how you init an array of zeroes based on self.n_neurons
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # input vector
        self.input = [0] * self.n_neurons

        # output vector
        # it's not that bias enters this layer, it exists it
        # it will be used in next layer but exists in this layer
        self.output = [0] * (self.n_neurons + use_bias)

        # first vector is our bias value
        self.output[0] = self.bias_val

        # error vector
        self.error = [0] * self.n_neurons

        # weight matrix
        self.weight = make_matrix(prev_layer_size + use_bias, self.n_neurons)

        for i in range(len(self.weight)):
            for j in range(self.weight[i]):
                self.weight[i][j] = between(-0.2, 0.2)
