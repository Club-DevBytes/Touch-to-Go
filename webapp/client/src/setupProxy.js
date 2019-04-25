const proxy = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(proxy('/all_attend_tbl', { target: 'http://localhost:3008/' }));
  app.use(proxy('/attend_name_empid', { target: 'http://localhost:3008/' }));
  app.use(proxy('/dynamic_name_empid', { target: 'http://localhost:3008/' }));
  app.use(proxy('/insert_emp_id_name', { target: 'http://localhost:3008/' }));

  app.use(proxy('/get_reg_emps', { target: 'http://localhost:3008/' }));

  
};