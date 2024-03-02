function removeElement() {
    var element = document.getElementById('main_div');
    var element2=document.getElementById('main_div2');
    var element3=document.getElementById('t2m');
    var element4=document.getElementById('t2m2');
    var element5=document.getElementById('ed2');
    var element6=document.getElementById('ed1');
    element.style.display = 'none';
    if (element) {
        element.style.display = 'none';
        element2.style.display = 'block';
        element3.style.display = 'none';
        element4.style.display = 'block';
        element5.style.backgroundColor = "#092e3b";
        element6.style.backgroundColor = "#176B87";

 
    }
}


function reappearElement() {
    var element = document.getElementById('main_div');
    var element2 = document.getElementById('main_div2');
    var element3=document.getElementById('t2m');
    var element4=document.getElementById('t2m2');
    var element5=document.getElementById('ed2');
    var element6=document.getElementById('ed1');

    if (element) {
        element.style.display = 'block'; 
        element2.style.display = 'none'; 
        element3.style.display = 'block';
        element4.style.display = 'none';
        element6.style.backgroundColor = "#092e3b";
        element5.style.backgroundColor = "#176B87";

        
    }
}