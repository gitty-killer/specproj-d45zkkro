"use strict";

const items = new Map();

function setItem(key, value) {
  items.set(key, value);
}

function getItem(key) {
  return items.get(key) || null;
}

module.exports = { setItem, getItem };
