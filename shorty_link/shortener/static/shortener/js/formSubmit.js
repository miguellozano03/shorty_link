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

        shortUrlContainer.innerHTML = data.error ? `Error: ${data.error}` : `Your url: ${data.short_url}`;
        
    })

})
