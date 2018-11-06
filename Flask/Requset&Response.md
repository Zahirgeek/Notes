## Response
- 返回数据
	- Response(msg, status, headers, mimetype, content_type, direct_passthrough)
	- make_response(data, code)
		- data 返回数据内容
		- code 状态码
- 终止执行
	 - abort(code)
		 - code 状态码(错误)
- 捕获状态码
	- @app.errorhandler(code)

## Request
- request.args
	- 返回值是元组(key, value)
	- 接收query_params
	- 不是get专属,所有请求都能获取这个参数

- request.form
	- 接收post数据
		- 直接支持put,patch
	- ImmutableMultiDict
		- args和form都是此类型
		- dict子类

- request.files
	- 文件上传数据
- 属性
	- url		&nbsp;&nbsp;&nbsp;&nbsp;完整请求地址
	- base_url	&nbsp;&nbsp;&nbsp;&nbsp;去掉GET参数的URL
	- host_url	&nbsp;&nbsp;&nbsp;&nbsp;只有主机和端口号的URL
	- path		&nbsp;&nbsp;&nbsp;&nbsp;路由中的路径
	- method		&nbsp;&nbsp;&nbsp;&nbsp;请求方法
	- remote_addr	&nbsp;&nbsp;&nbsp;&nbsp;请求的客户端地址
	- args		&nbsp;&nbsp;&nbsp;&nbsp;GET请求参数
	- form		&nbsp;&nbsp;&nbsp;&nbsp;POST请求参数
	- files		&nbsp;&nbsp;&nbsp;&nbsp;文件上传
	- headers		&nbsp;&nbsp;&nbsp;&nbsp;请求头
	- cookies		&nbsp;&nbsp;&nbsp;&nbsp;请求中的cookie