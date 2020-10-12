import React, { useState } from "react";
import axios from "axios";
import Webcam from "react-webcam";
import EmotionTracker from "emotion-tracker-js";
import { Card } from "antd";
const { Meta } = Card;

const suggestedVideoData = [
  {
    actors:
      "Ron Moody, Mike Reid, Miles Petit, Danny Ogle, Jason Gerard, Helena Roman, Matthew Hendrickson, Spyros Merianos, Abbie Balchin, Rachel Balchin, Jason Bullet, Ernesto Cantu, Andy Cheeseman, Emily Corcoran, Lynette Creane",
    description:
      "Getaway driver Miles Foster is placed in witness protection after the murder of his friend Andres by Astin Brody, a shady underworld boss. Miles is hidden on the Greek Island of Zanthi with...",
    directors: "Danny Patrick",
    duration: 90,
    genre_name: "Adventure",
    imdb_url: "https://www.imdb.com/title/tt0451130/",
    movie_id: "tt0451130",
    poster_url:
      "https://m.media-amazon.com/images/M/MV5BOTUwMmI1MWEtYzRkNy00NjBkLTllM2YtZmNkNmVjODI1M2Q2XkEyXkFqcGdeQXVyMzA2ODY0NA@@.jpg",
    production_company: "Empire Productions",
    score: 9.3,
    title: "Moussaka & Chips",
    year: 2005,
  },
  {
    actors:
      "Bryan Cranston, Arun Govil, Edie Mirman, Rael Padamsee, Namrata Sawhney, James Earl Jones, Shatrughan Sinha, Jinder Walia, Amrish Puri, Mishal Varma, Tom Wyner, Richard Cansino, Shakti Singh, Dilip Sinha, Michael Sorich",
    description:
      "An anime adaptation of the Hindu epic the Ramayana, where Lord Ram combats the wicked king Ravana.",
    directors: "Ram Mohan, Yûgô Sakô",
    duration: 170,
    genre_name: "Adventure",
    imdb_url: "https://www.imdb.com/title/tt0259534/",
    movie_id: "tt0259534",
    poster_url:
      "https://m.media-amazon.com/images/M/MV5BOTk4NGM0NmUtOTc2Yi00NTcxLWE3NGItYzEwODZjNzlhZjE2XkEyXkFqcGdeQXVyNTgyNTA4MjM@.jpg",
    production_company: "Nippon Ramayana Film Co.",
    score: 9,
    title: "Ramayana: The Legend",
    year: 1992,
  },
];

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user",
};

// Utility function
function dataURLtoFile(dataurl, filename) {
  let arr = dataurl.split(","),
    mime = arr[0].match(/:(.*?);/)[1],
    bstr = atob(arr[1]),
    n = bstr.length,
    u8arr = new Uint8Array(n);

  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new File([u8arr], filename, { type: mime });
}

function RenderSuggestedVideo(props) {
  const { poster_url, year, title, description, genre_name, duration } = {
    ...props,
  };
  return (
    
    <Card
      hoverable
      style={{ width: 240 }}
      cover={<img alt="example" src={poster_url} height= "230px"/>}
    >
      {/* <Meta title={title} description={description} /> */}
      <h2> {title}</h2>
      <div style={{ paddingTop: "2rem", textAlign: "left" }}>
        <p> {description}</p>
        <p> Genre: {genre_name}</p>
        <p> Duration: {duration}</p>
        <p> Year: {year}</p>
      </div>
    </Card>
    
  );
}

export default function WebcamCapture() {
  const webcamRef = React.useRef(null);
  const [isSuggestedVideos, setIsSuggestedVideos] = useState(false);
  const [suggestedVideos, setSuggestedVideos] = useState(suggestedVideoData);
  let emotionTracker;

  // function that will be called as soon as the user's emotion changes!
  const emotionCallback = async (key, value, target) => {
    console.log(key, value, target);
    if (key === "dominant_emotion") {
      setIsSuggestedVideos(true);
      let res = await axios.post(
        "fortress88.servebeer.com:8000/api/v1/recommend",
        {
          emotion: value.charAt(0).toUpperCase() + value.slice(1),
          num_of_movies: 5,
          recommendation_type: "improve",
        }
      );
      console.log("The value of res is:", res);
      setSuggestedVideos(res.movies);
    }
  };

  React.useEffect(() => {
    emotionTracker = new EmotionTracker(emotionCallback);
    // Enable the proxy subscription for the emotion Callback
    emotionTracker.track();
  }, []);

  const capture = React.useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    // Important to convert the screenshot to a binary file.
    let binaryImage = dataURLtoFile(imageSrc);
    // Request a state change! Will fire the callback you wrote if the state has been changed!
    emotionTracker.poll(binaryImage);
  }, [webcamRef]);

  return (
    <>
      {!isSuggestedVideos && (
        <div style={{display: "flex", flexDirection: "column", alignItems:"center"}}>
          <h1>Place your face in the camera and capture an image!</h1>
          <Webcam
            audio={false}
            height={400}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            width={720}
            videoConstraints={videoConstraints}
          />{" "}
          <button style={{marginTop:"2rem"}} onClick={capture}>Capture photo</button>
        </div>
      )}
      <div style={{ display: "flex", width: "60%", margin: "auto" }}>
        {isSuggestedVideos &&
          suggestedVideos.map((item) => <RenderSuggestedVideo {...item} />)}
      </div>
    </>
  );
}
