// Keep the input's label at top when not empty
document.querySelectorAll('.financy-input').forEach(input => {
  input.addEventListener('input', () => {
    const label = input.parentElement.querySelector('label');

    if (input.value)
      label.classList.add('top-label');
    else
      label.classList.remove('top-label');
  });
});


// Close popups on overlay clicked
document.querySelectorAll('.overlay').forEach(overlay => {
  overlay.addEventListener('click', (event) => {
    const isOverlay = event.target.id.includes('overlay');
    if (isOverlay)
      overlay.style.display = 'none';
  });
});