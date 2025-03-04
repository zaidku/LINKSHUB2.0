// Back-to-Top Button
document.addEventListener('DOMContentLoaded', function () {
    const backToTopButton = document.getElementById('back-to-top');

    // Show/hide the button based on scroll position
    window.addEventListener('scroll', function () {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Smooth scroll to top when the button is clicked
    backToTopButton.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});

// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');

    // Toggle dark mode
    darkModeToggle.addEventListener('change', function () {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('darkMode', this.checked);
    });

    // Check for saved preference
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }
});

// Toast Notifications
function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    const toastBody = toast.querySelector('.toast-body');

    // Set the toast message and type
    toastBody.textContent = message;
    toast.classList.add(`bg-${type}`);

    // Show the toast
    const toastInstance = new bootstrap.Toast(toast);
    toastInstance.show();
}

// Example usage of showToast:
// showToast('This is a success message!', 'success');
// showToast('This is an error message!', 'danger');

// Loading Spinner
function showSpinner() {
    document.getElementById('loading-spinner').classList.remove('d-none');
}

function hideSpinner() {
    document.getElementById('loading-spinner').classList.add('d-none');
}

// Example usage of loading spinner:
// showSpinner(); // Show the spinner
// hideSpinner(); // Hide the spinner

// Sidebar Toggle (Bootstrap handles this automatically, no JS needed)