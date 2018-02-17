如何用Datasets API加速TensorFlow数据操作
===================

[![BSD License][bsdlicense-button]][bsdlicense]
[![Code of Conduct][codeofconduct-button]][Code of Conduct]

[bsdlicense-button]: http://img.shields.io/badge/license-BSD-yellow.svg
[bsdlicense]: http://opensource.org/licenses/BSD-3-Clause
[codeofconduct-button]: https://img.shields.io/badge/code%20of%20conduct-contributor%20covenant-green.svg?style=flat-square
[Code of Conduct]: https://github.com/Python-Markdown/markdown/blob/master/CODE_OF_CONDUCT.md

问题描述
-------------

我们使用TensorFlow进行模型训练的传统做法是在每一个epoch中将数据通过feed_dict的形式传入到session中。这种方法在`数据导入`阶段需要在Python和C++(TensorFlow)之间来回切换，而之后的`训练`操作也必须等到导入操作完成后才开始执行。为了解决这种运行效率低下的问题，我们在TensorFlow 1.2之前使用基于多线程和队列的输入Pipelines。除此之外，我们也常常会用`batching`的方式来训练模型，这也引入了一些额外的Python操作。

```python
# 传统模型训练流程
# (Optional) Batching
#			 Feed data
for epoch in range(training_epochs):
    # batching: randomly select a subset of training examples
    rand_index = np.random.choice(len(X), size=batch_size)
    rand_x = X[rand_index]
    rand_y = Y[rand_index]

    # feed data
    # Python -> C++
    sess.run(train_step, feed_dict={placeholder_x: rand_x, placeholder_y: rand_y})
```

不过不用担心，从TensorFlow 1.4开始，我们可以使用`tf.data`模块(Datasets API)来简化这一流程。

Datasets API简介
-------------

在TensorFlow 1.4之前，Datasets API是TensorFlow contrib package中的一个模块。自1.4起，我们可以通过`tf.data.Dataset`来调用其相应的API。那么，用Datasets API有什么好处呢？

1. 首先，从代码编写的角度来看，Datasets API属于High Level的接口，我们可以用其简化传统的数据处理方式

   - 传统方式：在for loop中使用Python代码(比如Numpy或者Pandas)来进行batch、shuffle、padding等操作

     ```python
     for epoch in range(training_epochs):
         # batch/shuffle/padding etc.
         # ...
         sess.run(train_step, feed_dict={...})
     ```

   - Datasets API方式：在for loop或while循环开始前通过TensorFlow来进行上述操作并生成迭代器(Iterator)

     ```python
     with tf.Graph().as_default() as g1:
     	# define placeholders and variables to build graph
     	# ...

         # prepare dataset for training
     	dataset = tf.data.Dataset.from_tensor_slices((features, labels))
         dataset = dataset.batch(batch_size).repeat(repeat_times)
         iterator = dataset.make_initializable_iterator()
         
         # create session from graph
         # ...
         
         try:
         	sess.run(tf.global_variables_initializer())
           while True:
               sess.run(train_step)
         except tf.errors.OutOfRangeError:
             pass
     ```

2. 从效率和性能的角度看，Datasets API既可以减少Python和C++代码运行的切换次数，还能够充分利用GPU的资源，可以有效地减少模型的训练时间

     ​

文末推荐
-------------

- [Cmder](https://github.com/cmderdev/cmder): Lovely console emulator package for Windows
- [PFFI](https://github.com/patternfinance/PFFI): Pattern Finance Factor Investing