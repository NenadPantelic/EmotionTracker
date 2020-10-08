import React from "react";
import illustration from "./illustration.jpg";

export default function Welcome() {
  return (
    <>
      <div className="welcome">
        <h2 className="welcomeText">Welcome</h2>
        <div className="illustration">
          <img width="100%" src={illustration} alt="illustration" />
        </div>
        <h2 className="enterText">Enter</h2>
      </div>
    </>
  );
}
