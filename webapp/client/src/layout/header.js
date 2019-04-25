import React from "react";
import {Link, Button} from "../components";
import { Header } from "@arwes/arwes";
import Logo from "../assets/img/logo.png";
import AnimateContext from "../helpers/animateContext";

const TopHeader = () => (
  <AnimateContext.Consumer>
    {({ show }) => (
      <Header
        animate
        show={show}
        style={{
          marginBottom: "1.45rem"
        }}
      >
        
        <div>

        <div
          style={{
            margin: "0 auto",
            maxWidth: "100%",
            padding: "0.5rem 1.0875rem",
            display: "flex",
            justifyContent: "space-between"
          }}
          >
          <Link
            to="/"
            style={{
              color: "white",
              textDecoration: "none"
            }}
          >
            <img  src={Logo} style={{maxWidth: "200px", maxHeight: "30px"}} alt="logo"/>

          </Link>
          
          <h3 >
          Gujarat Industrial Hackathon
          </h3>

          <h3>
          Team ID: TG001631
          </h3>

        </div>

        </div>
      </Header>
    )}
  </AnimateContext.Consumer>
);

export default TopHeader;
