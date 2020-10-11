# emotion-tracker-js

A js wrapper for our Emotion Recognition engine. Gives developers easy access to the user's emotion.

## Docs

### How to use

It all revolves around the `EmotionTracker` class. 

First install this library

```bash
npm install 'emotion-tracker-js'
```

Import and initialize our tracker!

```javascript
import EmotionTracker from 'emotion-tracker-js'

let emotionUpdateCallback = () => {}

let emotionTracker = new EmotionTracker(emotionUpdateCallback)
emotionTracker.track()
// You need to take the pictures and establish the connection with the webcam and use that
// ... Webcam code that takes picture
let emotion = emotionTracker.poll(imageFile)
// As soon as the api request is resolved, the callback you specified will be called '
// and you will have access to the newest emotion state of the user. You can use the variable emotion as well.
```

### Callbacks and State Management

Our module makes use of javascript proxies thanks to which the user will be notified each time the user's emotion changes.
Developers can easily abstract their functionality into a callback which accepts the following arguments

```javascript
function myCallback(key, value, target) {
    // do whatever you want with these
}
```

The callback is invoked with the parameters of the property that is changed in the emotion state object as well as the value it is taking and the previous state value.
