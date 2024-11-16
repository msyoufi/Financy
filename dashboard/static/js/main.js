// Keep the label of an input at the top when input is not empty
document.querySelectorAll('.financy-input').forEach(input => {
  input.addEventListener('input', () => {
    const label = input.parentElement.querySelector('label');

    if (input.value)
      label.classList.add('top-label');
    else
      label.classList.remove('top-label');
  });
});
