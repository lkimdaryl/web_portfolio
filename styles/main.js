document.addEventListener("DOMContentLoaded", function() {

    setTimeout(function() {
        var myImage = document.querySelector('#my-img');
        myImage.classList.add('in-focus');
    }, 100);

    setTimeout(function() {
        var myName = document.querySelector('#my-name');
        myName.classList.add('in-focus');
    }, 500);

    setTimeout(function() {
        var myTitle = document.querySelector('#title');
        myTitle.classList.add('in-focus');
    }, 1000);

    setTimeout(function() {
        var slogan = document.querySelector('#slogan');
        slogan.classList.add('in-focus');
    }, 1500);


})