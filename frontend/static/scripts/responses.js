function getBotResponse(input) {
    if (input == "hello") {
        addBotMessage("Hello There")
        //return "Hello there!";
    } else if (input == "goodbye") {
        addBotMessage("Talk to you later");
        //return "Talk to you later!";
    } else {

        if (input.toLowerCase().includes('open')) {
            addBotMessage("Opening");
            eel.get_result(input)
        } else if (input.toLowerCase().includes('add')) {
            addBotMessage("Please enter the details in console");
            eel.get_result(input)
        } else {
            addBotMessage("Redirecting")
            eel.get_result(input);
        }
    }
}

// Retrieves the response
function getHardResponse(userText) {

    getBotResponse(userText);
}