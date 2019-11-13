var url = 'http://www.cuiqingcai.com';
var page = require('webpage').create();
//回调函数来实现接收到资源请求的监听
page.onResourceRequested = function (request) {
    console.log('Resuest' + JSON.stringify(request, undefined, 4));
}
////回调函数来实现资源接受完毕的监听
page.onResourceReceived = function (respinse) {
    console.log('Receive' + JSON.stringify(request, undefined, 4));
}
page.open(url);