let originalImage = null;
let encryptedImage = null;
let key = null;

function encryptImage() {
    if (!originalImage) {
        alert("Please select an image first.");
        return;
    }

    const context = document.getElementById('processedCanvas').getContext('2d');
    const imageData = context.getImageData(0, 0, context.canvas.width, context.canvas.height);
    const data = imageData.data;

    key = [];
    for (let i = 0; i < data.length; i++) {
        const randomValue = Math.floor(Math.random() * 256);
        key.push(randomValue);
        data[i] = data[i] ^ randomValue;
    }

    context.putImageData(imageData, 0, 0);
    encryptedImage = imageData;
    alert("Image encrypted successfully.");
}

function decryptImage() {
    if (!encryptedImage || !key) {
        alert("Please encrypt an image first.");
        return;
    }

    const context = document.getElementById('processedCanvas').getContext('2d');
    const imageData = context.getImageData(0, 0, context.canvas.width, context.canvas.height);
    const data = imageData.data;

    for (let i = 0; i < data.length; i++) {
        data[i] = data[i] ^ key[i];
    }

    context.putImageData(imageData, 0, 0);
    alert("Image decrypted successfully.");
}

function resetImage() {
    if (!originalImage) {
        alert("Please select an image first.");
        return;
    }

    const context = document.getElementById('processedCanvas').getContext('2d');
    context.drawImage(originalImage, 0, 0, context.canvas.width, context.canvas.height);
    encryptedImage = null;
    key = null;
    alert("Image reset to original.");
}

function saveImage() {
    if (!encryptedImage) {
        alert("No encrypted image to save.");
        return;
    }

    const canvas = document.getElementById('processedCanvas');
    const link = document.createElement('a');
    link.href = canvas.toDataURL();
    link.download = 'encrypted_image.png';
    link.click();
}

document.getElementById('imageInput').addEventListener('change', (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
            const maxCanvasSize = 500;
            const canvas = document.getElementById('originalCanvas');
            const context = canvas.getContext('2d');

            // Resize image if larger than maxCanvasSize
            let scaleFactor = Math.min(maxCanvasSize / img.width, maxCanvasSize / img.height);
            canvas.width = img.width * scaleFactor;
            canvas.height = img.height * scaleFactor;
            context.drawImage(img, 0, 0, canvas.width, canvas.height);

            const processedCanvas = document.getElementById('processedCanvas');
            const processedContext = processedCanvas.getContext('2d');
            processedCanvas.width = canvas.width;
            processedCanvas.height = canvas.height;
            processedContext.drawImage(img, 0, 0, processedCanvas.width, processedCanvas.height);

            originalImage = img;
        };
        img.src = e.target.result;
    };

    reader.readAsDataURL(file);
});
