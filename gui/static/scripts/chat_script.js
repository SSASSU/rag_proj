async function sendQuery() {
    const queryInput = document.getElementById('chat-input');
    const query = queryInput.value;

    if (query.trim() === '') return;

    const chatbox = document.getElementById('chat-box');
    chatbox.innerHTML += `<div class="message user"><div class="bubble user">${convertTextToHtml(query)}</div></div>`;
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

        chatbox.innerHTML += `<div class="message bot"><div class="bubble bot">${convertTextToHtml(answer)}</div></div>`;
    } catch (error) {
        console.error('Fetch error:', error);
        chatbox.innerHTML += `<div class="message bot"><div class="bubble bot">Error fetching response</div></div>`;
    }

    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom
}

function convertTextToHtml(text) {
    // HTML 특수 문자 이스케이프
    let escapedText = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");

    // 줄바꿈을 <br>로 변환
    escapedText = escapedText.replace(/\n/g, "<br>");

    // 여러 공백을 &nbsp;로 변환
    escapedText = escapedText.replace(/ /g, "&nbsp;");

    return escapedText;
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
