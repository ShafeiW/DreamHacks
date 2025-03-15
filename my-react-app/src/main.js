import './style.css'
import { setupCounter } from './counter.js'

document.querySelector('#app').innerHTML = `
  <div class="lebron-container">
    <div class="glow-effect"></div>
    <h1>Lebron GPT</h1>
    <p class="tagline">The wisdom of greatness, illuminated</p>
    <div class="card">
      <button id="start-button" type="button">Get Started</button>
    </div>
    <p class="description">
      Experience the ethereal basketball intelligence of the King
    </p>
  </div>
`

// Repurpose the counter function for our start button
setupCounter(document.querySelector('#start-button'))
