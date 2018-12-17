## 父与子的编程之旅：与小卡特一起学Python2

### 术语箱

- GUI 就是图形用户界面(graphical user interface)。这表示界面中有窗口、菜单、按钮、滚动条等等。没有 GUI 的程序称为文本模式(text-mode)程序、控制台(console)程序或命令行(command-line)程序。
- 关键字(keyword)是作为 Python 语言一部分的特殊词，也称为保留字(reservedword)。
- 每次循环称为一次迭代(iteration)。
- 传递部分(调用函数)时应当称作实参(argument)，而接收部分(函数内部)时应该称为形参(parameter)。



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