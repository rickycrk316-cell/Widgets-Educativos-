// Ayudas comunes a todos los simuladores (las une el integrador al inicio de 90_sim.html).
// El kit ya define sel(dc,g), num(dc,n), out(dc,html) y rd(x,d). No redefinas nombres reservados:
// show ir tog ch sel num out rd recon tabla par hv vacio. Tus ayudas privadas llevan prefijo de ejecutor (e1_, e23_, e45_, vis_).
function par(t){return '<p>'+t+'</p>';}
function hv(a,v){return a.indexOf(v)>-1;}
function vacio(dc,t){out(dc,par(t));}
