"use strict";

const { setItem, getItem } = require("./storage");

function handleRequest(req, res) {
  if (req.url === "/status") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ ok: true }));
    return;
  }

  if (req.url.startsWith("/item/") && req.method === "GET") {
    const key = req.url.split("/").pop();
    const value = getItem(key);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ key, value }));
    return;
  }

  if (req.url.startsWith("/item/") && req.method === "POST") {
    const key = req.url.split("/").pop();
    let body = "";
    req.on("data", (chunk) => { body += chunk; });
    req.on("end", () => {
      setItem(key, body.trim());
      res.writeHead(201, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ key }));
    });
    return;
  }

  res.writeHead(404);
  res.end();
}

module.exports = { handleRequest };
