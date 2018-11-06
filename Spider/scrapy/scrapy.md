## scrapy命令
- 创建项目
	
		scrapy startproject qianmu

- 生成spider文件
- 注意:爬虫名字不能和项目名称重复

		#scrapy genspider [爬虫名字] [目标网站域名]
		scrapy genspider usnews qianmu.iguye.com

- 运行爬虫

		# 运行名为usnews的爬虫
		scrapy crawl usnews
		# 将爬到的数据导出为Json文件
		scrapy crawl usnews -o usnews.json
		# 导出为csv文件
		scrapy crawl usnews -o usnews.csv -t csv
		# 单独运行爬虫文件
		scrapy runspider usnews.py

- 调试爬虫

		# 进入到scrapy控制台,使用的是项目的环境
		scarpy shell
		# 带一个URL参数,将会自动请求这个url,并在请求成功后进入控制台
		scrapy shell httpL//url.com
- 进入控制台以后,可以使用以下函数和对象

| A        | B                                                            |
| -------- | ------------------------------------------------------------ |
| fetch    | 请求url或者Requesrt对象，注意：请求成功以后会自动将当前作用域内的request和responsne对象重新赋值 |
| view     | 用浏览器打开response对象内的网页                             |
| help    | 打印帮助信息                                                 |
| spider   | 相应的Spider类的实例                                         |
| settings | 保存所有配置信息的Settings对象                               |
| crawler  | 当前Crawler对象                                              |
| scrapy   | scrapy模块       

