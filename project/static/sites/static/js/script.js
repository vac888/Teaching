document.getElementById("submitObject").addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение отправки формы

    // Получаем значение из поля ввода
    const selectElement = document.getElementById('object-select');

    const selectedValue = selectElement.value;
        
    var formData = new FormData();
    formData.append('inputText', selectedValue);

    // Создаем объект FormData для отправки данных

    // Отправляем данные на сервер с помощью fetch
    fetch('post_1.html/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // CSRF token для защиты от CSRF-атак
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успех:', data);
        // Здесь можно добавить обработку ответа от сервера
    })
    .catch((error) => {
        console.error('Ошибка:', error);
    });

});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}