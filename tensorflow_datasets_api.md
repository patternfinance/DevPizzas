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

我们使用TensorFlow进行模型训练的传统做法是在每一个epoch中将数据通过feed_dict的形式传入到session中。这种方法在`数据导入`阶段需要在Python和C++之间来回切换，而之后的`训练`操作也必须等到导入操作完成后才开始执行。为了解决这种运行效率低下的问题，我们在TensorFlow 1.2之前使用基于多线程和队列的输入Pipelines。除此之外，我们也常常会用`batching`的方式来训练模型，这也引入了一些额外的操作。



而从TensorFlow 1.4开始，我们可以使用`tf.data`模块来简化这一流程。



文末推荐
-------------

- [Cmder](https://github.com/cmderdev/cmder): Lovely console emulator package for Windows
- [PFFI](https://github.com/patternfinance/PFFI): Pattern Finance Factor Investing