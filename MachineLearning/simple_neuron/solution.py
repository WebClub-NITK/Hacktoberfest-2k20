import numpy as np


class Function:
	def __init__(self, before=None):
		self.before = before
		if before is None:
			self.before_forward = lambda x: x
			self.before_diff = lambda _: 1
		else:
			self.before_forward = before.forward
			self.before_diff = before.diff

	def _forward(self, x):
		pass

	def _diff(self, x):
		pass

	def _backward(self, diff):
		pass

	def _str(self):
		pass

	def forward(self, x):
		return self._forward(self.before_forward(x))

	def diff(self, x):
		return self._diff(self.before_forward(x)) * self.before_diff(x)

	def backward(self, x, diff):
		diff = diff * self._diff(self.before_forward(x))
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
	train_input = np.array([[1, 2, 3], [2, 3, 4]])
	train_output = np.array([0.1, 0.9])
	learning_rate = 0.6
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

