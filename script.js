// Mobile Menu Toggle
const mobileToggle = document.getElementById('mobileToggle');
const navLinks = document.getElementById('navLinks');
const header = document.getElementById('header');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        navLinks.classList.toggle('mobile-open');
        const icon = navLinks.classList.contains('mobile-open') ? 'x' : 'menu';
        mobileToggle.innerHTML = `<i data-lucide="${icon}"></i>`;
        lucide.createIcons();
    });
}

// Header Scroll Effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Initialize Lucide Icons
if (typeof lucide !== 'undefined') {
    lucide.createIcons();
}
