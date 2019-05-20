from ML_connect_four.classes.neural_network import NeuralNetwork
import numpy as np

class Test:

    def test_setting_and_getting_weights(self):
        nn = NeuralNetwork(2,1,3)
        weights = nn.get_weights()
        print(nn.weights)
        print(weights)
        nn.set_weights(weights)
        new_weights = nn.get_weights()
        np.testing.assert_almost_equal(weights,new_weights)

if __name__ == '__main__':
    tests = Test()
    tests.test_setting_and_getting_weights()
