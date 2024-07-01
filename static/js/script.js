function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput === "") return;

    const chatLog = document.getElementById("chatlog");
    const userMessage = document.createElement("div");
    userMessage.textContent = "Vous : " + userInput;
    chatLog.appendChild(userMessage);

    fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("div");
        botMessage.textContent = "Bot : " + data.response;
        chatLog.appendChild(botMessage);
    });

    document.getElementById("user-input").value = "";
}
