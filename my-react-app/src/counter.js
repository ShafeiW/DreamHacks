export function setupCounter(element) {
  let clicked = false
  
  const setButtonText = (isClicked) => {
    clicked = isClicked
    if (clicked) {
      element.innerHTML = `Channeling Lebron's wisdom...`
      element.disabled = true
      
      // Simulate loading and then show a message
      setTimeout(() => {
        alert("The King's wisdom is coming soon! This feature is under development.")
        element.innerHTML = `Get Started`
        element.disabled = false
        clicked = false
      }, 2000)
    } else {
      element.innerHTML = `Get Started`
    }
  }
  
  element.addEventListener('click', () => setButtonText(true))
  setButtonText(false)
}
