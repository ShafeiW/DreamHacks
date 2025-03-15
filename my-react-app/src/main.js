import './style.css'
import { setupButton } from './button.js'

document.querySelector('#app').innerHTML = `
  <div class="light-rays"></div>
  <div class="glow-effect"></div>
  <h1>Lebron GPT</h1>
  <p class="tagline">The wisdom of greatness, illuminated</p>
  <div class="card">
    <button id="start-button" type="button">Get Started</button>
  </div>
  <p class="description">
    Experience the ethereal basketball intelligence of the King
  </p>
  <p class="lebron-quote">
    "I'm always watching, always guiding. The path to greatness is never walked alone." - Ethereal Lebron
  </p>
`

// Repurpose the counter function for our start button
setupButton(document.querySelector('#start-button'))
