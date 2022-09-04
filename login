<html>
<html xmlns="http://www.w3.org/1999/xhtml!>
  <head>
  <meta charset = "utf-8">
  <meta name="generator" content="pdf2htmlEX">
  <meta hettp-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
  <style type="text/css">
    /*! 
Base CSS for pdf2htmlEX * Copyright 2012,2013 Lu Wang <coolwanglu@gmail.com> * https://github.com/pdf2htmlEX/pdf2htmlEX/blob/master/share/LICENSE */
#sidebar{
    position:absolute;
    top:0;
    left:0;
    bottom:0;
    width:250px;
    padding:0;
    margin:0;
    overflow:auto
}
#page-container{
    position:absolute;
    top:0;
    left:0;
    margin:0;
    padding:0;
    border:0
}
@media screen{
    #sidebar.opened+#page-container{
        left:250px
    }
    #page-container{
        bottom:0;
        right:0;
        overflow:auto
    }
    .loading-indicator{
        display:none
    }
    .loading-indicator.active{
        display:block;
        position:absolute;
        width:64px;
        height:64px;
        top:50%;
        left:50%;
        margin-top:-32px;
        margin-left:-32px
    }
    .loading-indicator img{
        position:absolute;
        top:0;
        left:0;
        bottom:0;
        right:0
    }
}
@media print{
    @page{
        margin:0
    }
    html{
        margin:0
    }
    body{
        margin:0;
        -webkit-print-color-adjust:exact
    }
    #sidebar{
        display:none
    }
    #page-container{
        width:auto;
        height:auto;
        overflow:visible;
        background-color:transparent
    }
    .d{
        display:none
    }
}
.pf{
    position:relative;
    background-color:white;
    overflow:hidden;
    margin:0;
    border:0
}
.pc{
    position:absolute;
    border:0;
    padding:0;
    margin:0;
    top:0;
    left:0;
    width:100%;
    height:100%;
    overflow:hidden;
    display:block;
    transform-origin:0 0;
    -ms-transform-origin:0 0;
    -webkit-transform-origin:0 0
}
.pc.opened{
    display:block
}
.bf{
    position:absolute;
    border:0;
    margin:0;
    top:0;
    bottom:0;
    width:100%;
    height:100%;
    -ms-user-select:none;
    -moz-user-select:none;
    -webkit-user-select:none;
    user-select:none
}
.bi{
    position:absolute;
    border:0;
    margin:0;
    -ms-user-select:none;
    -moz-user-select:none;
    -webkit-user-select:none;
    user-select:none
}
@media print{
    .pf{
        margin:0;
        box-shadow:none;
        page-break-after:always;
        page-break-inside:avoid
    }
    @-moz-document url-prefix(){
        .pf{
            overflow:visible;
            border:1px solid #fff
        }
        .pc{
            overflow:visible
        }
    }
}
.c{
    position:absolute;
    border:0;
    padding:0;
    margin:0;
    overflow:hidden;
    display:block
}
.t{
    position:absolute;
    white-space:pre;
    font-size:1px;
    transform-origin:0 100%;
    -ms-transform-origin:0 100%;
    -webkit-transform-origin:0 100%;
    unicode-bidi:bidi-override;
    -moz-font-feature-settings:"liga" 0
}
.t:after{
    content:''
}
.t:before{
    content:'';
    display:inline-block
}
.t span{
    position:relative;
    unicode-bidi:bidi-override
}
._{
    display:inline-block;
    color:transparent;
    z-index:-1
}
::selection{
    background:rgba(127,255,255,0.4)
}
::-moz-selection{
    background:rgba(127,255,255,0.4)
}
.pi{
    display:none
}
.d{
    position:absolute;
    transform-origin:0 100%;
    -ms-transform-origin:0 100%;
    -webkit-transform-origin:0 100%
}
.it{
    border:0;
    background-color:rgba(255,255,255,0.0)
}
.ir:hover{
    cursor:pointer
}
</style>

