var app = require('http').createServer(handler),
    io = require('socket.io').listen(app),
    fs = require('fs'),
    rl = require('readline'),
    url = require('url'),
    path = require('path');

// process.stdin.resume(); // needed if not using readline
process.stdin.setEncoding('ascii');
app.listen(3000);

var mimeTypes = {
    "html": "text/html",
    "js": "text/javascript",
    "css": "text/css"
};

function handler (req, res) {
    var uri = url.parse(req.url).pathname;
    var filename = path.join(process.cwd(), uri);
    fs.readFile(filename, function (err,data) {
        if (err) {
            res.writeHead(500);
            console.log(uri);
            console.log(filename);
            return res.end('Error');
        }
        var mimeType = mimeTypes[path.extname(filename).split('.')[1]];
        res.writeHead(200, {'Content-Type':mimeType});
        res.end(data);
    });
}

io.sockets.on('connection', function (socket) {
    rl.createInterface(process.stdin, fs.createWriteStream('/dev/null'), null)
        .on('line',function(chunk) {
            if (chunk.length > 0) { socket.emit('data',chunk.toString()); }
        });
});
