function changeText(id){
    id.innerHTML = "Hola";
}

function abrirFacebook(){
    window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(location));
}

function myFunction(imgs) {
    var expandImg = document.getElementById("expandedImg");
    var imgText = document.getElementById("imgtext");
    expandImg.src = imgs.src;
    expandImg.parentElement.style.display = "block";
  }