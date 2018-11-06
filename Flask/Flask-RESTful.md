## flask-RESTful
- 软件架构风格
- 实现前后端分离
- 让后端开发者只关注数据
- 组成
	- 安装
	- 初始化
		- 使用App进行Api的初始化
	- 创建资源
		- 继承自Resource
		- 和视图函数基本一致
		- CBV
	- 注册资源
		- 在API上添加

### 输出
- 默认输出字典,可以直接进行序列化
- 如果包含对象
	- 默认会抛出异常,对象不可JSON序列化
- 使用格式化工具
	- marshal函数
	- marshal_with 装饰器
	- 条件
		- 格式
			- 字典格式
			- 允许嵌套
			- vlaue是fields.xxx
		- 数据
			- 允许任何格式
			 
		-  如果格式和数据完全对应,数据就是预期格式
		-  如果格式比数据中字段多,程序依然正常运行,不存在的字段是默认值
		-  如果格式比数据中字段少,程序正常执行,少的字段不会显示

	- 结论
		- 想要什么格式的返回
		- 格式工具(模板)就是什么样的
		- 和传入的数据没有什么直接关系

	- 格式和数据的映射
		- 格式中的字段名和数据中的名需要一致
			- 也可以手动指定映射
			- Atribute="Property_name"
		-也可以对属性指定默认值

			- default
			- 指定默认值,值传递使用传进来的值
			- 未传递,则使用默认值 

	- fields
		- Raw
			- format
			- output
			- 调用
				- 将数据传递进格式化工具的时候,先获取值output
				- 再对值进行格式化format
		- String
			- 继承Raw
			-  将value进行格式化
			-  转换成兼容格式的text

		- Interger
			- 继承自Raw
			- 重写了初始化,将default设置为0
			- 重写格式化,直接将vlaue转换成int
		- Boolean
			- 继承自Raw
			- 重写格式化,直接将vlaue转换成bool
		- Nested
			- 继承自Raw
			- 重写output
			- 进行marshal
		
		- List
			- 继承自Raw
			- 重写output
				- 判断类型
				- 对不同的类型进行不同的处理
					- dict 直接进行处理
					- list 迭代处理
			- 重写format
				- 进行格式化
### RequestParser
- 使用过程
	- 先定义一个RequestParser对象	parser = reqparse.RequestParser()
	- 向对象中添加字段	parser.add_argument()
	- 从对象中获取字段	args = parser.parse_args()
- 对象在添加参数的时候,可以实现数据预校验
	- 参数是否必须 required=True
	- 数据的类型(python3 默认类型str) type
	- 还可以设置错误提示 
	- 接受多个值 action="append" 
	- 可以在接收的时候指定别名 dest
	- 指定参数的来源	location