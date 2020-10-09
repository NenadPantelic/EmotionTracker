import React from "react";
import {Link} from "react-router-dom";
import illustration from "./illustration.jpg";

export default function Welcome() {
  return (
    <>
      <div className="welcome">
        <h2 className="welcomeText">Welcome</h2>
        <div className="illustration">
        <Link to="/dashboard"><img width="100%" src={illustration} alt="illustration" /></Link>
        </div>
        <p className="message">...Checkout some movie recommendations, based on your mood</p>
        <h2 className="enterText"><Link to="/dashboard">Enter</Link></h2>
      </div>
    </>
  );
}
