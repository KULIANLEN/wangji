function setHome(obj,url){
	try{
		obj.style.behavior='url'+'(#default#homepage)';
		obj.setHomePage(url);
	}catch(e){if(window.netscape){try{netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");}
	catch(e){alert("抱歉！您的浏览器不支持直接设为首页。请在浏览器地址栏输入“about:config”并回车然后将[signed.applets.codebase_principal_support]设置为“true”，点击“加入收藏”后忽略安全提示，即可设置成功。");}
	var prefs=Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);prefs.setCharPref('browser.startup.homepage',url);}}
}

function bookmark(url,title){
	if (window.sidebar) window.sidebar.addPanel(title, url,"");
	else if( window.opera && window.print ){
		var mbm = document.createElement('a');
		mbm.setAttribute('rel','sidebar');
		mbm.setAttribute('href',url);
		mbm.setAttribute('title',title);
		mbm.click();
	}
	else if( document.all ){ window.external.AddFavorite(url,title);}
	else{alert("当前浏览器内核不支持。请按 Ctrl+D 快捷键手工添加。");}
}

function fhPrint(){
	document.body.className='print';
	window.print();
}

function setFontSize(s){
	$('#fontSize a').attr('class','');
	$('#'+s).addClass('red');
	$('#content').attr('class',s);
}
function ID(o){if(document.getElementById(o))return document.getElementById(o);}

function copyToClipBoard(){
var clipBoardContent='';
clipBoardContent+=document.title+'\r\n';
clipBoardContent+=window.location;
window.clipboardData.setData("Text",clipBoardContent);
alert("已复制链接及标题到剪贴板！");
}


function postDigg(ftype,aid){
	var saveid = getCookie('diggid');
	if(saveid != null)
	{
		var saveids = saveid.split(',');
		var hasid = false;
		saveid = '';
		j = 1;
		for(i=saveids.length-1;i>=0;i--)
		{
			if(saveids[i]==aid && hasid) continue;
			else {
				if(saveids[i]==aid && !hasid) hasid = true;
				saveid += (saveid=='' ? saveids[i] : ','+saveids[i]);
				j++;
				if(j==20 && hasid) break;
				if(j==19 && !hasid) break;
			}
		}
		if(hasid) {
		 tit='新闻网提示';
     // html="您已经顶过了，<br />发现其它好新闻再继续顶吧 ^-^";
     html="此新闻您已操作过，谢谢您！";
  		 dlg = new Dialog(html, {modal: false, height: 100, time: 2000, title: tit }).show();
		 return false;
		}
		else {saveid += ','+aid;$.getScript("/api/favour.php?action="+ftype+"&id="+aid)}
		setCookie('diggid',saveid,1);
	}
	else
	{	$.getScript("/api/favour.php?action="+ftype+"&id="+aid)
		setCookie('diggid',aid,1);
	}
}
function getDigg(ftype,aid){
	$.getScript("/api/favour.php?action="+ftype+"&id="+aid);
}

function getCookie(c_name){
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=")
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end   = document.cookie.indexOf(";",c_start);
            if (c_end == -1)
            {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return null
}

function setCookie(c_name,value,expiredays){
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + expiredays);
    document.cookie = c_name + "=" +escape(value) + ((expiredays == null) ? "" : ";expires=" + exdate.toGMTString()); //使设置的有效时间正确。增加toGMTString()
}

function soit(){
	s=$('#keyword').val();
	if(s==''||s=='请输入关键词...'){return false;}
}

function errDiv(n,t){
	if(n!=0){ID('postErr').className='';ID('errWin').innerHTML='<iframe id="IErr" border="0" frameborder="0" height="320" marginheight="1" marginwidth="1" name="IErr" scrolling="no" width="550" src="/api/erraddsave.php?aid='+n+'&title='+t+'"></iframe>';}else{ID('postErr').className='none';}
}

