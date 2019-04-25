import React, { Component } from 'react';

import { Link, Center , Empid_name, DatePick , Button} from "../../components";
import { Frame, Words } from "@arwes/arwes";
import moment from "moment";


  

  class Splash extends Component {
    constructor(props) {
      super(props);
      this.state = { 
        data: null ,
        dateVal: moment().format('YYYY-MM-DD')
      };
  
     
    } 

    dynamic_name_empid = (date) =>{
      const url = "/dynamic_name_empid";

      fetch(url, {
        method: "post",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      
        //make sure to serialize your JSON body
        body: JSON.stringify({
          date: date
        })
      })
        .then(response => response.json())
        .then(data => this.setState({
          data: data,
        }))
    }


    handleClick(e) {
      e.preventDefault()
      console.log("in csv");

      const url = "/getCsv";

      fetch(url)
        .then(response => response.json())
        // .then(data => this.setState({
        //   data: data,
        // }))
    }

  componentWillMount(){
  //  this.dynamic_name_empid(this.state.dateVal)
  }

  handleDateValChange = (DateVal) => {
    this.setState({dateVal: DateVal});
}



  render() {
    // console.log(this.state)
    const {data} = this.state;
    
    return (
    <Center>

         <Link to="/register">
          <Button>Register Employee</Button>
        </Link>

      <br/>
        <Link to="/allemp">
          <Button>All Employees</Button>
        </Link>

        <br/>

        {/* <Button onClick={e => this.handleClick(e)}>Get CSV</Button>
        <br/> */}
      <h1 >
        Complete Employee List on 
      </h1>

      <DatePick onDateSelect = {this.handleDateValChange} netWorkCall = {this.dynamic_name_empid}/>
        

     <div className="emp_id_name_container"
     style={{  padding: 20 , width: "100%"}}>
     {data ? (
        data.map((element, k) => {
          return (
          <Link to={`detail/${element["EMP_ID"]}/${element["NAME"]}`} key={k}>
            <Empid_name emp_id={element["EMP_ID"]} emp_name={element["NAME"]} key={k}/>
          </Link>)

        })    ) : (
          <h1 >
           .
        </h1>
      )}

      {data && data["length"] ? null : <Center> <h1 > All Absent on this day </h1> </Center>
        //data && this.state.data.length() && <h1 > Complete Employee List on </h1>
      }
     </div>

    </Center>
  )
  }
}
export default Splash;
