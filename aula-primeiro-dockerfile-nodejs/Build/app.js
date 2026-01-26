const http = require("http");

const hostname = "0.0.0.0";
const port = process.env.PORT;
const version = process.env.VERSION;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Ola Mundo");
});

server.listen(port, hostname, () => {
  console.log(
    `Server running at http://${hostname}:${port}/ \n version ${version}`,
  );
});

process.on("SIGINT", () => {
  process.exit();
});
