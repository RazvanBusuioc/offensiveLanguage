import acsLogo from './sigla_cs.png';
import upbLogo from './upb-logo.jpg';
import submitLogo from './debug-start.svg'
import { useState, useRef, useEffect } from "react";
import './App.css';
import axios from 'axios'

function App() {
  const [currText, setText] = useState("");
  const [messages, setMessages] = useState([]);
  const chatRef = useRef()

  const api = axios.create({
    baseURL: 'http://localhost:7020/api',
  })
  const postMessage = (message) => api.post('/fbro/text', {text: message})

  const addMessage = async (m) => {
    const prediction = await predict(m)
    setMessages((t) => [...t, prediction]);
  };

  const predict = async (text) => {
    const r = await postMessage(text);
    return {
      text: text,
      class: r.data
    }
  }

  const handleChange = (event) => {
    setText(event.target.value)
  }
  
  const handleSubmit = (event) => {
    event.preventDefault();
    if (currText == "")
      return;
    setText("");
    addMessage(currText);
    
  }

  useEffect(() => {
    chatRef.current.scrollIntoView({ behavior: 'smooth' })
  })

  return (
    <div className="desktop">
      <div className="app">
        <div className="logos">
          <div>
            <img className="upbLogo" src={upbLogo}/>
          </div>
          <div>
            <img className="acsLogo" src={acsLogo}/>
          </div>
        </div>

        <div className="title">
          <h1>Offensive Language Detection</h1>
        </div>

        <div className="chat">

          <div className="chatMessages">

            {messages.map((message, key) => (
              <div className={key % 2 == 0 ? "chatMessageLeft" : "chatMessageRight"}>
                <div className={"chatMessage " + message.class.toLowerCase()}>
                  {message.text}
                </div>
              </div>
            ))}

            <div ref={chatRef}>

            </div>

          </div>
          <form onSubmit={handleSubmit}>
            <div className="chatForm">
              <input className="formInput" onChange={handleChange} value={currText || ""}></input>
              <button className="submitButton" type="submit" >
                <img className="submitLogo" src={submitLogo}/>
              </button>
            </div>
          </form>

        </div>
      </div>
    </div>
  );
}

export default App;
