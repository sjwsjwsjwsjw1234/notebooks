# vscode配置c++环境
---
### 1. 安装minGW编译器
* 下载地址: <https://osdn.net/projects/mingw/downloads/68260/mingw-get-setup.exe/>，安装（安装目录名不要带中文）。
* 安装完后打开选择如下安装包：
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219191803876-126551350.png)
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219191812400-1415777336.png)
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219191820284-42231086.png)
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219191827410-1108292200.png)
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219191935481-1038648021.png)
前两张图是编译器，gdb是调试器
* 将minGW下的bin目录加入环境变量（比如我的是：D:\minGW\bin\）

### 2. 安装配置vscode
* vscode官网下载并安装vscode
* 打开vscode，选择扩展
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219192246571-618461798.png)

  搜索下载如下插件
  ![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219192317177-1511461398.png)  （必须）
  ![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219203129037-637528695.png)   （必须）

  ![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219192340798-271601873.png)  （括号颜色插件，推荐）
  ![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219192409148-1291091979.png)  （汉化插件）

### 3. 开始在vscode下写代码
* 创建一个文件夹作为vscode的工作目录，将该文件夹拖入到vscode图标上打开。
* 在该文件夹下创建一个cpp项目
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219192756993-369769361.png)
* 输入如下代码
	```c++:
	#include<iostream>
	using namespace std;
	int main()
	{
		cout<<"hello vscode";
	}
	```
	按下CTRL+S保存，否者运行会报错！！！！！！ 
* 保存后，右键，点击Run Code
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219193115712-1333862475.png)
运行结果如图：
![image](https://img2020.cnblogs.com/blog/1882256/202112/1882256-20211219193339370-1961362326.png)


### 4. 常见问题补充
* 无法输入的问题
在文件-首选项-设置-工作区中搜索Run In Terminal，勾选选项。

* 出现错误：
	>g++ : 无法将“g++”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，然后再试一次。

	解决办法：
	>以管理员身份运行vscode
