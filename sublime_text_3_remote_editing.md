如何在Sublime Text 3中远程编辑文件
===================

[![BSD License][bsdlicense-button]][bsdlicense]
[![Code of Conduct][codeofconduct-button]][Code of Conduct]

[bsdlicense-button]: http://img.shields.io/badge/license-BSD-yellow.svg
[bsdlicense]: http://opensource.org/licenses/BSD-3-Clause
[codeofconduct-button]: https://img.shields.io/badge/code%20of%20conduct-contributor%20covenant-green.svg?style=flat-square
[Code of Conduct]: https://github.com/Python-Markdown/markdown/blob/master/CODE_OF_CONDUCT.md



本文目标
-------------

在Windows 10中使用Sublime Text 3远程编辑macOS中的文件

1. `local` 在Sublime Text 3中安装rsub包
2. `remote` 在macOS中安装rmate
3. `local` 在Windows 10中配置ssh远程连接macOS的方式
4. `local` 使用ssh连接macOS并远程编辑文件




安装顺序
-------------

1. 在Sublime Text 3中安装rsub包

   - 通过Preferences - Package Control选择Install Package
   - 搜索并安装rsub包
   - 如果你无法成功完成安装，你可以手动将[rsub包](/sources/rsub.sublime-package)放至Installed Packages中
   - 重启Sublime Text 3

2. 在Windows 10中配置ssh

   - 将下段代码加入到~/.ssh/config文件中，并将Host/Hostname/User字段替换成你想要的

     ```bash
     Host mba
         Hostname 192.168.3.122
         RemoteForward 52698 127.0.0.1:52698
         User pf
     ```

   - 使用ssh登录远程macOS电脑

     ```bash
     ssh mba
     ```

3. 在macOS中安装rmate

   - 下载rmate并重命名为rsubl

     ```bash
     wget -O /usr/local/bin/rsubl https://raw.github.com/aurora/rmate/master/rmate
     chmod a+x /usr/local/bin/rsubl
     ```

4. 在Sublime Text 3中编辑远程文件

   - 在远程macOS电脑中通过rsubl打开需要在Windows中编辑的文件
   - 文件会自动出现在Windows 10的Sublime Text 3编辑器中




文末推荐
-------------

- [PFFI](https://github.com/patternfinance/PFFI): Pattern Finance Factor Investing
- [Cmder](https://github.com/cmderdev/cmder): Lovely console emulator package for Windows