export function setupButton(element) {
  let clicked = false
  
  const setButtonText = (isClicked) => {
    clicked = isClicked
    if (clicked) {
      element.innerHTML = `Channeling Lebron's wisdom...`
      element.disabled = true
      
      // Navigate to chat page after a brief delay
      setTimeout(() => {
        window.location.href = '/chat.html';
      }, 1500)
    } else {
      element.innerHTML = `Get Started`
    }
  }
  
  element.addEventListener('click', () => setButtonText(true))
  setButtonText(false)
}
