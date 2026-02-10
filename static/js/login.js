
document.addEventListener('DOMContentLoaded', () => {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const mobileSignUpButton = document.getElementById('mobileSignUp');
    const mobileSignInButton = document.getElementById('mobileSignIn');
    const container = document.getElementById('container');

    const togglePanel = (showSignUp) => {
        if (showSignUp) {
            container.classList.add("right-panel-active");
        } else {
            container.classList.remove("right-panel-active");
        }
    };

    if (signUpButton) signUpButton.addEventListener('click', () => togglePanel(true));
    if (signInButton) signInButton.addEventListener('click', () => togglePanel(false));
    if (mobileSignUpButton) mobileSignUpButton.addEventListener('click', () => togglePanel(true));
    if (mobileSignInButton) mobileSignInButton.addEventListener('click', () => togglePanel(false));

    // Auto-hide flash messages
    setTimeout(() => {
        const alerts = document.querySelectorAll('[role="alert"]');
        alerts.forEach(alert => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        });
    }, 3000);
});
