const imagePreview = document.getElementById('image-preview');
const imageName = document.getElementById('image-name');
const resultsList = document.getElementById('results-list');
const fileInput = document.getElementById('file-input');
const selectImageButton = document.getElementById('select-image-button');
const startClassificationButton = document.getElementById('start-classification-button');

selectImageButton.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
        };
        reader.readAsDataURL(file);
        imageName.textContent = file.name;
        resultsList.innerHTML = ''; // Clear previous results
    }
});

startClassificationButton.addEventListener('click', () => {
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select an image first.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    resultsList.innerHTML = '<li>Classifying...</li>';

    fetch('http://127.0.0.1:5000/classify', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        resultsList.innerHTML = '';
        if (data.results) {
            data.results.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result;
                resultsList.appendChild(li);
            });
        } else if (data.error) {
            const li = document.createElement('li');
            li.textContent = `Error: ${data.error}`;
            resultsList.appendChild(li);
        }
    })
    .catch(error => {
        resultsList.innerHTML = '';
        const li = document.createElement('li');
        li.textContent = `Error: ${error.message}`;
        resultsList.appendChild(li);
    });
});