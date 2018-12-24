import React from 'react'
import ReactDOM from 'react-dom'

const DataInterface = require('./data.js');
var data = new DataInterface;
// Settings; to be hooked into room settings / etc but for now can be per session 
const settingsArea = <h1></h1>//<inputArea><input class='checkbox' id='grammar-entry' type='checkbox' /><span></span><label>Label Of Thing</label></inputArea>;

ReactDOM.render(
    settingsArea, 
    document.getElementById('settings')
); 

class StoryPanel extends React.Component {
    constructor(props){
        super(props)
        this.storyLines = ["Some placeholder", "text until", "later"]; // Array of strings
    }

    render(){
        // A div wrapper with an element wrapper for each line of text. 
        // These will have element ID's and other information, but this is a basic outline
        var storyData = this.update();
        const lineFormat = <p class="mk-line">{content}</p>;
        var lines = this.storyLines.map((line) => { return <span class="mk-line">{line} </span>;});
        console.log(lines);
        return (<div class="story-content"><p>{lines}</p></div>);
    }

    update(){
        var storyData = data.getUpdatedStory();
        return storyData; 
    }
}

ReactDOM.render(
    <StoryPanel />,
    document.getElementById('story')
);
