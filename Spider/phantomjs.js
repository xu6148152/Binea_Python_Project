var url = 'http://www.baidu.com';
var page = require('webpage').create();
page.open(url, status => {
    var title = page.evaluate(() => document.title);
    console.log('Page title is ' + title);
    phantom.exit();
});