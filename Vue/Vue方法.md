# Vue.js 方法
---
vm.$watch( expOrFn, callback, [options] )   
- 
- 参数:
	- {string | Function} expOrFn
	- {Function | Object} callback
	- {Object} [options]
		- {boolean} deep
		- {boolean} immediate
- 返回值：{Function} unwatch

- 用法：
	- 观察 Vue 实例变化的一个表达式或计算属性函数。回调函数得到的参数为新值和旧值。表达式只接受监督的键路径。对于更复杂的表达式，用一个函数取代。
	- <span style="color:red;font-size:20px">注意</span>：在变异 (不是替换) 对象或数组时，旧值将与新值相同，因为它们的引用指向同一个对象/数组。Vue 不会保留变异之前值的副本。

			v.$watch("age", function(newVal, oldVal){
    			console.log(oldVal, newVal);
    			if(newVal > 20 || newVal < 0){
        		v.age = oldVal;
    			}
			});
