import React from "react";
import { Frame} from "@arwes/arwes";
import AnimateContext from "../helpers/animateContext";

export default ({ ...props}) => {
  return (
    
    <div className="emp_list"
      style={{ padding: 20 , width: "100%"}}
      >
        <Frame animate level={1} corners={3}>
          
          <div style={{ padding: '8px 8px', fontSize: '22px' }}>
          <h1 style={{margin: "0 0 -1px"}}>
            Employee Id : {props.emp_id}
          </h1>

          {props.emp_name}
          
          </div>
        </Frame>
        </div>

        
      

  );
};
