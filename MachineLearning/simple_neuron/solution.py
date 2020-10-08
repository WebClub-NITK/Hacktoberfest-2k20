import numpy as np


class Function:
	def __init__(self, before=None):
		self.before = before

	def _forward(self, x):
		pass

	def _diff(self, x):
		pass

	def _backward(self, diff):
		pass

	def _str(self):
		pass

	def forward(self, x):
		if self.before is None:
			return self._forward(x)
		else:
			return self._forward(self.before.forward(x))

	def diff(self, x):
		if self.before is None:
			return self._diff(x)
		else:
			return self._diff(self.before.forward(x)) * self.before.diff(x)

	def backward(self, x, diff):
		diff = diff * self._diff(x)
		self._backward(diff)
		if self.before is not None:
			self.before.backward(x, diff)

	def __str__(self):
		ret = ''
		if self.before is not None:
			ret += str(self.before) + '\n  ↓\n'
		else:
			ret += '[Input]\n  ↓\n'
		ret += self._str()
		return ret


class Sigmoid(Function):
	def _forward(self, x):
		return 1 / (1 + np.exp(-x))

	def _diff(self, x):
		return np.exp(x) / (1 + np.exp(x)) ** 2

	def _backward(self, diff):
		pass

	def _str(self):
		return '[Sigmoid Function]'


class Neuron(Function):
	def __init__(self, size, before=None):
		super().__init__(before)
		self.size = size
		self.param = np.random.random_sample(size)

	def _forward(self, x):
		return np.dot(x, self.param)

	def _diff(self, x):
		return x

	def _backward(self, diff):
		self.param += diff

	def _str(self):
		return '[Neuron] = ' + str(self.param)


if __name__ == '__main__':
	data_size = 2
	train_input = [[1, 2, 3], [2, 3, 4]]
	train_output = [0.1, 0.9]
	learning_rate = 0.1
	total_step = 100000

	network = Sigmoid(Neuron(3))

	tot_loss = 0
	for i in range(total_step):
		tot_loss = 0

		for j in range(data_size):
			output = network.forward(train_input[j])
			loss = train_output[j] - output
			tot_loss += loss
			network.backward(train_input[j], loss * learning_rate)

		if i % 100 == 0:
			print('total loss on iter {}: {}'.format(i, tot_loss))

	print('Result Network')
	print(network)
	print('loss = {}'.format(tot_loss))

