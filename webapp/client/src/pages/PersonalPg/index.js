import React, { Component } from 'react';

import { Link, Center , Empid_name, Emp_detail_comp } from "../../components";
import { Frame, Words, Image } from "@arwes/arwes";




  class PersonalPg extends Component {
    constructor(props) {
      super(props);
      this.state = { data: null };
  
      
    } 

    star_employ = (emp_id) =>{
      const url = "/star_employ";

      fetch(url, {
        method: "post",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      
        //make sure to serialize your JSON body
        body: JSON.stringify({
          emp_id: emp_id
        })
      })
        .then(response => response.json())
        .then(data => this.setState({
          data: data
        }))
    } 
  componentWillMount(){
    
    // const url = "/attend_name_empid";

    // fetch(url)
    //   .then(response => response.json())
    //   .then(data => this.setState({
    //     data: data,
    //   }))

//    this.attnd_tbl_frm_empid(this.props.empid)

// console.log(this.props.empid)

   this.star_employ(this.props.empid)


  }

  render() {
    console.log(this.state)
    const {data} = this.state;
    return (
    <Center>
    
    <h1 >
        Personalized details  Employee Id : {this.props.empid} {this.props.name}
      </h1>


        <div className="emp_details_container"
     style={{  padding: 20 , width: "100%"}}>
     {data ? (
        data.map((element, k) => {

          
          return (
            
            <Emp_detail_comp name={this.props.name} empid={this.props.empid} 
            key={k} 
            date={element["DATE"]}
            IN_TIME={element["IN_TIME"]}
            OUT_TIME={element["OUT_TIME"]}

            />
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
export default PersonalPg;
