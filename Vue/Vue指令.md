# v-once
---
- 不需要表达式
- 详细:
	- 只渲染元素和组件一次。随后的重新渲染，元素/组件及其所有的子节点将被视为静态内容并跳过。这可以用于优化更新性能。

			<div id="container">
        		<ul>
            		<li>Zahir is a boy</li>
            		<li>Zahir is a {{word0}} boy</li>
            		<li v-once>Zahir is a {{word1}} boy</li>
        		</ul>
    		</div>
			-------------------------------------------------------
			var vm = new Vue({
    			el:"#container",
    			data:{
        			word0: "good",
        			word1: "nice",
    			}
			});
			setTimeout(function(){
    			vm.word0 = "ハンサム"
    			vm.word1 = "優しい"
			}, 3000);

# v-html
---
- 预期: string
- 详细:
- 更新元素的 innerHTML 。注意：内容按普通 HTML 插入 - 不会作为 Vue 模板进行编译 。如果试图使用 v-html 组合模板，可以重新考虑是否通过使用组件来替代。
- <strong style="color:red; font-size:20px">警告</strong>:
	- 在网站上动态渲染任意 HTML 是非常危险的，因为容易导致 XSS 攻击。只在可信内容上使用 v-html，永不用在用户提交的内容上。
	- 在单文件组件里，scoped 的样式不会应用在 v-html 内部，因为那部分 HTML 没有被 Vue 的模板编译器处理。如果你希望针对 v-html 的内容设置带作用域的 CSS，你可以替换为 CSS Modules 或用一个额外的全局元素手动设置类似 BEM 的作用域策略。

			<div id="container">
        		<ul>
            		<li>{{word0}}</li>
            		<li>{{word1}}</li>
            		<li v-html="word2"></li>
        		</ul>
    		</div>
# v-bind
---
- 缩写：:
- 预期：any (with argument) | Object (without argument)
- 参数：attrOrProp (optional)
- 修饰符：
	- .prop - 被用于绑定 DOM 属性 (property)。(差别在哪里？)
	- .camel - (2.1.0+) 将 kebab-case 特性名转换为 camelCase. (从 2.1.0 开始支持)
	- .sync (2.3.0+) 语法糖，会扩展成一个更新父组件绑定值的 v-on 侦听器。
- 用法：

	- 动态地绑定一个或多个特性，或一个组件 prop 到表达式。
	在绑定 class 或 style 特性时，支持其它类型的值，如数组或对象。可以通过下面的教程链接查看详情。
	在绑定 prop 时，prop 必须在子组件中声明。可以用修饰符指定不同的绑定类型。没有参数时，可以绑定到一个包含键值对的对象。注意此时 class 和 style 绑定不支持数组和对象。

			<div id="container">
        		<button v-bind:disabled="flag">这是一个按钮</button>
    		</div>
			--------------------------------------------------------
			var vm = new Vue({
    			el:"#container",
    			data:{
        			flag:false,
    			}
			});

			// 定时器
			setTimeout(function(){
    			vm.flag = true;
			}, 3000);

# v-text
---
- 预期: string
- 详细:
	- 更新元素的 textContent。如果要更新部分的 textContent ，需要使用 {{ Mustache }} 插值。会将html标签内文本都转变为文本形式
- 示例：
			
		<div id="container">
        	<p v-text="word">Zahir</p>
    	</div>
		---------------------------------
		var vm = new Vue({
    		el:"#container",
    		data:{
        		word:"</strong>Zahir</strong>",
    		}
		});
# v-show
---
- 预期: any
- 用法:
	- 根据表达式之真假值，切换元素的 display CSS 属性。
	- 当条件变化时该指令触发过渡效果。
- 示例：
			
		<div id="container">
        	<p v-show="word">Zahir</p>
    	</div>
		---------------------------------
		var vm = new Vue({
    		el:"#container",
    		data:{
        		word:false,
    		}
		});
# v-if
---
- 预期：any

- 用法：
	- 根据表达式的值的真假条件渲染元素。在切换时元素及它的数据绑定 / 组件被销毁并重建。如果元素是 <template> ，将提出它的内容作为条件块。
	- 当条件变化时该指令触发过渡效果。
	- <strong style="color:#F9603A; font-size:20px">注意</strong>:
		- 当和 v-if 一起使用时，v-for 的优先级比 v-if 更高。详见[列表渲染教程](https://cn.vuejs.org/v2/guide/list.html#v-for-with-v-if)
- 参考: [条件渲染](https://cn.vuejs.org/v2/guide/conditional.html)
- 示例:

		<div id="container">
        	<p v-if="word>10">Zahir</p>
    	</div>
		---------------------------------
		var vm = new Vue({
    		el:"#container",
    		data:{
        		word:4,
    		}
		});
# v-else
- 不需要表达式
- 限制：前一兄弟元素必须有 v-if 或 v-else-if。
- 用法：
	- 为 v-if 或者 v-else-if 添加“else 块”。
- 示例:
	
		<div id="container">
        	<p v-if="word>10">Zahir</p>
        	<p v-else>Jane</p>
    	</div>
		----------------------------------
		var vm = new Vue({
    		el:"#container",
    		data:{
       			word:4,
    		}
		});
# v-for
- 预期：Array | Object | number | string
- 用法：
	- 基于源数据多次渲染元素或模板块。此指令之值，必须使用特定语法 alias in expression ，为当前遍历的元素提供别名：

			<div v-for="item in items">
  				{{ item.text }}
			</div>
	- 另外也可以为数组索引指定别名 (或者用于对象的键)：
	
			<div v-for="(item, index) in items"></div>
			<div v-for="(val, key) in object"></div>
			<div v-for="(val, key, index) in object"></div>
- 示例:
		
		<div id="container">
        	<ul>
            	<li v-for="item in arr">{{item}}</li>
        	</ul>
    	</div>
		---------------------------------------------------
		var vm = new Vue({
    		el:"#container",
    		data:{
        		arr:[1,2,3,4,5]
    		}
		});

		// 定时器
		setTimeout(function(){
    		// 给li增加值
    		vm.arr.push(6);
			// 修改li的值
			Vue.set(vm.arr, 1, 7)
		}, 1000);