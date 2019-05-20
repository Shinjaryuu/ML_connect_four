import numpy as np

class NeuralNetwork:

    def __init__(self, input_size, output_size, hidden_layer_size):
        """Create a neural network with input_size input neurons,
        output_size output neurons and one hidden layer with
        hidden_layer_size neurons in it. Weights are initialized
        randomly, the neurons all start with 0"""
        self.inputs = np.zeros(input_size)
        self.outputs = np.zeros(output_size)
        self.out_pre_activation = np.zeros(output_size)
        self.hidden_layer = np.zeros(hidden_layer_size)
        self.hl_pre_activation = np.zeros(hidden_layer_size)
        self.weights = [np.random.rand(input_size, hidden_layer_size),
                        np.random.rand(hidden_layer_size, output_size)]
        self.num_connections = [input_size * hidden_layer_size,
                                hidden_layer_size * output_size]
        self.weight_shapes = [w.shape for w in self.weights]

    @classmethod
    def activation_function(x):
        """Activation function for the neurons in this neural network
        Currently: Sigmoid function"""
        return 1/(1+np.exp(-x))

    def set_inputs(self, inputs):
        """Set the input neurons. Inputs must be a list of numpy array
        with as many entries as there are input neurons"""
        self.inputs = np.array(inputs)

    def forward(self):
        """Compute the values of the hidden layer and the output layer for
        the previously set inputs and the current value of the weights"""
        self.hl_pre_activation = np.dot(self.inputs, self.weights[0])
        self.hidden_layer = self.activation_function(self.hl_pre_activation)
        self.out_pre_activation = np.dot(self.hidden_layer, self.weights[1])
        self.outputs = self,activation_function(self.out_pre_activation)

    def get_weights(self):
        """Get a flattened array of the weights"""
        return np.concatenate([ws.flatten() for ws in self.weights])

    def set_weights(self, new_weights):
        """Set the weights to the new provided values. The weights should
        be given in form of a flat numpy array"""
        start = 0
        self.weights = []
        for (n, shape) in zip(self.num_connections,self.weight_shapes):
            self.weights.append(np.reshape(new_weights[start:start+n],shape))
            start += n
