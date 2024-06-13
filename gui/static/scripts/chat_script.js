async function sendQuery() {
    const queryInput = document.getElementById('chat-input');
    const query = queryInput.value;

    if (query.trim() === '') return;

    const chatbox = document.getElementById('chat-box');
    chatbox.innerHTML += `<div class="message user"><div class="bubble user">${query}</div></div>`;
    chatbox.innerHTML += `<div class="message bot loading"><div class="bubble bot">Loading...</div></div>`;
    chatbox.scrollTop = chatbox.scrollHeight;

    queryInput.value = '';

    try {
        const response = await fetch('/question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        const answer = result.answer;

        const loadingMessage = chatbox.querySelector('.message.bot.loading');
        if (loadingMessage) {
            loadingMessage.remove();
        }

        chatbox.innerHTML += `<div class="message bot"><div class="bubble bot">${answer}</div></div>`;
    } catch (error) {
        console.error('Fetch error:', error);
        chatbox.innerHTML += `<div class="message bot"><div class="bubble bot">Error fetching response</div></div>`;
    }

    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom
}

$(document).ready(function() {
    $('#send-btn').on('click', function() {
        sendQuery();
    });

    $('#chat-input').on('keypress', function(event) {
        if (event.key === 'Enter') {
            sendQuery();
        }
    });
});

