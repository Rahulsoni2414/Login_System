document.addEventListener('DOMContentLoaded', () => {
    // Navbar transparency on scroll
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('shadow-md');
            navbar.classList.add('bg-white/95');
            navbar.classList.remove('bg-white/80');
        } else {
            navbar.classList.remove('shadow-md');
            navbar.classList.remove('bg-white/95');
            navbar.classList.add('bg-white/80');
        }
    });

    // Stats Counter Animation
    const stats = [
        { id: 'stat-students', end: 12000, suffix: '+' },
        { id: 'stat-faculty', end: 300, suffix: '+' },
        { id: 'stat-courses', end: 50, suffix: '+' },
        { id: 'stat-awards', end: 150, suffix: '+' }
    ];

    const animateStats = () => {
        stats.forEach(stat => {
            const element = document.getElementById(stat.id);
            if (!element) return;

            const duration = 2000; // 2 seconds
            const start = 0;
            const stepTime = Math.abs(Math.floor(duration / (stat.end - start)));

            let current = start;
            const timer = setInterval(() => {
                current += Math.ceil(stat.end / 100); // Increment by 1% of total to be faster
                if (current >= stat.end) {
                    current = stat.end;
                    clearInterval(timer);
                }
                element.innerText = current.toLocaleString() + stat.suffix;
            }, 20);
        });
    };

    // Trigger animation when stats section is in view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.getElementById('stat-students'); // Use one element to trigger
    if (statsSection) {
        observer.observe(statsSection.closest('section'));
    }
});
