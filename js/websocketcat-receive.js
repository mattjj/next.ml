var socket = io.connect('http://localhost');
// var socket = io.connect('http://willsky-student7.lids.mit.edu');
var received;
socket.on('data', function (data) {
    received = JSON.parse(data);
});
