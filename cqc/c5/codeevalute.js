// 代码评估
var url = 'http://www.baidu.com'
var page = require('webpage').create();
page.open(url, function (status) {
    var title = page.evaluate(function () {
        return document.title;
    });
    console.log('Page title is ' + title);
    phantom.exit();
})