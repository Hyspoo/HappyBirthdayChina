# HappyBirthdayChina

Python + OpenCV实现标准五星红旗的绘制

### 国旗长宽比

3:2


### 标准BGR色值

国旗红：(16, 41, 222)

星星黄：(0, 222, 255)

### 五角星排列方式

1、首先将国旗等分成四个矩形，将左上角的矩形划分为15\*10的网格

2、大五角星的中心位于(5,5)处，远端距中心3格，方向朝上

3、小五角星的中心分别位于(10,2),(12,4),(12,7),(10,9)处，远端距中心1格，方向指向大五角星中心



<img src="./flagRule.jpg" style="zoom:70%" />
