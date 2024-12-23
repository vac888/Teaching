//function getCookie(name) {
//    const value = `; ${document.cookie}`;
//    const parts = value.split(`; ${name}=`);
//    if (parts.length === 2) return parts.pop().split(';').shift();
//}

//const username = getCookie('username');

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function hideButton() {
        document.getElementById('open-modal-btn').style.display = 'none';
        setCookie('hideButton', 'true', 365); // Сохраняем на 1 год
        document.getElementById('open-modal-btn2').style.display = 'none';
        setCookie('hideButton2', 'true', 365); // Сохраняем на 1 год
        document.getElementById('open-modal-btn3').style.display = 'block';
        setCookie('hideButton3', 'true', 365); // Сохраняем на 1 год
        setCookie('username', 'true', 365);
}

window.onload = function() {
    console.log(document.getElementById('open-modal-btn').style.display);
    if (getCookie('hideButton') === 'true' && getCookie('hideButton2') === 'true' && getCookie('hideButton3') === 'true') {
        document.getElementById('open-modal-btn').style.display = 'none';
        document.getElementById('open-modal-btn2').style.display = 'none';
        document.getElementById('open-modal-btn3').style.display = 'block';
    } else {
        document.getElementById('open-modal-btn').style.display = 'block';
        document.getElementById('open-modal-btn2').style.display = 'block';
        document.getElementById('open-modal-btn3').style.display = 'none';
        deleteCookie('username');
    }
};

function showButton() {
    document.getElementById('open-modal-btn').style.display = 'block';
    deleteCookie('hideButton');
    document.getElementById('open-modal-btn2').style.display = 'block';
    deleteCookie('hideButton2');
    location.reload();
}

function deleteCookie(name) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/;';
    document.cookie = 'username' + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/;';
}
