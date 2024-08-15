document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form"),
      emailField = form.querySelector(".email-field"),
      emailInput = emailField.querySelector(".email"),
      passField = form.querySelector(".create-password"),
      passInput = passField.querySelector(".password");

  // Ensure the emailInput and passInput are found
  if (!emailInput || !passInput) {
      console.error("Email or Password input not found!");
      return;
  }

  // Email Validation
  function checkEmail() {
      const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
      if (!emailInput.value.match(emailPattern)) {
          return emailField.classList.add("invalid");
      }
      emailField.classList.remove("invalid");
  }

  // Hide and show password
  const eyeIcons = document.querySelectorAll(".show-hide");

  eyeIcons.forEach((eyeIcon) => {
      eyeIcon.addEventListener("click", () => {
          const pInput = eyeIcon.parentElement.querySelector("input");
          if (pInput.type === "password") {
              eyeIcon.classList.replace("bx-hide", "bx-show");
              return (pInput.type = "text");
          }
          eyeIcon.classList.replace("bx-show", "bx-hide");
          pInput.type = "password";
      });
  });

  // Password Validation
  function createPass() {
      const passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

      if (!passInput.value.match(passPattern)) {
          return passField.classList.add("invalid");
      }
      passField.classList.remove("invalid");
  }

  // Calling Function on Form Submit
  form.addEventListener("submit", (e) => {
      e.preventDefault(); // Prevent form submission to perform validation first
      checkEmail();
      createPass();

      // Calling validation functions on key up to provide immediate feedback
      emailInput.addEventListener("keyup", checkEmail);
      passInput.addEventListener("keyup", createPass);

      // If no validation errors, submit the form
      if (
          !emailField.classList.contains("invalid") &&
          !passField.classList.contains("invalid")
      ) {
          form.submit();  // Submit the form to the server
      } else {
          console.log("Form submission prevented due to validation errors");  // Log if validation fails
      }
  });
});
