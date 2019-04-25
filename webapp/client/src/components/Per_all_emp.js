import React from "react";
import AnimateContext from "../helpers/animateContext";
import { Frame, Words, Image } from "@arwes/arwes";

export default ({ ...props}) => {

  const error_prop = {
    error: 'NO IMAGE',
  };
  return (
    
  
     

      <div className="emp_list"
      style={{ padding: 20 , width: "100%"}}
      >
        <Frame animate level={1} corners={3}>
          
        <div className="container" style={{display: "flex", justifyContent: "space-between"}}>

        <div style={{ padding: '8px 8px', fontSize: '22px' }}>
              <h1 style={{margin: "0 0 -1px"}}>

              {props.date}

              </h1>
      
              <br/>

              <br/>

            IN Time: {props.IN_TIME}
            
              <br/>

            OUT Time: {props.OUT_TIME}
          
          </div>

     

          <div style={{ padding: "10px 20px 0px 0px", maxWidth: "200px" }}>
          <Image animate resources={props.IN_PIC} i18n={error_prop}> IN_PIC</Image>

        </div>

        <div style={{ padding: "10px 20px 0px 0px", maxWidth: "200px" }}>
          <Image animate resources={props.OUT_PIC} i18n={error_prop}> OUT_PIC</Image> 
            

        </div>
         </div> 
       

        </Frame>
        </div>
     


        
      

  );
};
