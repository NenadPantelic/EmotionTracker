import React from 'react'

export default function Search() {
    const isOn = true
    return (
        <div>
            <h2>Welcome to EmoFace, Place your face in the Camera to begin!</h2>
            <form>
                <input style={{"width": "50%", "height" : "35px"}} type="text" name="url" id="url" placeholder="Enter Url Here"/>
                <select style={{"width": "20%", "height" : "42px"}}>
                    <option>Option 1</option>
                    <option>Option 1</option>
                </select>
                <input style={{"width": "10%", "height" : "42px"}} type="submit" value="Search" />
            </form>
            
        </div>
    )
}