function jsonDB(){
  var arr=new Array();
  if($('#recommend').length>0)arr.push('recommend');
  if($('#photo').length>0)arr.push('photo');
  if($('#video').length>0)arr.push('video');
  if($('#latest').length>0)arr.push('latest');
  if($('#tuijian').length>0)arr.push('tuijian');

domain="//news.lzu.edu.cn";
imax=5;
var d = new Date();
m=d.getSeconds();
M=m % imax;
$.getJSON("/api/json.js",{Rand:Math.random()},function(feihuang){
	for(var j in arr){
    if(arr[j]=='recommend'){
      $.each(feihuang.cmdList,function(i,FH){
        if(i==6) return false;
        if(FH.l!='')$("#"+arr[j]+" ol").append("<li><span>"+FH.h+"</span> <a href='"+FH.b+"'>"+FH.l+"</a></li>");
      });
    }
		if(arr[j]=='tuijian'){
			$.each(feihuang.cmdList,function(i,FH){
				if(i==9) return false;
				if(FH.l!='')$("#"+arr[j]+" ol").append("<li><span>"+FH.h+"</span> <a href='"+FH.b+"'>"+FH.l+"</a></li>");
			});
		}
		if(arr[j]=='latest'){
			$.each(feihuang.latestList,function(i,FH){
				if(i==9) return false;
				if(FH.l!='')$("#"+arr[j]+" ol").append("<li><span>"+FH.h+"</span><a href='"+FH.b+"'>"+FH.l+"</a></li>");
			});
		}
		if(arr[j]=='photo'){
			$.each(feihuang.picList,function(i,FH){
				if(i==imax) return false;
				if(FH.l!=''){
					$("#"+arr[j]+" li:eq("+i+") a").attr('href',FH.b);
					$("#"+arr[j]+" li:eq("+i+") img").attr('src', domain+FH.p);
					$("#"+arr[j]+" li:eq("+i+") span").html(FH.l);
				}
			});
		}
		if(arr[j]=='video'){
			$.each(feihuang.videoList,function(i,FH){
        if(i>1) return false;
				// if(i==imax) return false;
        // if(FH.l!='' && i==M){//随机推荐一个视频
				if(FH.l!=''){
					$("#"+arr[j]+" a").attr('href',FH.b);
					$("#"+arr[j]+" a img").attr('src', domain+FH.p);
					$("#"+arr[j]+" a.txt").html(FH.l);
				}
			});
		}
	}
});

}

function counter(aid){
	curl=window.location.href;
	furl=document.referrer;
	tit=document.title.replace(' - 兰州大学新闻网','');
	if(aid>0)o='cnum';
	else o='hide';
	document.write('<scr'+'ipt type="text/javascript" src="/api/count.php?curl='+escape(curl)+'&furl='+escape(furl)+'&title='+tit+'&click=cnum&id='+aid+'"></script>');
}
function contImg(){
  $('#cont img').each(function(index, el) {
    src=$(this).attr('src');
    if(src.indexOf('//')<0){
      $(this).attr('src','//news.lzu.edu.cn'+src);
    }
    $(this).removeAttr('width');
    $(this).removeAttr('height');
    $(this).css({
      'max-width': '100%',
      'height': 'auto',
      'width': 'auto'
    });
  });
}

function showQrcode(n,tit){
	arr=new Array();
	arr[0]=new Array('兰州大学微信公众号二维码','http://news.lzu.edu.cn/new-media/fup/img/201707/07-20_152952-5.jpg');
	arr[1]=new Array('扫一扫，访问手机版','/public/img/urlcode.png');
  html='<img src="'+arr[n][1]+'" style="max-height:280px" alt="" />';
  dlg = new Dialog(html, {modal: false, height: 320, title: arr[n][0] }).show();
}
function makeCode () {
  var elText = document.getElementById("text");

  if (!elText.value) {
    alert("Input a text");
    elText.focus();
    return;
  }

  qrcode.makeCode(elText.value);
}
function getQrcode(){
  url=window.location.href;
  if(arguments.length==1)url=arguments[0];
  html="<div id='qrcodeImg'></div>";
  dlg = new Dialog(html, {modal: false, height: 230, title: '扫一扫，访问手机版' }).show();
  var qrcode = new QRCode(document.getElementById("qrcodeImg"), {
    width : 200, height : 200
  });
  qrcode.makeCode(url);
}

function showEmail(e,tit){
  html='<br />信箱地址：<br /><strong>'+e+'</strong><br /><br />如果您已经安装邮件客户端或者APP，<br />可 <a href="mailto:'+e+'"><strong>点击这里</strong></a> 直接发送邮件。';
  dlg = new Dialog(html, {modal: false, height: 200, title: tit }).show();
}

function img2bg(o){
	$(o+' img').each(function(index, el) {
		imgurl=$(this).attr('data-src').trim();
		$(this).parent().css('background-image', "url('"+'http://news.lzu.edu.cn'+imgurl+"')");
		$(this).hide();
	});
}
function thumbnailCheck(o){
  $(o+' li').each(function(i,e){
    imgurl='http://news.lzu.edu.cn'+$(this).attr('data-image');
    if(imgurl.indexOf('nopic.gif')>0){
      $(this).find('.thumbnail').remove();
      $(this).children().removeClass('hasimg');
    }
    p=$(this).find('p');
    if(p.text().length<5)p.remove();
    p.click(function(){window.location.href=$(this).attr('data-url');})
  });
}

function contFixed(){
// var e = this,
//  i = $(window).height(),
//  n = $(window).width(),
//  a = $("main").width(),
//  l = $(window).scrollTop(),
//  s = 0;
// var o = this,
//  f = $('body').find(".wechat-share-img").attr("src") || "",
//  m = $("header").height(),
//  p = $('body').offset().top,
//  g = p + $('body').outerHeight(),
//  w = $('body').find("#digg-share .inner"),
//  v = w.height() + 175,
//  x = $('body').find("#digg-share"),
//  A = x.offset().top - 175,
//  T = $('body').find("#next-news"),
//  _ = T.offset().top,
//  y = $('body').find("aside"),
//  R = y.offset().top - 175,
//  I = $('body').find("#latest"),
//  C = I.height();
//  if (_ - v > l && l > A ? w.addClass("fixed").css({
//      left: n / 2 - a / 2 + "px"
//    }) : w.removeClass("fixed").css({
//      left: "0px"
//    }), _ - (C + m) > l && l > R ? I.addClass("fixed").css({
//      right: n / 2 - a / 2 + "px"
//    }) : I.removeClass("fixed").css({
//      right: "0px"
//    }), 1 === s && p > l && l + i / 3 > p);
}

