document.addEventListener('DOMContentLoaded', function() {
    // Get all alert elements
    const alerts = document.querySelectorAll('.alert');
    
    // Add fade-out and remove each alert after 5 seconds
    alerts.forEach(function(alert) {
        setTimeout(function() {
            // Add fade-out class
            alert.classList.add('fade-out');
            
            // Remove the alert after fade animation
            setTimeout(function() {
                alert.style.display = 'none';
                alert.remove();
            }, 500);
        }, 5000);
    });
});
