import React, { Component } from "react";

import { Input, Button, SnackComp } from "../../components";
import { Frame, Words } from "@arwes/arwes";




class Register extends Component {

    state = { snackState: false};

    insert_emp_id_name = (emp_id, name) =>{
        const url = "/insert_emp_id_name";
  
        fetch(url, {
          method: "post",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        
          //make sure to serialize your JSON body
          body: JSON.stringify({
            emp_id: emp_id,
            name: name
          })
        })
        //   .then(response => console.log(response.json()))
        //   .then(data => console.log(data))
        return 1;
      } 

      show_hide_snack = () =>{

        this.setState({
          snackState: true
        })

        setTimeout(
          function() {
            this.setState({
              snackState: false
            })
          }
          .bind(this),
          2000
      );
      }

  render() {
    return (
     
    
    <div>

    <div style={{ maxWidth: "540px" }}>
       
       <form
         onSubmit={e => {
           e.preventDefault();
           // login(this.state.email);

           this.state.emp_id && this.state.name && this.insert_emp_id_name(this.state.emp_id, this.state.name) && this.show_hide_snack()
         }}
       >
         <div>
           <label>Employee id: </label>
           <Input
             type="number"
             onChange={e => this.setState({ emp_id: e.target.value })}
           />
         </div>
         <div>
           <label>Employee name: </label>
           <Input type="text" 
           onChange={e => this.setState({ name: e.target.value })}
           />
         </div>
         
         <div>
           <Button type="submit">
             {"Register"}
           </Button>
         </div>
       </form>
    </div>


   <div style={{
       position:"fixed",
        left:"0",
        right:"0",
        bottom:"30%",
        height:"30px",
        margin: "auto",
        width: "80%" }}> 
        
        
        {this.state.snackState && <SnackComp/>}
        
   </div>


    </div>
    
    );
  }
}
export default Register;