function mainNavPos(direction,x){
    if(direction==''){
      if(x<100)direction='right';
      else direction='left';
    }
    if(direction=='right'){
      pos = 0;
      cls = 'shade-right';
      ic = 'fh fh-toright';
    }
    else{
      pos = -300;
      cls = 'shade-left';
      ic = 'fh fh-toleft';
    }
    $("#main-nav").animate({"left":pos+"px"},400);
    $('#nav-shade').attr('class', cls);
    $('#nav-shade i').attr('class', ic);
}

$(function () {
	$("a[href*='http://']:not([href*='" + location.hostname + "']),[href$='.html']").attr("target", "_blank");
  var topnav = $('header .inner'),Header=$('header'),toTop = $('#totop'),w=$(window).width();

  $(window).scroll(function () {
    var top = $(window).scrollTop();
    if (top < 600) {
      toTop.fadeOut();
    } else {
      toTop.fadeIn();
    }
  });
  toTop.click(function () {
    $('html,body').animate({scrollTop: 0}, 500);
  });

  if (window.innerWidth>960) {
    $('#main-nav li').hover(function() {
      $(this).addClass('active');
    }, function() {
      $(this).removeClass('active');
    });

    $(window).scroll(function () {
      var top = $(window).scrollTop();
      // if (top > 1) {
	     // topnav.addClass('fixed fixedShadow');
      // } else {
	     // topnav.removeClass('fixed fixedShadow');
      // }
      if(top > 190 && w>1250){
        $('#digg-share').addClass('fixed2');
      }else {
        $('#digg-share').removeClass('fixed2');
      }
    });
  }else{// 移动端
    // 菜单处理
    $('.site-menus .so').last().append($('#so-top'));
    $('#so-top').removeClass('mob-none').css({'margin':'10px auto','background-color':'#FFFFFF'});
    $('#mob-menu').click(function(event) {
      $('#mob-fuwu,#mob-renyuan').slideUp('fast');
      $('.site-menus').last().toggle();
    });

    $('main,section').click(function(event) {
      $('.site-menus').last().slideUp('fast');
      $('#mob-fuwu,#mob-renyuan').slideUp('fast');
    });

    $('#nav-fuwu li span,#nav-renyuan li span').remove();
    $('#mob-fuwu').append($('#nav-fuwu li'));
    $('#mob-renyuan').append($('#nav-renyuan li'));

    $('#mob-service').click(function(event) {
      $('.site-menus').last().slideUp('fast');
      $('#mob-renyuan').slideUp('fast');
      $('#mob-fuwu').toggle('fast');
    });
    $('#mob-user').click(function(event) {
      $('.site-menus').last().slideUp('fast');
      $('#mob-fuwu').slideUp('fast');
      $('#mob-renyuan').toggle('fast');
    });

    //添加滑动事件
    $("#nav-shade").click(function(event) {
      pos=$(this).css('left');
      pos=parseInt(pos);
      mainNavPos('',pos);
    });
    $("#main-nav,#main-nav a,#main-nav li").swipe({
      swipe:function(event, direction, distance, duration, fingerCount) {
        mainNavPos(direction,-1);
      },
      threshold:0
    });

  }


  brmsg='<div style="border:1px #FFCA7E solid;background:#FFF4D2;width:100%;position:absolute;z-index:9999999999999;"><div style="border:1px #FFF solid;padding:6px 12px;text-align:center">您的IE浏览器版本比较低，请升级！如果是360、sogou等双核浏览器可切换到极速模式！</div></div>';
  if($.browser.msie){//低版本IE提示升级
    if(parseInt($.browser.version )<9){
      $('body').prepend(brmsg);
    }
  }else{
      console.info('Welcome to Lanzhou University! ');
      console.info(document.lastModified);
  }
  var userAgent = navigator.userAgent.toLowerCase();
  var rSafari = /version\/([\w.]+).*(safari)/;
  var matchBS;
  matchBS = rSafari.exec(userAgent);
  if (matchBS != null){
    $('body').addClass('safari'); // safari 手机浏览器对 background fixed 兼容性不好
    //if(matchBS[1] <= 8)$('body').prepend(brmsg.replace('IE','Safari '+matchBS[1])); //低版本Safari不支持CSS3，进行升级提示。
  }


  jsonDB();
  $('.slideBox').slideBox({direction : 'left', delay : 5, hideClickBar : false, clickBarRadius : 10});
});