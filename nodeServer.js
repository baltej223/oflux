var http = require('http');
var url = require('url');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/HTML'});
  res.write("<H1>DEPRICATED</H2>");
  res.end();
}).listen(8080);