document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault(); // Formun varsayılan davranışını engelle
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage('Sen', message); // Kullanıcı mesajını ekle

        try {
            const response = await fetch('/get_response', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `message=${encodeURIComponent(message)}`
            });

            const data = await response.json();
            appendMessage('Protesq Bot', data.response); // Bot yanıtını ekle
        } catch (error) {
            console.error('Hata:', error);
            appendMessage('Protesq Bot', 'Üzgünüm, bir hata oluştu.');
        }

        userInput.value = ''; // Mesaj girişini temizle
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message';
        messageElement.innerHTML = `<strong>${sender}:</strong> ${escapeHTML(message)}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll'u en alta kaydır
    }

    function escapeHTML(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
});
