"use strict";

const http = require("http");
const { handleRequest } = require("./router");

const server = http.createServer(handleRequest);
server.listen(3000, () => {
  console.log("listening on 3000");
});
