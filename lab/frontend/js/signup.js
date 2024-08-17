const form = document.querySelector("form"),
  nameField = form.querySelector(".name-field"),
  nameInput = nameField.querySelector(".name"),
  usernameField = form.querySelector(".username-field"),
  usernameInput = usernameField.querySelector(".username"),
  emailField = form.querySelector(".email-field"),
  emailInput = emailField.querySelector(".email"),
  passField = form.querySelector(".create-password"),
  passInput = passField.querySelector(".password"),
  cPassField = form.querySelector(".confirm-password"),
  cPassInput = cPassField.querySelector(".cPassword");

// CSRF token helper function
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Add the CSRF token to the form
const csrfToken = getCSRFToken();
const csrfInput = document.createElement('input');
csrfInput.type = 'hidden';
csrfInput.name = 'csrfmiddlewaretoken';
csrfInput.value = csrfToken;
form.appendChild(csrfInput);

// Validation functions
function checkName() {
  const namePattern = /^[a-zA-Z\s]+$/;
  if (!nameInput.value.match(namePattern)) {
    nameField.classList.add("invalid");
  } else {
    nameField.classList.remove("invalid");
  }
}

function checkUsername() {
  const usernamePattern = /^[a-zA-Z0-9_]+$/;
  if (!usernameInput.value.match(usernamePattern)) {
    usernameField.classList.add("invalid");
  } else {
    usernameField.classList.remove("invalid");
  }
}

function checkEmail() {
  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!emailInput.value.match(emailPattern)) {
    emailField.classList.add("invalid");
  } else {
    emailField.classList.remove("invalid");
  }
}

function createPass() {
  const passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passInput.value.match(passPattern)) {
    passField.classList.add("invalid");
  } else {
    passField.classList.remove("invalid");
  }
}

function confirmPass() {
  if (passInput.value !== cPassInput.value || cPassInput.value === "") {
    cPassField.classList.add("invalid");
  } else {
    cPassField.classList.remove("invalid");
  }
}

// Hide and show password
const eyeIcons = document.querySelectorAll(".show-hide");

eyeIcons.forEach((eyeIcon) => {
  eyeIcon.addEventListener("click", () => {
    const pInput = eyeIcon.parentElement.querySelector("input");
    if (pInput.type === "password") {
      eyeIcon.classList.replace("bx-hide", "bx-show");
      pInput.type = "text";
    } else {
      eyeIcon.classList.replace("bx-show", "bx-hide");
      pInput.type = "password";
    }
  });
});

// Call validation on form submission
form.addEventListener("submit", (e) => {
  checkName();
  checkUsername();
  checkEmail();
  createPass();
  confirmPass();

  // Prevent form submission if there are invalid fields
  if (
    nameField.classList.contains("invalid") ||
    usernameField.classList.contains("invalid") ||
    emailField.classList.contains("invalid") ||
    passField.classList.contains("invalid") ||
    cPassField.classList.contains("invalid")
  ) {
    e.preventDefault();
  }
});
