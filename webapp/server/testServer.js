const express = require('express');
const bodyParser = require('body-parser');
const mysql      = require('mysql');
// https://github.com/mysqljs/mysql
// const connection = mysql.createConnection({
//   host     : '127.0.0.1',
//   user     : 'root',
//   password : 'root',
//   database : 'COMPANY'
// });

const connection = mysql.createConnection({
  host     : '192.168.43.190',
  user     : 'root',
  password : 'password',
  database : 'COMPANY'
});


// Initialize the app
const app = express();
//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/all_attend_tbl', function (req, res) {

    connection.query('SELECT * FROM ATTENDENCE', function (error, results, fields) {
      if (error) throw error;
      res.send(results)
    });

});

app.get('/attend_name_empid', function (req, res) {

  connection.query('SELECT DISTINCT ATTENDENCE.EMP_ID, EMP_DETAILS.NAME FROM EMP_DETAILS, ATTENDENCE WHERE EMP_DETAILS.EMP_ID = ATTENDENCE.EMP_ID',
   function (error, results, fields) {
    if (error) throw error;
    res.send(results)
  });

});


app.post('/dynamic_name_empid', function (req, res) {
  const date = req.body.date;
  connection.query(`SELECT DISTINCT ATTENDENCE.EMP_ID, EMP_DETAILS.NAME FROM EMP_DETAILS, ATTENDENCE WHERE EMP_DETAILS.EMP_ID = ATTENDENCE.EMP_ID AND DATE="${date}"`,
   function (error, results, fields) {
    if (error) throw error;
    // console.log(results)
    res.send(results)
  });

});


app.post('/get_name_server', function (req, res) {
  const emp_id = req.body.emp_id;
  connection.query(`SELECT NAME FROM EMP_DETAILS WHERE EMP_ID="${emp_id}"`,
   function (error, results, fields) {
    if (error) throw error;
    // console.log(results)
    res.send(results)
  });

});

app.post('/attnd_tbl_frm_empid', function (req, res) {
  const emp_id = req.body.emp_id;
  connection.query(`SELECT * FROM ATTENDENCE WHERE EMP_ID="${emp_id}"`,
   function (error, results, fields) {
    if (error) throw error;
    // console.log(results)
    res.send(results)
  });

});


app.post('/insert_emp_id_name', function (req, res) {
  const emp_id = req.body.emp_id;
  const name = req.body.name;

  connection.query(`INSERT INTO EMP_DETAILS VALUES ("${emp_id}","${name}")`,
   function (error, results, fields) {
    if (error) throw error;
    // console.log(results)
    // res.send(results)
    console.log("1 record inserted");
    console.log(results)

  });

});

connection.query('SELECT * FROM ATTENDENCE', function (error, results, fields) {
  if (error) throw error;
  console.log(results)
});


// Start the server
app.listen(3000, () => {
 console.log('Go to http://localhost:3000/data to see posts');
});