from tipo.Functional import activation
import numpy as np
import gc


# This class includes all the layer structures and handy tools for AI research
class Node:

    def __init__(self):
        pass

    # These methods prints the network structure of our network when the class gets called
    def __call__(self):
        for obj in gc.get_objects():
            if isinstance(obj, self.LinearLayer):
                print('[' + str(obj) + ", num_inputs: " + str(obj.num_inputs) + " num_neurons:" + str(
                    obj.num_neurons) + '],')

    # This class takes care of the Feed forward layers
    class LinearLayer:

        def __init__(self, num_inputs, num_neurons, bias_enabled=True):
            self.num_inputs = num_inputs
            self.num_neurons = num_neurons

            self.weights = 0.10 * np.random.randn(num_inputs, num_neurons)
            self.biases = np.where(bias_enabled, np.random.randn(1, num_neurons), np.zeros((1, num_neurons)))

        def __call__(self, batch, activation=activation.none):
            output = activation(np.dot(batch, self.weights) + self.biases)
            return output
