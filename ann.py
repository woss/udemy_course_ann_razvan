from utils import make_matrix, between, sigmoid


use_bias = 1
squash = sigmoid


class ANN:
    def __init__(self, layer_sizes):
        self.layers = []
        self.learn_rate = 0.1

        for l in range(len(layer_sizes)):
            layer_size = layer_sizes[l]
            prev_layer_size = 0 if l is 0 else layer_sizes[l - 1]
            layer = Layer(layer_size, prev_layer_size)
            self.layers.append(layer)

    def train(self):
        pass

    def predict(self, input):
        """return prediction for input"""
        self.set_input(input)
        self.forward_propagate()
        return self.get_output()

    def set_input(self, input_vector):
        input_layer = self.layers[0]

        for i in range(0, input_layer.n_neurons):
            input_layer.output[i + use_bias] = input_vector[i]

    def forward_propagate(self):
        """
        Propagate signal through the network
        """
        # exclude last layer
        for l in range(len(self.layers) - 1):
            src_layer = self.layers[l]
            dst_layer = self.layers[l + 1]

            for j in range(0, dst_layer.n_neurons):
                sum_in = 0

                for i in range(0, src_layer.n_neurons + use_bias):
                    # weights come from next layer but inputs come from
                    # previous layer
                    sum_in += dst_layer.weight[i][j] * src_layer.output[i]

                dst_layer.input[j] = sum_in
                dst_layer.output[j + use_bias] = squash(sum_in)

    def get_output(self):
        """
        Return ntwork output
        """

        # our output layer is the last layer
        output_layer = self.layers[-1]
        res = [0] * output_layer.n_neurons
        for i in range(0, len(res)):
            res[i] = output_layer.output[i + use_bias]

        return res

    def update_weigths(self):
        pass


class Layer:
    def __init__(self, layer_size, prev_layer_size):
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
            for j in range(len(self.weight[i])):
                self.weight[i][j] = between(-0.2, 0.2)


if __name__ == '__main__':
    and_ann = ANN([1, 1])
    inputs = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
    targets = [[0.0], [0.0], [0.0], [1.0]]

    # make some predictions

    for i in range(len(targets)):
        print(inputs[i], and_ann.predict(inputs[i]))
