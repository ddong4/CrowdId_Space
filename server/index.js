const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');
const config = require('./config/config.json');
const app = express();

app.use(express.json());

app.use(
  cors({
    origin: '*'
  })
);
const db = require('./models');

// Routers

// TODO:

/**
 * Routes for Nearby Objects
 */

console.log(
  `Server running at http://${config.development.server_host}:${config.development.server_port}`
);

module.exports = app;
