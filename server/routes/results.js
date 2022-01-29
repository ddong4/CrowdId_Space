const express = require('express');
const mysql = require('mysql2');
const config = require('../config/config.json');
const router = express.Router();

// TODO: set up mysql database
const connection = mysql.createConnection({
  host: config.development.host,
  user: config.development.username,
  password: config.development.password,
  port: config.development.rds_port,
  database: config.development.database
});
connection.connect();

/**
 * Result Object Nearby Routes
 */
async function result(req, res) {
  // TODO: Angela implement and return json of results
  // I will give the data as a string req="-80,-80"
}

module.exports = {
  result
};
