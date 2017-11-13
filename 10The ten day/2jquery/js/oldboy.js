//alert('oldboy') //弹窗

/*name = 'alex'   //python写法

def Foo():  //python写法，//单行注释
    pass
*/  //多行注释

//name = 'alex'   //全局变量
//var name = 'alex'   //局部变量
/*
window.name = '123' //建议全局变量这么写

function Foo(name) {
    var arg2 = arguments[1] //默认参数
    console.log(name);  //console用于调试
    console.log(arg2);  //;号在每一行语句后面都要进行分割.
    return aaa; //返回值
}

Foo('alex')
*/
/*
var temp = function () {    //匿名函数

}
*/
/*
(function () {
    console.log('alex')
})()    //自执行函数,不用调用自动执行

(function (name) {
    console.log(name);
})('oldboy')

var name = '   tanglei   '
console.log(name.trim())    //字符串去空白

var name = 'alex'
console.log(name.charAt(0)) //根据索引找字符
console.log(name.substring(1,3))    //生成子字符串
console.log(name.length)    //字符串长度

var arry = [1,2,3,4]
//var arry = Array(1,2,3,4,)  //声明数组
arry.push('alex');
console.log(arry)
arry.unshift('old');
console.log(arry)
arry.splice(1,0,'boy');
console.log(arry)
*/

var array = [11,22,33,44,55]
/*
for(var item in array){
    console.log(item)   //循环返回的是index
}
for(var item in array){
    console.log(array[item])    //循环返回的是数组里面的数值
}
*/
for(var i=0;i<array.length;i++){
    console.log(array[i]);
}