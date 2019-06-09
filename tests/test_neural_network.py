from ML_connect_four.classes.neural_network import NeuralNetwork
import numpy as np

class Test:

    def test_setting_and_getting_weights(self):
        nn = NeuralNetwork(2,1,[3])
        weights = [np.array([[0.1,0.3,0.6],[0.2,0.5,0.7]]),
                   np.array([[0.8],[0.9],[1.1]])]
        weights = np.concatenate([ws.flatten() for ws in weights])
        nn.set_weights(weights)
        new_weights = nn.get_weights()
        np.testing.assert_almost_equal(weights,new_weights)

    def test_forward_one_layer(self):
        nn = NeuralNetwork(2,1,[3])
        weights = [np.array([[0.1,0.3,0.6],[0.2,0.5,0.7]]),
                   np.array([[0.8],[0.9],[1.1]])]
        weights = np.concatenate([ws.flatten() for ws in weights])
        nn.set_weights(weights)
        outputs = nn.forward(np.array([0.6,0.3]))
        np.testing.assert_almost_equal(outputs[0], 0.838917292)

    def test_forward_two_layers(self):
        nn = NeuralNetwork(2,2,[3,1])
        weights = [np.array([[0.1, 0.3, 0.6], [0.2, 0.5, 0.7]]),
                   np.array([[0.8], [0.9], [1.1]]),
                   np.array([[-0.2, -0.7]])]
        weights = np.concatenate([ws.flatten() for ws in weights])
        nn.set_weights(weights)
        outputs = nn.forward(np.array([0.6,0.3]))
        np.testing.assert_almost_equal(outputs[0], 0.458152262)
        np.testing.assert_almost_equal(outputs[1], 0.357267894)
