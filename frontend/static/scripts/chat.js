function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    let time = hours + ":" + minutes;

    return time;
}

function firstBotMessage() {
    let firstMessage = "Present at your service";
    document.getElementById("botStarterMessage").innerHTML = 
        '<p class="botText"><span>' + firstMessage + '<span></p>';
    
    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();


function getResponse() {
    let userText = $("#textInput").val();
    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    if (userText == "") {
        addBotMessage("Please Enter Some Input");
    }

    else {
        $("#textInput").val("");
        $("#chatbox").append(userHtml);
        document.getElementById("chat-bar-bottom").scrollIntoView(true);

        getHardResponse(userText);
        
        document.getElementById("chat-bar-bottom").scrollIntoView(true);
    }
}

function addBotMessage(sampleText) {
    let botHtml = '<p class="botText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    setTimeout(() => {
        responsiveVoice.speak(sampleText, "Hindi Female");
        $("#chatbox").append(botHtml);
    }, 1000)
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function addUserMessage(sampleText) {
    let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

function sendButton() {
    getResponse();
}

/*let p = new Promise((resolve, reject) => {

});*/

var result = '';

function listen() {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.interimResults = true;

    var temp = ''
    result = ''

    recognition.onresult = function(event) {
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                result += event.results[i][0].transcript;
              } else {
                temp += event.results[i][0].transcript;
              }
        }
    }

    recognition.onend = function(event) {
        //alert(result)
    }

    recognition.start();
}

function micButton() {
    listen();

    setTimeout(() => {
        let output = result;
        //alert(output);
        addUserMessage(output);
        getBotResponse(output);
    }, 10000);

}

// Press Enter to send a message
$("#textInput").keypress(function(e) {
    if (e.which == 13) {
        getResponse();
    }
});