# -*- coding: utf-8 -*-

import tensorflow as tf
import keras

if __name__ == '__main__':
	sess = tf.Session()
	a = tf.constant(10)
	b = tf.constant(22)
	print("Hello Pattern Finance: %i"%sess.run(a+b))