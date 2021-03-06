## 父与子的编程之旅：与小卡特一起学Python2

### 术语箱

- GUI 就是图形用户界面(graphical user interface)。这表示界面中有窗口、菜单、按钮、滚动条等等。没有 GUI 的程序称为文本模式(text-mode)程序、控制台(console)程序或命令行(command-line)程序。

- 关键字(keyword)是作为 Python 语言一部分的特殊词，也称为保留字(reservedword)。

- 每次循环称为一次迭代(iteration)。

- 传递部分(调用函数)时应当称作实参(argument)，而接收部分(函数内部)时应该称为形参(parameter)。

- 按编程术语来讲，如果限制对对象数据的访问，使得只能通过使用方法来获
  取和修改这些数据，就称为数据隐藏(data hiding)。

- 像素(pixel)这个词是“图像元素”(picture element)的简写。这表示屏幕上或图像中的一点。如果在一个图像浏览器中查看图片，充分放大(让图像非常大)，就可以看到单个的像素。

- 完成图形编程时，将像素从一个地方复制到另一个地方是很常见的(比如从变量复制到屏幕，或者从一个表面复制到另一个表面)。像素复制在编程中有一个特殊的名字，叫做块移(blitting)。

- 简单地说，碰撞检测(collision detection)指的是了解两个动画精灵何时接触或重叠。两个移动的东西相互碰到一起，这就是一个碰撞(collision)。

- 帧速率(每秒帧数，fps)

- 队列(queue)读作“Q”。日常生活中，这就表示排队。 在编程中，队列通常指一个列表，其中的元素按某种特定的顺序到达，或者 将按某种特定的顺序使用

- 计算机图形学中，渲染(render)是指绘制某个东西，或者让它可见。

- 在较大的字符串中查找较小的字符串时,较小的这个字串称为串(substring)。 



### Python2和Python3的区别：

- 在 Python 2 中，做除法的方式称为“整除”(floor division)。但 Python 3 的工作方式不一样，在 Python 3 中，如果你使用常规的除法操作符(前斜杠 “/”)，则做的是常规除法，而不是整除。
- 在 Python 3 中，通过在行尾添加逗号使得打印的内容都在同一行的方法不再有效。而且，在 Python 3 中使用 print() 时，要打印的内容必须被包含在一对括号中。
- Python 2 在进行除法运算时会默认向下取整，Python 3 会默认进行浮点数除法。
- 在 Python 2 中，range() 函数返回一个列表。但在 Python 3 中，range() 返回一个 range 对象。
- \#! python2  \#! python3分别表示该代码文件使用Python2或者Python3解释运行。
- 不等于，在 Python 3 中，不再支持 <> 形式的不等于，只能使用 != 来表示不 等于。

### 技巧

- 脚本有汉字需要用以下代码开头，否则以后可能会无法打开。   #-*- coding: UTF-8 -*-
- 如果有一个很长的语句，在一行里放不下，就可以使用反斜线字符告诉Python，这一行还没有结束下一行的内容也是这一行的一部分”。
- **Pygame 用python3 运行。**
- pyuic5 --preview firstgui.ui  可预览UI文件
- pyuic5 --execute --output firstgui.py firstgui.ui  生成UI文件的py文件

### 备忘

- Gui文件有bug
- PyQt4中的`QtGui`模块已经被分成PyQt5的[`QtGui`](http://pyqt.sourceforge.net/Docs/PyQt5/QtGui.html#PyQt5-QtGui)， [`QtPrintSupport`](http://pyqt.sourceforge.net/Docs/PyQt5/QtPrintSupport.html#PyQt5-QtPrintSupport)和[`QtWidgets`](http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html#PyQt5-QtWidgets)模块。
- Listing_24-4.py 在python3运行有问题
