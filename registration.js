document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('.form');
    const firstNameInput = form.querySelector('input[name="firstName"]');
    const lastNameInput = form.querySelector('input[name="lastName"]');
    const passwordInput = form.querySelector('input[name="password"]');
    const confirmPasswordInput = form.querySelector('input[name="confirmPassword"]');
    const emailInput = form.querySelector('input[name="email"]');
    const phoneInput = form.querySelector('input[name="phone"]');
    const addressInput = form.querySelector('textarea[name="address"]');
    const postalCodeInput = form.querySelector('input[name="postalCode"]');
    const termsCheckbox = form.querySelector('input[type="checkbox"]');
    const submitButton = form.querySelector('input[type="submit"]');

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        if (!validateRequired(firstNameInput.value) ||
            !validateRequired(lastNameInput.value) ||
            !validateRequired(passwordInput.value) ||
            !validateRequired(confirmPasswordInput.value) ||
            !validateRequired(emailInput.value) ||
            !validateRequired(phoneInput.value) ||
            !validateRequired(addressInput.value) ||
            !validateRequired(postalCodeInput.value)) {
            alert("Please fill in all required fields.");
            return;
        }

        if (passwordInput.value !== confirmPasswordInput.value) {
            alert("Passwords do not match.");
            return;
        }

        if (!validateEmail(emailInput.value)) {
            alert("Please enter a valid email address.");
            return;
        }
        if (!validatePhoneNumber(phoneInput.value)) {
            alert("Please enter a valid phone number.");
            return;
        }

        if (!termsCheckbox.checked) {
            alert("Please agree to terms and conditions.");
            return;
        }
        

        // Form submission logic here
        alert("Registration successful!");
        form.reset();
    });

    function validateRequired(value) {
        return value.trim() !== '';
    }

    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    function validatePhoneNumber(phoneInput) {
        var phoneRegex = /^\d{10}$/;
        return phoneRegex.test(phoneInput);
    }
});

