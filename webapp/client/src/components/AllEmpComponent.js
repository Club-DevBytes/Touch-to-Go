import React from "react";
import AnimateContext from "../helpers/animateContext";
import { Frame, Words, Image } from "@arwes/arwes";

export default ({ ...props}) => {

 
  return (
    
  
      <div className="emp_list"
      style={{ padding: 20 , width: "100%"}}
      >
        <Frame animate level={1} corners={3}>
          
        <div className="container" style={{display: "flex", justifyContent: "space-between"}}>

        <div style={{ padding: '8px 8px', fontSize: '22px' }}>
              <h1 style={{margin: "0 0 -1px"}}>

            EMP ID: {props.emp_id}
              </h1>
      
              <br/>

              <br/>

            Name: {props.name}
            
             
          
          </div>

         </div> 
       

        </Frame>
        </div>
     


        
      

  );
};
