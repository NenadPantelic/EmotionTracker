import React, { useEffect } from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const handleCapture = () => {
    console.log("Hello there");
    document.getElementById("canvas").style.display = "inherit";
  };

  async function init(obj) {
    try {
      const stream = await navigator.mediaDevices.getUserMedia(obj);
      document.getElementById("video").srcObject = stream;
    } catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    const constraint = {
      video: {
        width: {
          min: 560,
          max: 1280,
          ideal: 1280,
        },
        height: {
          min: 340,
          max: 720,
          ideal: 720,
        },
      },
    };

    init(constraint)
      .then((res) => {
        console.log("successful");
      })
      .catch((err) => {
        console.log("there was an error");
      });
      
  }, []);

  return (
    <div clasName="dashboard">
      <h2>Place your face in the Camera to begin!</h2>
      <div className="webcam">
        <video id="video" autoPlay />
      </div>
      <div>
        <button onClick={handleCapture} id="capture">
          Capture
        </button>
      </div>
      <canvas
        style={{ display: "none" }}
        id="canvas"
        width="540"
        height="320"
      ></canvas>
      <div className="link-wrapper">
        <Link to="/">{"<< Home"}</Link>
        <Link to="/search">{"Test out the API >>"}</Link>
      </div>
      <div id="err-msg"></div>
    </div>
  );
}
