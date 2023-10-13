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

    var MVPBttn = document.querySelector('#MVP-bttn');
    MVPBttn.addEventListener('click', event => {
        window.open('https://github.com/lkimdaryl/MVPIdeation', '_blank')
    })

    var RMSBttn = document.querySelector('#RMS-bttn');
    RMSBttn.addEventListener('click', event => {
        window.open('https://github.com/lkimdaryl/Restaurant_Management_System', '_blank')
    });

    var SBBttn = document.querySelector('#SB-bttn');
    SBBttn.addEventListener('click', event => {
        window.open('https://github.com/lkimdaryl/SecureBand', '_blank')
    })

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = JSON.stringify(Object.fromEntries(new FormData(form)));
        const url = form.action;

        fetch(url, {
            credentials: 'same-origin',
            method: form.method,
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => {
            showNotification(data['Status']);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });
});

function showNotification(status){
    const form = document.getElementById("messageForm");
    const nameInput = document.getElementById("name");
    const messageTextarea = document.getElementById("message");
    const notification = document.getElementById("notification");
    if (status === "Success"){
        messageTextarea.value = "";
        messageTextarea.placeholder = "";
        nameInput.value = "";
        notification.textContent = "Message Sent Successfully!";
        notification.classList.add("show-success");
        setTimeout(function () {
            messageTextarea.placeholder = "Enter your message here";
            notification.classList.remove("show-success");
        }, 2000);
    }else{
        messageTextarea.value = "";
        messageTextarea.placeholder = "";
        nameInput.value = "";
        notification.textContent = "Sending Message Failed.";
        notification.classList.add("show-fail");
        setTimeout(function () {
            messageTextarea.placeholder = "Enter your message here";
            notification.classList.remove("show-fail");
        }, 2000);
    }
}