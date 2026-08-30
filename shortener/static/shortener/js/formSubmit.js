console.log("Hello world");

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('shorty-form');
    const inputForm = document.getElementById('form-input');
    const shortUrlContainer = document.getElementById('result');

    form.addEventListener('submit', async e => {
        e.preventDefault();

        const originalUrl = inputForm.value;
        const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        console.log(originalUrl);
        const response = await fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({"url": originalUrl})
        });
        
        const data = await response.json();

        shortUrlContainer.innerHTML = data.error ? `Error: ${data.error}` : `Your url: <a href="${data.short_url}" target="_blank">${data.short_url}</a>`;


        const resultContainer = document.getElementById('result-container');

        if (data.error || data.short_url) {
            resultContainer.classList.add('show');
        } else {
          resultContainer.classList.remove('show');
        }

        shortUrlContainer.className = data.error ? 'error' : '';
        
    })

})
