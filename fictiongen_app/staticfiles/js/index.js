import React from 'react'
import ReactDOM from 'react-dom'



function Welcome(props) {
  return <h1>Hellowee, {props.name}</h1>;
}

const element = <Welcome name="worlde" />;
ReactDOM.render(
  element,
  document.getElementById('react')
); 


// Settings; to be hooked into room settings / etc but for now can be per session 
const settingsElement = <storySettings roomID="hmm"/>;
const fudge = <h1>Fudge</h1>;

const settingsArea = <inputArea><input class='checkbox' id='grammar-entry' type='checkbox' /><span></span><label>Label Of Thing</label></inputArea>;

ReactDOM.render(
    settingsArea, 
    document.getElementById('settings')
); 
