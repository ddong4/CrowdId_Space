const express = require('express');
const mysql = require('mysql2');
const config = require('../config/config.json');
const router = express.Router();

// TODO: set up mysql database
// const connection = mysql.createConnection({
//   host: config.development.host,
//   user: config.development.username,
//   password: config.development.password,
//   port: config.development.rds_port,
//   database: config.development.database
// });
// connection.connect();

/**
 * Result Object Nearby Routes
 */
async function result(req, res) {
  // TODO: Angela implement and return json of results
  // I will give the data as a string req="-80,-80"
 //read json
 let response = await fetch('/server/test_data/star_data_yes.json');
 let user = await response.json(); 
 //call helper function
  ret = parseReq(req); 
//res.json()
  res = user; 
  //return results
  return res;  
}

//parse the req and return true 
function parseReq(req) {
  
  //sep by comma
  const coordinate = req.split(',');
  //test
  let latitude = word[0]; 
  //console.log(word[0]); 
  let longitude = word[1]; 
  //console.log(word[1]);

  //if found in star_data_yes, return true
  //var latitude = await User.
  if (latitude && longitude) {
      let y = new Boolean(true);
      return y;
  } 
  if (!latitude || !longitude) {
      let x = new Boolean(false);
      return x; 
  }
  //if found in star_data_no

}

module.exports = {
  result
};
