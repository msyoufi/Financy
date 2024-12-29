const formOverlay = document.getElementById('form_overlay');
const tranxForm = document.getElementById('transaction_form');
const formTitle = document.getElementById('form_title');
const tranxSubmit = document.getElementById('tranx_submit');
const deleteDialogOverlay = document.getElementById('delete_dialog_overlay');
const deleteButton = document.getElementById('delete_button');
const CSRFToken =
  document.querySelector('input[name="csrfmiddlewaretoken"]').value;

function openAddForm() {
  setDateInputToNow();
  formTitle.innerText = 'Add a new Transaction';
  tranxSubmit.innerText = 'Add';
  tranxForm.action = '/transactions';
  formOverlay.style.display = 'flex';
}

function openEditForm(tranxId) {
  populateForm(tranxId);
  formTitle.innerText = 'Edit Transaction';
  tranxSubmit.innerText = 'Save';
  tranxForm.action = '/transactions/' + tranxId;
  formOverlay.style.display = 'flex';
}

function closeForm() {
  resetForm();
  formOverlay.style.display = 'none';
  tranxSubmit.disabled = true;
}

function setDateInputToNow() {
  const now = new Date();

  tranxForm.querySelector('input[type="date"]')
    .value = `${now.getFullYear()}-${now.getMonth() + 1}-${now.getDate()}`;
}

async function populateForm(tranxId) {
  const tranxData = await getTranxData(tranxId);
  tranxForm.querySelectorAll('input, select').forEach(input => {
    const value = tranxData[input.name];

    if (input.type === 'radio')
      input.checked = value === input.value;
    else if (input.name !== 'csrfmiddlewaretoken')
      input.value = value;

    if (input.value) {
      const label = input.parentElement.querySelector('label');
      label.classList.add('top-label');
    }
  });
}

async function getTranxData(tranxId) {
  const res = await fetch(`transactions/${tranxId}`);
  return await res.json();
}

function toggleSubmit() {
  if (tranxForm.checkValidity())
    tranxSubmit.disabled = false;
  else
    tranxSubmit.disabled = true;
}

function resetForm() {
  tranxForm.reset();
  tranxForm.action = '';
  tranxForm.querySelectorAll('input, select').forEach(input => {
    const label = input.parentElement.querySelector('label');
    if (input.name !== 'date')
      label.classList.remove('top-label');
  });
}

function confirmDelete(tranxId) {
  deleteDialogOverlay.style.display = 'flex';
  deleteButton.dataset.tranxId = tranxId;
}

async function deleteTranx() {
  const tranxId = deleteButton.dataset.tranxId;
  const headers = { 'X-CSRFToken': CSRFToken };
  const res = await fetch(`transactions/${tranxId}`, { method: 'DELETE', headers });

  if (res.status === 200)
    document.getElementById('tranx_' + tranxId).remove();

  closeDeleteDialog();
}

function closeDeleteDialog() {
  deleteButton.dataset.tranxId = '';
  deleteDialogOverlay.style.display = 'none';
}

// Close popups on overlay clicked
document.querySelectorAll('.overlay').forEach(overlay => {
  overlay.addEventListener('click', (event) => {
    const isOverlay = event.target.id.includes('overlay');
    if (isOverlay) {
      overlay.style.display = 'none';
      closeForm();
    }
  });
});