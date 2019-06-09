from ML_connect_four.classes.neural_network import NeuralNetwork
import numpy as np

class Test:

    def test_setting_and_getting_weights(self):
        nn = NeuralNetwork(2,1,[3])
        weights = nn.get_weights()
        nn.set_weights(weights)
        new_weights = nn.get_weights()
        np.testing.assert_almost_equal(weights,new_weights)

    def test_forward(self):
        nn = NeuralNetwork(2,1,[3])
        weights = [np.array([[0.1,0.3,0.6],[0.2,0.5,0.7]]),
                   np.array([[0.8],[0.9],[1.1]])]
        weights = np.concatenate([ws.flatten() for ws in weights])
        nn.set_weights(weights)
        outputs = nn.forward(np.array([0.6,0.3]))
        np.testing.assert_almost_equal(outputs[0], 0.838917292)
