document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form"),
        usernameField = form.querySelector("[name='username']"),
        passField = form.querySelector("[name='password']"),
        eyeIcons = document.querySelectorAll(".show-hide");

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

    // Show/Hide Password Functionality
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

    // Basic Validation Before Form Submission
    form.addEventListener("submit", (e) => {
        if (usernameField.value.trim() === "" || passField.value.trim() === "") {
            e.preventDefault(); // Prevent form submission if validation fails
            alert("Please fill out both fields.");
        }
    });
});
