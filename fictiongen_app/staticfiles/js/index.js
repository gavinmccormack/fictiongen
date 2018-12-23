import React from 'react'
import ReactDOM from 'react-dom'

var data = require('./data.js');

console.log(data);
// Settings; to be hooked into room settings / etc but for now can be per session 
const settingsArea = <inputArea><input class='checkbox' id='grammar-entry' type='checkbox' /><span></span><label>Label Of Thing</label></inputArea>;

ReactDOM.render(
    settingsArea, 
    document.getElementById('settings')
); 

class StoryPanel extends React.Component {
    constructor(props){
        super(props)
    }

    render(){
        this.update();
        return (<h1>basic render enabled</h1>);
    }

    update(){
        console.log(data);
        storyData = data.getUpdatedStory();
        console.log(storyData);
    }
}

ReactDOM.render(
    <StoryPanel />,
    document.getElementById('story')
);
