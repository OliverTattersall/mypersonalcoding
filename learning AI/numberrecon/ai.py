import mnist_loader
import model

training_data, validation_data, test_data1 = mnist_loader.load_data_wrapper()

net=model.Network([784, 30,10])
net.SGD(training_data, 30, 10, 3,0, test_data=test_data1)

