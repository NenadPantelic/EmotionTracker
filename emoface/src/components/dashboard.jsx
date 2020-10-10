import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div clasName="dashboard">
      <h2>Place your face in the Camera to begin!</h2>
      <div className="webcam">
        <video
          
          src="https://www.youtube.com/watch?v=rZNDsiW7wpk"
          id="video"
          width="720"
          height="560"
          controls
        />{" "}
      </div>

      <div className="link-wrapper">
        <Link to="/">{"<< Home"}</Link>
        <Link to="/search">{"Test out the API >>"}</Link>
      </div>
    </div>
  );
}