<style type="text/css">
/*! * Fancy styles for pdf2htmlEX * Copyright 2012,2013 Lu Wang <coolwanglu@gmail.com> * https://github.com/pdf2htmlEX/pdf2htmlEX/blob/master/share/LICENSE */
@keyframes fadein{
    from{
        opacity:0
    }
    to{
        opacity:1
    }
}
@-webkit-keyframes fadein{
    from{
        opacity:0
    }
    to{
        opacity:1
    }
}
@keyframes swing{
    0{
        transform:rotate(0)
    }
    10%{
        transform:rotate(0)
    }
    90%{
        transform:rotate(720deg)
    }
    100%{
        transform:rotate(720deg)
    }
}
@-webkit-keyframes swing{
    0{
        -webkit-transform:rotate(0)
    }
    10%{
        -webkit-transform:rotate(0)
    }
    90%{
        -webkit-transform:rotate(720deg)
    }
    100%{
        -webkit-transform:rotate(720deg)
    }
}
@media screen{
    #sidebar{
        background-color:#2f3236;
        background-image:url("data:image/svg+xml;
        base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0IiBoZWlnaHQ9IjQiPgo8cmVjdCB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSIjNDAzYzNmIj48L3JlY3Q+CjxwYXRoIGQ9Ik0wIDBMNCA0Wk00IDBMMCA0WiIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2U9IiMxZTI5MmQiPjwvcGF0aD4KPC9zdmc+")
    }
    #outline{
        font-family:Georgia,Times,"Times New Roman",serif;
        font-size:13px;
        margin:2em 1em
    }
    #outline ul{
        padding:0
    }
    #outline li{
        list-style-type:none;
        margin:1em 0
    }
    #outline li>ul{
        margin-left:1em
    }
    #outline a,#outline a:visited,#outline a:hover,#outline a:active{
        line-height:1.2;
        color:#e8e8e8;
        text-overflow:ellipsis;
        white-space:nowrap;
        text-decoration:none;
        display:block;
        overflow:hidden;
        outline:0
    }
    #outline a:hover{
        color:#0cf
    }
    #page-container{
        background-color:#9e9e9e;
        background-image:url("data:image/svg+xml;
        base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1IiBoZWlnaHQ9IjUiPgo8cmVjdCB3aWR0aD0iNSIgaGVpZ2h0PSI1IiBmaWxsPSIjOWU5ZTllIj48L3JlY3Q+CjxwYXRoIGQ9Ik0wIDVMNSAwWk02IDRMNCA2Wk0tMSAxTDEgLTFaIiBzdHJva2U9IiM4ODgiIHN0cm9rZS13aWR0aD0iMSI+PC9wYXRoPgo8L3N2Zz4=");
        -webkit-transition:left 500ms;
        transition:left 500ms
    }
    .pf{
        margin:13px auto;
        box-shadow:1px 1px 3px 1px #333;
        border-collapse:separate
    }
    .pc.opened{
        -webkit-animation:fadein 100ms;
        animation:fadein 100ms
    }
    .loading-indicator.active{
        -webkit-animation:swing 1.5s ease-in-out .01s infinite alternate none;
        animation:swing 1.5s ease-in-out .01s infinite alternate none
    }
    .checked{
        background:no-repeat url(data:image/png;
        base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3goQDSYgDiGofgAAAslJREFUOMvtlM9LFGEYx7/vvOPM6ywuuyPFihWFBUsdNnA6KLIh+QPx4KWExULdHQ/9A9EfUodYmATDYg/iRewQzklFWxcEBcGgEplDkDtI6sw4PzrIbrOuedBb9MALD7zv+3m+z4/3Bf7bZS2bzQIAcrmcMDExcTeXy10DAFVVAQDksgFUVZ1ljD3yfd+0LOuFpmnvVVW9GHhkZAQcxwkNDQ2FSCQyRMgJxnVdy7KstKZpn7nwha6urqqfTqfPBAJAuVymlNLXoigOhfd5nmeiKL5TVTV+lmIKwAOA7u5u6Lped2BsbOwjY6yf4zgQQkAIAcedaPR9H67r3uYBQFEUFItFtLe332lpaVkUBOHK3t5eRtf1DwAwODiIubk5DA8PM8bYW1EU+wEgCIJqsCAIQAiB7/u253k2BQDDMJBKpa4mEon5eDx+UxAESJL0uK2t7XosFlvSdf0QAEmlUnlRFJ9Waho2Qghc1/U9z3uWz+eX+Wr+lL6SZfleEAQIggA8z6OpqSknimIvYyybSCReMsZ6TislhCAIAti2Dc/zejVNWwCAavN8339j27YbTg0AGGM3WltbP4WhlRWq6Q/btrs1TVsYHx+vNgqKoqBUKn2NRqPFxsbGJzzP05puUlpt0ukyOI6z7zjOwNTU1OLo6CgmJyf/gA3DgKIoWF1d/cIY24/FYgOU0pp0z/Ityzo8Pj5OTk9PbwHA+vp6zWghDC+VSiuRSOQgGo32UErJ38CO42wdHR09LBQK3zKZDDY2NupmFmF4R0cHVlZWlmRZ/iVJUn9FeWWcCCE4ODjYtG27Z2Zm5juAOmgdGAB2d3cBADs7O8uSJN2SZfl+WKlpmpumaT6Yn58vn/fs6XmbhmHMNjc3tzDGFI7jYJrm5vb29sDa2trPC/9aiqJUy5pOp4f6+vqeJ5PJBAB0dnZe/t8NBajx/z37Df5OGX8d13xzAAAAAElFTkSuQmCC)
    }
}
</style>

