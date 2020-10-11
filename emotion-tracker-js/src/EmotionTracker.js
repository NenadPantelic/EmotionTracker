import apiUrl from "../config.js"
const axios = require('axios').default;

export default class EmotionTracker {

    constructor(callbackOnChange, url = apiUrl) {
        this.state = {
            "emotion" : {},
            "dominant_emotion" : "none"
        }

        this.generateProxyHandler = (callback) => {
            return (target, key, value) => {
                callback(key, value, target);
                return true;
            }
        }

        this.erEngineUrl = url
        this.proxyHandler = {
            set: this.generateProxyHandler(callbackOnChange)
        }

        this.axiosInstance = axios.create({
            baseURL: this.erEngineUrl,
            timeout: 300000,
            headers: {'X-Custom-Header': 'EmotionRecognition'}
        });
    }
 
    track() {
        this.state = new Proxy(this.state, this.proxyHandler);
        return this.state
    }

    async poll(imageFile) {

        let res = await this.axiosInstance.post("", imageFile, {
            headers: {
                'Content-Type' : "image"
            }
        })
        
        this.state.emotion = res.data.emotion;
        this.state.dominant_emotion = res.data.dominant_emotion;
        
        return this.state;
    }

}