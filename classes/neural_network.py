import numpy as np
import copy


class NeuralNetwork:

    def __init__(self, input_size, output_size, hidden_layer_sizes):
        """Create a neural network with input_size input neurons,
        output_size output neurons and one hidden layer with
        hidden_layer_size neurons in it. Weights are initialized
        randomly, the neurons all start with 0
        """
        self.layer_sizes = [input_size] + hidden_layer_sizes + [output_size]
        self.weights = [np.random.rand(prev_layer, next_layer)
                        for prev_layer, next_layer
                        in zip(self.layer_sizes, self.layer_sizes[1:])]

    @staticmethod
    def activation_function(x):
        """Activation function for the neurons in this neural network
        Currently: Sigmoid function
        """
        return 1/(1+np.exp(-x))

    def forward(self, inputs):
        """Compute the output for the given inputs. A numpy array of multiple
        inputs can be given, in which case a numpy array of outputs is
        returned
        """
        neurons = copy.deepcopy(inputs)
        for weights in self.weights:
            neurons = self.activation_function(np.dot(neurons,weights))
        return neurons

    def get_weights(self):
        """Get a flattened array of the weights"""
        return np.concatenate([ws.flatten() for ws in self.weights])

    def set_weights(self, new_weights):
        """Set the weights to the new provided values. The weights should
        be given in form of a flat numpy array
        """
        start = 0
        for index, weight in enumerate(self.weights):
            shape = weight.shape
            num_con = np.product(shape)
            self.weights[index] = np.reshape(new_weights[start:start+num_con], shape)
            start += num_con
