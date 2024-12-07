document.addEventListener('DOMContentLoaded', function() {
    const signupButton = document.getElementById('signupButton');
    const acceptAndCloseTermsButton = document.getElementById('acceptAndCloseTerms');
    const toastEl = document.querySelector('.toast');
    const toast = new bootstrap.Toast(toastEl);
    let termsAccepted = false;

    acceptAndCloseTermsButton.addEventListener('click', function() {
        termsAccepted = true;
        signupButton.disabled = false;
        const modal = bootstrap.Modal.getInstance(document.getElementById('termsModal'));
        modal.hide();
    });

    signupButton.addEventListener('click', function(event) {
        if (!termsAccepted) {
            event.preventDefault();
            toast.show();
        }
    });
});