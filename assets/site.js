(function(){
var r=document.documentElement,nav=document.getElementById("nav");
try{var t=localStorage.getItem("theme");if(t)r.setAttribute("data-theme",t);}catch(e){}
document.getElementById("theme").onclick=function(){
  var dark=r.getAttribute("data-theme")==="dark"||(!r.getAttribute("data-theme")&&matchMedia("(prefers-color-scheme:dark)").matches);
  var n=dark?"light":"dark";r.setAttribute("data-theme",n);try{localStorage.setItem("theme",n);}catch(e){}
};
document.getElementById("menu").onclick=function(){nav.classList.toggle("open");};
[].forEach.call(document.querySelectorAll("pre"),function(p){
  var b=document.createElement("button");b.className="cp";b.textContent="Copy";
  b.onclick=function(){var x=p.querySelector("code").innerText;
    (navigator.clipboard?navigator.clipboard.writeText(x):Promise.reject()).then(function(){b.textContent="Copied";setTimeout(function(){b.textContent="Copy";},1500);},function(){});};
  p.appendChild(b);
});
})();
