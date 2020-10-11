const { default: Axios } = require("axios")
const apiUrl = require("../config.js")

export default class EmotionTracker {

    state = {
        "emotion" : {},
        "dominant_emotion" : "none"
    }
    
    proxyHandler = null
    erEngineUrl = apiUrl

    constructor(callbackOnChange) {
        this.proxyHandler = {
            set: this.generateProxyHandler(callbackOnChange)
        }
    }
   
    generateProxyHandler = (callback) => {
        return (target, key, value) => {
            callback(key, value, target);
            return true;
        }
    }
 
    track() {
        return new Proxy(this.state, this.proxyHandler);
    }

    async poll(imageFile) {

        let res = await Axios.post(this.erEngineUrl, imageFile, {
            headers: {
                'Content-Type' : imageFile.type
            }
        })

        this.state.emotion = res.data.emotion;
        this.state.dominant_emotion = res.data.dominant_emotion;
        console.log(this.state);

        return this.state;
    }

}