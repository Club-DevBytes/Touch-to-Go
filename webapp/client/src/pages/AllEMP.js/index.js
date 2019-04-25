import React, { Component } from 'react';

import { Link, Center , Empid_name, AllEmpComponent } from "../../components";
import { Frame, Words, Image } from "@arwes/arwes";




  class AllEMP extends Component {
    constructor(props) {
      super(props);
      this.state = { data: null };
  
      
    } 

    // attnd_tbl_frm_empid = (emp_id) =>{
    //   const url = "/attnd_tbl_frm_empid";

    //   fetch(url, {
    //     method: "post",
    //     headers: {
    //       'Accept': 'application/json',
    //       'Content-Type': 'application/json'
    //     },
      
    //     //make sure to serialize your JSON body
    //     body: JSON.stringify({
    //       emp_id: emp_id
    //     })
    //   })
    //     .then(response => response.json())
    //     .then(data => this.setState({
    //       data: data
    //     }))
    // } 
  componentWillMount(){
    
    const url = "/get_reg_emps";

    fetch(url)
      .then(response => response.json())
      .then(data => this.setState({
          data: data,
        }))
  //  this.attnd_tbl_frm_empid(this.props.empid)
  }

  render() {
    console.log(this.state)
    const {data} = this.state;
    return (
    <Center>
    
    <h1 >
        Details of All Employee Id
      </h1>


        <div className="emp_details_container"
     style={{  padding: 20 , width: "100%"}}>
     {data ? (
        data.map((element, k) => {

          
          return (
            <Link to={`personal/${element["EMP_ID"]}/${element["NAME"]}`} key={k}>

            <AllEmpComponent name={element["NAME"]} emp_id={element["EMP_ID"]}
            key={k} 
            
            />
            </Link>
            )

        })    ) : (
          <h1 >
            No Data on This Date
        </h1>
      )}
     </div>
     

    </Center>
  )
  }
}
export default AllEMP;
