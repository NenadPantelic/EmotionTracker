import React from 'react';
import Webcam from 'react-webcam'
import EmotionTracker from 'emotion-tracker-js'

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

// Utility function
function dataURLtoFile(dataurl, filename) {
  let arr = dataurl.split(','), 
  mime = arr[0].match(/:(.*?);/)[1], 
  bstr = atob(arr[1]), 
  n = bstr.length, 
  u8arr = new Uint8Array(n);

  while(n--){
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new File([u8arr], filename, { type : mime });
}

export const WebcamCapture = () => {
    const webcamRef = React.useRef(null);
    let emotionTracker;

    // function that will be called as soon as the user's emotion changes!
    const emotionCallback = (key, value, target) => console.log(key, value, target)

    React.useEffect(() => {
      // Initialize on component mount
      emotionTracker = new EmotionTracker(emotionCallback);
      // Enable the proxy subscription for the emotion Callback
      emotionTracker.track();
    }, [])

    const capture = React.useCallback(
      () => {
        const imageSrc = webcamRef.current.getScreenshot();
        // Important to convert the screenshot to a binary file.
        let binaryImage = dataURLtoFile(imageSrc)
        // Request a state change! Will fire the callback you wrote if the state has been changed!
        emotionTracker.poll(binaryImage);
      },[webcamRef]
    );

    return (
      <>
        <Webcam
          audio={false}
          height={720}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={1280}
          videoConstraints={videoConstraints}
        />
        <button onClick={capture}>Capture photo</button>
      </>
    );
};