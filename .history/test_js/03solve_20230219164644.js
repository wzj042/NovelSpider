
// s 为页面中初次加载时加载的一个使用base64编码的纯数字数组，
s = window.atob(ns);
var chapter_order = new Array();
chapter_order = s.split(',');

var chapter_content = document.getElementById("chapter").innerHTML;

document.getElementById("chapter").innerHTML = chapter_content.replace(new RegExp(/\\[(.*?)\\]/), '$1');

chapter_content = chapter_content.replace(new RegExp(/\\[.*?\\]/), '');

var qs_arr_1 = new Array();

qs_arr_1 = chapter_content.split("<br><br>");

var result = '';
var order_offset = chapter_order[0];
var len = qs_arr_1.length;

for (var i = 1; i <= len; i++) {
    result += qs_arr_1[chapter_order[i] - order_offset] + "<br/><br/>";
}

document.getElementById('ad').innerHTML = result;
document.getElementById("chapter")["style"].color = "#FBF6EC";
document.getElementById("chapter")["style"].height = "5px";

