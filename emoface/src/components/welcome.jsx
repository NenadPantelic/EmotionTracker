import React from "react";
import {Link} from "react-router-dom";
import illustration from "../illustration.jpg";
import face from "../face.jpg";

export default function Welcome() {
  return (
    <>
      <div className="welcome">
        <h2 className="welcomeText">Emoface</h2>
        <div className="illustration">
        <Link to="/dashboard"><img width="70%" src={face} alt="facial recognition" /></Link>
        </div>
        <p className="message">...Checkout some movie recommendations, based on your mood</p>
        <h2 className="enterText"><Link to="/dashboard">Enter</Link></h2>
      </div>
    </>
  );
}
