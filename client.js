
const callMe = () => {
    console.log("me called!");
}

const callMeBack = (callback) => {
    console.log("me call you back!");
    callback("me called back, yes?");
}

var callback = null;

const registerMessageCallback = (cb) => {
    callback = cb;
}

var socket = null;

function connect() {

    const urlParams = new URLSearchParams(window.location.search);
    const userId = urlParams.get('userid');
    const queryString = userId ? `?userId=${userId}` : "";
    let host = window.location.host;
    if (!host || host == null || host == undefined || host == "") {
        host = "localhost:5167";
    }
    
    const url = 'ws://' + host + queryString;
    socket = new WebSocket(url);

    socket.addEventListener('open', function(event) {
        console.log('Websocket opened');
    });

    socket.addEventListener('message', function(event) {
        console.log('Message from server: ' + event.data);
        if (!!callback) {
            callback(event.data);
        }
    });

    socket.addEventListener('close', function(event) {
        console.log('Websocket closed');
    });
}

