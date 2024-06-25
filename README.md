# 停车场管理系统

#### 介绍
该网页主要设计开发实现了一个停车场管理系统，包括车辆进出管理与计费管理两部分。
1. 车辆进场记录进场时间，车辆出场计算出场时间。
2. 长期卡车辆每年或每月交一次费用。临时车出场时计算停车费并缴纳费用。
3. 车位管理，实时显示车位总数和状态、空闲车位数量。
4. 停车费的查询和统计。
5. 进场车辆及时间随机生成。

#### 软件架构
项目架构说明
- app
  - controller   <!--数据库基本方法-->
    - __init__.py
    - carsController.py
    - parkingController.py
  - models      <!--数据库对象-->
    - __init__.py
    - cars.py
    - parking.py
  - service     <!--数据库操作方法-->
    - __init__.py
    - service
  - static      <!--固定资源文件-->
    - __init__.py
    - style.css
  - templates   <!--模板文件-->
    - __init.py
    - base.html
    - carlist.html
    - history.html
    - index.html
  - __init__.py
- config        <!--配置文件-->
  - config.py
  - __init__.py
- utils         <!--常用方法-->
- views         <!--视图文件-->
  - __init__.py
  - carlist
    - __init__.py
    - carlistviews.py
  - history
    - __init__.py
    - historyviews.py
  - index
    - __init__.py
    - indexviews.py
- forms.py     <!--模板函数文件-->
- start.py     <!--入口文件-->




#### 使用说明

1. 输入网址：xxxx,但暂时只能通过在终端输入 python start.py runserver启动
2. 在每个页面都有文字提示进行操作，主页可以进行车辆入库;当前车位可以查看当前占用车位的情况并进行出库;使用记录可以查看所有历史记录


#### 参与贡献
邹孟林
