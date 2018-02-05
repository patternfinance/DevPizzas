# 如何在Windows 10上安装Tensorflow(GPU版)

> #### 安装目标
>

如果安装过程顺利，你将获得如下环境：

- Tensorflow-gpu 1.5.0
- Visual Studio 2015 Community Edition
- CUDA 9.0
- cuDNN v7
- Python 3.6.4
- Keras




> #### 安装顺序
>

1. 安装Python 3.6.4

   [Python 3.6.4 安装包](https://www.python.org/downloads/release/python-364/) - 在Python官网下载3.6.4的安装包。在安装的最后一步不要忘记将Python加入到系统环境变量中。

   ​

2. 修改pip源

   [pip.ini文件](sources/pip.ini) - 在这里我们选择了阿里云的pip源来加速Python包的安装。在Windows 10中，我们需要在%APPDATA%目录下添加一个名称为pip的文件夹，并且在其中新建pip.ini文件。将以下代码复制粘贴至pip.ini文件中：

   ```
   [global]
   index-url=http://mirrors.aliyun.com/pypi/simple/
   [install]
   trusted-host=mirrors.aliyun.com
   ```

   ​

3. 安装CUDA

   - 安装Visual Studio 2015 Community Edition

     [Torrent](/sources/vs2015ce_torrent.txt) - 在国内可以选择[itellyou.cn](http://msdn.itellyou.cn/)的torrent来下载VS 2015社区版(免费)。在安装时只需勾选Visual C++部分。

     ![Visual Studio 2015 Community Edition](/imgs/vs2015ce.PNG)

   - 安装CUDA 9.0

     [CUDA ToolKit 9.0安装包](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_win10-exe) 以及 [Patch](https://developer.nvidia.com/compute/cuda/9.0/Prod/patches/1/cuda_9.0.176.1_windows-exe) - 我们可以在Legacy Release中找到[CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive)。安装完成后在命令行中测试是否安装成功。

     ![CUDA nvcc](/imgs/nvcc.PNG)

   - 安装cuDNN v7

     [cuDNN压缩包](https://developer.nvidia.com/rdp/cudnn-download) - cuDNN是NVIDIA推出的深度学习GPU加速库。我们需要下载与CUDA 9.0匹配的cuDNN v7压缩包，并将其中的bin、include、lib文件夹解压(覆盖)到C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0目录下。以下是CUDA相关的软件清单：

     ![CUDA Family](/imgs/cuda_family.PNG)

     ​

4. 通过pip安装Tensorflow GPU版

   Tensorflow在2018年1月底发布了[1.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v1.5.0)版并且宣布自1.6版起将支持AVX instructions。在1.5.0版中，如果我们直接通过pip install tensorflow来安装，会遇到依赖库*futures*版本不匹配的情况。我们需要先安装对应的*futures*版本。

   ```
   pip install futures==3.1.1
   ```

   然后指定安装Tensorflow GPU 1.5.0

   ```
   pip install tensorflow-gpu==1.5.0
   ```

   ​

5. 安装Keras

   ```
   pip install keras
   ```

   ​

6. 测试安装结果

   [test.py](/sources/test.py) - 你可以下载这个简单的脚本来测试你的Tensorflow环境是否安装成功。

   ![test.py](/imgs/test_tf_keras.PNG)




> #### 文末推荐
>

- [Cmder](https://github.com/cmderdev/cmder)： Lovely console emulator package for Windows