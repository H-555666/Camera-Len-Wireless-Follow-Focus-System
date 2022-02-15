# Camera-Len-Wireless-Follow-Focus-System
wireless follow focus system that is powered by micropython and pico

***很多文件还未完善，最初版已发布，请等待🌛***

## 简要使用说明
如果你是一位爱好者，并只想制造和个人使用，请查看这份文档：[简要使用说明](https://github.com/ZhongWwwHhh/Camera-Len-Wireless-Follow-Focus-System/blob/main/Documentation/Quickstart.md)

## 开发者
本项目始终欢迎各位大佬的指导和帮助！！！

这个项目完全是针对Raspberry Pi Pico进行设计的

如果你想应用在其它可运行micropython的微控制器上（例如更强大的arduino或pyboard），有另一份[代码解释](https://github.com/ZhongWwwHhh/Camera-Len-Wireless-Follow-Focus-System/blob/main/Documentation/Codeinterpretation.md)将会使这个过程更加方便

## 项目简介
这个项目目前实现一个摇杆电位器（航模遥控器上的那种）远程无线控制步进电机，只需要两块Raspberry Pi Pico，一个ULN2003及其驱动的步进电机，一对无线收发模块，致力于实现成本远低于昂贵的市售无线跟焦器的同等功能设备

***未来会逐渐增加为可以控制三电机的版本，并增加A-B点限位等更强大的功能，请看[开发日志](https://github.com/ZhongWwwHhh/Camera-Len-Wireless-Follow-Focus-System/blob/main/Documentation/Updatelog.md)***

接收端和发射端使用相同的模块化硬件设计（PCB），只用刷写不同的程序即可实现发射端-接收端的转换

所有软件将使用micropython以便于修改和应用，硬件将全部采用Kicad进行设计

## 开发&商业用途
请注意：**此存储库中的所有软、硬件均遵循GPL3.0(GNU General Public License v3.0)**

你可以 **获取 使用 修改** ，但所有内容将继续遵循GPL3.0协议

如果你将其作为商品，那么你 **不得不(强制)** 让 **任何人** 都 **知晓** 其性质且 **能获得到源代码/源设计文件**

更多内容请参见[原GPL3.0文件](https://github.com/ZhongWwwHhh/Camera-Len-Wireless-Follow-Focus-System/blob/main/LICENSE)
