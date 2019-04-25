import React from "react";
import { Router } from "@reach/router";
import Splash from "./pages/splash";
import EmpDetail from "./pages/EmpDetail";
import Register from "./pages/Register";
import AllEMP from "./pages/AllEMP.js"

import PersonalPg from "./pages/PersonalPg"



const NotFound = () => <div>Sorry, nothing here.</div>;

const Routes = () => {
  return (
    <Router>
      <Splash path="/" />
      <EmpDetail path="detail/:empid/:name"/>
      <Register path="register"/>
      <AllEMP path="allemp"/>

      <PersonalPg path="personal/:empid/:name"/>
      <NotFound default />
    </Router>
  );
};
export default Routes;