<style type="text/css">
.ff0{
    font-family:sans-serif;
    visibility:hidden;
}
 .sc_{
    text-shadow:none;
}
 @media screen and (-webkit-min-device-pixel-ratio:0){
     .sc_{
        -webkit-text-stroke:0px transparent;
    }
}
 .y0{
    bottom:-0.500000px;
}
 .h0{
    height:768.000000px;
}
 .h1{
    height:768.500000px;
}
 .w0{
    width:1080.000000px;
}
 .w1{
    width:1080.500000px;
}
 .x0{
    left:0.000000px;
}
 @media print{
     .y0{
        bottom:-0.666667pt;
    }
     .h0{
        height:1024.000000pt;
    }
     .h1{
        height:1024.666667pt;
    }
     .w0{
        width:1440.000000pt;
    }
     .w1{
        width:1440.666667pt;
    }
     .x0{
        left:0.000000pt;
    }
}
</style>
<script>
/*
 Copyright 2012 Mozilla Foundation 
 Copyright 2013 Lu Wang <coolwanglu@gmail.com>
 Apachine License Version 2.0 
*/
(function(){function b(a,b,e,f){var c=(a.className||"").split(/\s+/g);""===c[0]&&c.shift();var d=c.indexOf(b);0>d&&e&&c.push(b);0<=d&&f&&c.splice(d,1);a.className=c.join(" ");return 0<=d}if(!("classList"in document.createElement("div"))){var e={add:function(a){b(this.element,a,!0,!1)},contains:function(a){return b(this.element,a,!1,!1)},remove:function(a){b(this.element,a,!1,!0)},toggle:function(a){b(this.element,a,!0,!0)}};Object.defineProperty(HTMLElement.prototype,"classList",{get:function(){if(this._classList)return this._classList;
var a=Object.create(e,{element:{value:this,writable:!1,enumerable:!0}});Object.defineProperty(this,"_classList",{value:a,writable:!1,enumerable:!1});return a},enumerable:!0})}})();
</script>
<script>
(function(){/*
 pdf2htmlEX.js: Core UI functions for pdf2htmlEX 
 Copyright 2012,2013 Lu Wang <coolwanglu@gmail.com> and other contributors 
 https://github.com/pdf2htmlEX/pdf2htmlEX/blob/master/share/LICENSE 
*/
var pdf2htmlEX=window.pdf2htmlEX=window.pdf2htmlEX||{},CSS_CLASS_NAMES={page_frame:"pf",page_content_box:"pc",page_data:"pi",background_image:"bi",link:"l",input_radio:"ir",__dummy__:"no comma"},DEFAULT_CONFIG={container_id:"page-container",sidebar_id:"sidebar",outline_id:"outline",loading_indicator_cls:"loading-indicator",preload_pages:3,render_timeout:100,scale_step:0.9,key_handler:!0,hashchange_handler:!0,view_history_handler:!0,__dummy__:"no comma"},EPS=1E-6;
function invert(a){var b=a[0]*a[3]-a[1]*a[2];return[a[3]/b,-a[1]/b,-a[2]/b,a[0]/b,(a[2]*a[5]-a[3]*a[4])/b,(a[1]*a[4]-a[0]*a[5])/b]}function transform(a,b){return[a[0]*b[0]+a[2]*b[1]+a[4],a[1]*b[0]+a[3]*b[1]+a[5]]}function get_page_number(a){return parseInt(a.getAttribute("data-page-no"),16)}function disable_dragstart(a){for(var b=0,c=a.length;b<c;++b)a[b].addEventListener("dragstart",function(){return!1},!1)}
function clone_and_extend_objs(a){for(var b={},c=0,e=arguments.length;c<e;++c){var h=arguments[c],d;for(d in h)h.hasOwnProperty(d)&&(b[d]=h[d])}return b}
function Page(a){if(a){this.shown=this.loaded=!1;this.page=a;this.num=get_page_number(a);this.original_height=a.clientHeight;this.original_width=a.clientWidth;var b=a.getElementsByClassName(CSS_CLASS_NAMES.page_content_box)[0];b&&(this.content_box=b,this.original_scale=this.cur_scale=this.original_height/b.clientHeight,this.page_data=JSON.parse(a.getElementsByClassName(CSS_CLASS_NAMES.page_data)[0].getAttribute("data-data")),this.ctm=this.page_data.ctm,this.ictm=invert(this.ctm),this.loaded=!0)}}
Page.prototype={hide:function(){this.loaded&&this.shown&&(this.content_box.classList.remove("opened"),this.shown=!1)},show:function(){this.loaded&&!this.shown&&(this.content_box.classList.add("opened"),this.shown=!0)},rescale:function(a){this.cur_scale=0===a?this.original_scale:a;this.loaded&&(a=this.content_box.style,a.msTransform=a.webkitTransform=a.transform="scale("+this.cur_scale.toFixed(3)+")");a=this.page.style;a.height=this.original_height*this.cur_scale+"px";a.width=this.original_width*this.cur_scale+
"px"},view_position:function(){var a=this.page,b=a.parentNode;return[b.scrollLeft-a.offsetLeft-a.clientLeft,b.scrollTop-a.offsetTop-a.clientTop]},height:function(){return this.page.clientHeight},width:function(){return this.page.clientWidth}};function Viewer(a){this.config=clone_and_extend_objs(DEFAULT_CONFIG,0<arguments.length?a:{});this.pages_loading=[];this.init_before_loading_content();var b=this;document.addEventListener("DOMContentLoaded",function(){b.init_after_loading_content()},!1)}
Viewer.prototype={scale:1,cur_page_idx:0,first_page_idx:0,init_before_loading_content:function(){this.pre_hide_pages()},initialize_radio_button:function(){for(var a=document.getElementsByClassName(CSS_CLASS_NAMES.input_radio),b=0;b<a.length;b++)a[b].addEventListener("click",function(){this.classList.toggle("checked")})},init_after_loading_content:function(){this.sidebar=document.getElementById(this.config.sidebar_id);this.outline=document.getElementById(this.config.outline_id);this.container=document.getElementById(this.config.container_id);
this.loading_indicator=document.getElementsByClassName(this.config.loading_indicator_cls)[0];for(var a=!0,b=this.outline.childNodes,c=0,e=b.length;c<e;++c)if("ul"===b[c].nodeName.toLowerCase()){a=!1;break}a||this.sidebar.classList.add("opened");this.find_pages();if(0!=this.pages.length){disable_dragstart(document.getElementsByClassName(CSS_CLASS_NAMES.background_image));this.config.key_handler&&this.register_key_handler();var h=this;this.config.hashchange_handler&&window.addEventListener("hashchange",
function(a){h.navigate_to_dest(document.location.hash.substring(1))},!1);this.config.view_history_handler&&window.addEventListener("popstate",function(a){a.state&&h.navigate_to_dest(a.state)},!1);this.container.addEventListener("scroll",function(){h.update_page_idx();h.schedule_render(!0)},!1);[this.container,this.outline].forEach(function(a){a.addEventListener("click",h.link_handler.bind(h),!1)});this.initialize_radio_button();this.render()}},find_pages:function(){for(var a=[],b={},c=this.container.childNodes,
e=0,h=c.length;e<h;++e){var d=c[e];d.nodeType===Node.ELEMENT_NODE&&d.classList.contains(CSS_CLASS_NAMES.page_frame)&&(d=new Page(d),a.push(d),b[d.num]=a.length-1)}this.pages=a;this.page_map=b},load_page:function(a,b,c){var e=this.pages;if(!(a>=e.length||(e=e[a],e.loaded||this.pages_loading[a]))){var e=e.page,h=e.getAttribute("data-page-url");if(h){this.pages_loading[a]=!0;var d=e.getElementsByClassName(this.config.loading_indicator_cls)[0];"undefined"===typeof d&&(d=this.loading_indicator.cloneNode(!0),
d.classList.add("active"),e.appendChild(d));var f=this,g=new XMLHttpRequest;g.open("GET",h,!0);g.onload=function(){if(200===g.status||0===g.status){var b=document.createElement("div");b.innerHTML=g.responseText;for(var d=null,b=b.childNodes,e=0,h=b.length;e<h;++e){var p=b[e];if(p.nodeType===Node.ELEMENT_NODE&&p.classList.contains(CSS_CLASS_NAMES.page_frame)){d=p;break}}b=f.pages[a];f.container.replaceChild(d,b.page);b=new Page(d);f.pages[a]=b;b.hide();b.rescale(f.scale);disable_dragstart(d.getElementsByClassName(CSS_CLASS_NAMES.background_image));
f.schedule_render(!1);c&&c(b)}delete f.pages_loading[a]};g.send(null)}void 0===b&&(b=this.config.preload_pages);0<--b&&(f=this,setTimeout(function(){f.load_page(a+1,b)},0))}},pre_hide_pages:function(){var a="@media screen{."+CSS_CLASS_NAMES.page_content_box+"{display:none;}}",b=document.createElement("style");b.styleSheet?b.styleSheet.cssText=a:b.appendChild(document.createTextNode(a));document.head.appendChild(b)},render:function(){for(var a=this.container,b=a.scrollTop,c=a.clientHeight,a=b-c,b=
b+c+c,c=this.pages,e=0,h=c.length;e<h;++e){var d=c[e],f=d.page,g=f.offsetTop+f.clientTop,f=g+f.clientHeight;g<=b&&f>=a?d.loaded?d.show():this.load_page(e):d.hide()}},update_page_idx:function(){var a=this.pages,b=a.length;if(!(2>b)){for(var c=this.container,e=c.scrollTop,c=e+c.clientHeight,h=-1,d=b,f=d-h;1<f;){var g=h+Math.floor(f/2),f=a[g].page;f.offsetTop+f.clientTop+f.clientHeight>=e?d=g:h=g;f=d-h}this.first_page_idx=d;for(var g=h=this.cur_page_idx,k=0;d<b;++d){var f=a[d].page,l=f.offsetTop+f.clientTop,
f=f.clientHeight;if(l>c)break;f=(Math.min(c,l+f)-Math.max(e,l))/f;if(d===h&&Math.abs(f-1)<=EPS){g=h;break}f>k&&(k=f,g=d)}this.cur_page_idx=g}},schedule_render:function(a){if(void 0!==this.render_timer){if(!a)return;clearTimeout(this.render_timer)}var b=this;this.render_timer=setTimeout(function(){delete b.render_timer;b.render()},this.config.render_timeout)},register_key_handler:function(){var a=this;window.addEventListener("DOMMouseScroll",function(b){if(b.ctrlKey){b.preventDefault();var c=a.container,
e=c.getBoundingClientRect(),c=[b.clientX-e.left-c.clientLeft,b.clientY-e.top-c.clientTop];a.rescale(Math.pow(a.config.scale_step,b.detail),!0,c)}},!1);window.addEventListener("keydown",function(b){var c=!1,e=b.ctrlKey||b.metaKey,h=b.altKey;switch(b.keyCode){case 61:case 107:case 187:e&&(a.rescale(1/a.config.scale_step,!0),c=!0);break;case 173:case 109:case 189:e&&(a.rescale(a.config.scale_step,!0),c=!0);break;case 48:e&&(a.rescale(0,!1),c=!0);break;case 33:h?a.scroll_to(a.cur_page_idx-1):a.container.scrollTop-=
a.container.clientHeight;c=!0;break;case 34:h?a.scroll_to(a.cur_page_idx+1):a.container.scrollTop+=a.container.clientHeight;c=!0;break;case 35:a.container.scrollTop=a.container.scrollHeight;c=!0;break;case 36:a.container.scrollTop=0,c=!0}c&&b.preventDefault()},!1)},rescale:function(a,b,c){var e=this.scale;this.scale=a=0===a?1:b?e*a:a;c||(c=[0,0]);b=this.container;c[0]+=b.scrollLeft;c[1]+=b.scrollTop;for(var h=this.pages,d=h.length,f=this.first_page_idx;f<d;++f){var g=h[f].page;if(g.offsetTop+g.clientTop>=
c[1])break}g=f-1;0>g&&(g=0);var g=h[g].page,k=g.clientWidth,f=g.clientHeight,l=g.offsetLeft+g.clientLeft,m=c[0]-l;0>m?m=0:m>k&&(m=k);k=g.offsetTop+g.clientTop;c=c[1]-k;0>c?c=0:c>f&&(c=f);for(f=0;f<d;++f)h[f].rescale(a);b.scrollLeft+=m/e*a+g.offsetLeft+g.clientLeft-m-l;b.scrollTop+=c/e*a+g.offsetTop+g.clientTop-c-k;this.schedule_render(!0)},fit_width:function(){var a=this.cur_page_idx;this.rescale(this.container.clientWidth/this.pages[a].width(),!0);this.scroll_to(a)},fit_height:function(){var a=this.cur_page_idx;
this.rescale(this.container.clientHeight/this.pages[a].height(),!0);this.scroll_to(a)},get_containing_page:function(a){for(;a;){if(a.nodeType===Node.ELEMENT_NODE&&a.classList.contains(CSS_CLASS_NAMES.page_frame)){a=get_page_number(a);var b=this.page_map;return a in b?this.pages[b[a]]:null}a=a.parentNode}return null},link_handler:function(a){var b=a.target,c=b.getAttribute("data-dest-detail");if(c){if(this.config.view_history_handler)try{var e=this.get_current_view_hash();window.history.replaceState(e,
"","#"+e);window.history.pushState(c,"","#"+c)}catch(h){}this.navigate_to_dest(c,this.get_containing_page(b));a.preventDefault()}},navigate_to_dest:function(a,b){try{var c=JSON.parse(a)}catch(e){return}if(c instanceof Array){var h=c[0],d=this.page_map;if(h in d){for(var f=d[h],h=this.pages[f],d=2,g=c.length;d<g;++d){var k=c[d];if(null!==k&&"number"!==typeof k)return}for(;6>c.length;)c.push(null);var g=b||this.pages[this.cur_page_idx],d=g.view_position(),d=transform(g.ictm,[d[0],g.height()-d[1]]),
g=this.scale,l=[0,0],m=!0,k=!1,n=this.scale;switch(c[1]){case "XYZ":l=[null===c[2]?d[0]:c[2]*n,null===c[3]?d[1]:c[3]*n];g=c[4];if(null===g||0===g)g=this.scale;k=!0;break;case "Fit":case "FitB":l=[0,0];k=!0;break;case "FitH":case "FitBH":l=[0,null===c[2]?d[1]:c[2]*n];k=!0;break;case "FitV":case "FitBV":l=[null===c[2]?d[0]:c[2]*n,0];k=!0;break;case "FitR":l=[c[2]*n,c[5]*n],m=!1,k=!0}if(k){this.rescale(g,!1);var p=this,c=function(a){l=transform(a.ctm,l);m&&(l[1]=a.height()-l[1]);p.scroll_to(f,l)};h.loaded?
c(h):(this.loa…
</script>
<script> try{ pdf2htmlEX.defaultViewer = new pdf2htmlEX.Viewer({}); }catch(e){} </script>
<style>@media screen{.pc{display:none;}}</style>
<title>PEGABOT Login</title>
</head>

<body>
<div id="sidebar">
  <div id="outline"> </div>
  </div>
<div id="page-container">
  <div id="pf1" class="pf w0 h0" data-page-no="1"> ==$0
    <div class="pc pc1 w0 h0 opened">
      <img class="bi x0 y0 w1 h1" alt src="data:image/png;base64,iVBOR…+H8kJypg7UcGlAAAAAElFTkSuQmCC">
     </div>
     <div class="pi" data-data="{"ctm":[1.000000,0.000000,0.000000,1.000000,0.000000,0.000000]}"></div>
    </div>
   </div>
  <div class="loading-indicator">
    <img alt src="data:image/png;base64,iVBOR…XF+mWyZITVTkAAAAASUVORK5CYII=">
   </div> == $0
</body>
</html>
