document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const navLinksItems = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close mobile menu when clicking a link
    navLinksItems.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // 2. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Active link highlighting
        let current = '';
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (scrollY >= sectionTop - 150) {
                current = section.getAttribute('id');
            }
        });
        
        navLinksItems.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current) && current !== '') {
                link.classList.add('active');
            }
        });
    });

    // 3. Scroll Reveal Animations
    const revealElements = document.querySelectorAll('.reveal');
    
    if ('IntersectionObserver' in window) {
        const revealOptions = {
            threshold: 0.02,
            rootMargin: "100px 0px 100px 0px"
        };
        
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, revealOptions);
        
        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        revealElements.forEach(el => el.classList.add('visible'));
    }

    // Force visibility check on load for all visible elements
    setTimeout(() => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight + 300) {
                el.classList.add('visible');
            }
        });
    }, 100);

    // 4. Stats Counter Animation
    const counters = document.querySelectorAll('.counter');
    let hasAnimated = false;
    
    const counterObserver = new IntersectionObserver((entries) => {
        const [entry] = entries;
        if (entry.isIntersecting && !hasAnimated) {
            hasAnimated = true;
            
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const duration = 2000; // ms
                const increment = target / (duration / 16); // 60fps
                
                let current = 0;
                const updateCounter = () => {
                    current += increment;
                    if (current < target) {
                        counter.innerText = Math.ceil(current) + (target > 10 ? '+' : '');
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.innerText = target + (target > 10 ? '+' : '');
                    }
                };
                
                updateCounter();
            });
        }
    }, { threshold: 0.5 });
    
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        counterObserver.observe(statsSection);
    }

    // 5. Contact Form Submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.innerText;
            
            btn.innerText = 'Enviando...';
            btn.style.opacity = '0.8';
            
            // Simulate network request
            setTimeout(() => {
                btn.innerText = '¡Mensaje Enviado!';
                btn.style.backgroundColor = 'var(--color-success)';
                btn.style.color = '#fff';
                
                contactForm.reset();
                
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.style.backgroundColor = '';
                    btn.style.opacity = '1';
                }, 3000);
            }, 1500);
        });
    }

    // 6. Interactive Theme Switcher (2026 Color Palette Tester)
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeMenu = document.getElementById('themeMenu');
    const themeOptions = document.querySelectorAll('.theme-option');

    // Force default red-brand theme and sync localStorage
    const savedTheme = localStorage.getItem('asetran-theme') || 'red-brand';
    document.documentElement.setAttribute('data-theme', savedTheme);

    if (themeToggleBtn && themeMenu) {
        themeToggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            themeMenu.classList.toggle('active');
        });

        document.addEventListener('click', (e) => {
            if (!themeMenu.contains(e.target) && e.target !== themeToggleBtn) {
                themeMenu.classList.remove('active');
            }
        });

        themeOptions.forEach(option => {
            option.addEventListener('click', () => {
                const theme = option.getAttribute('data-theme');
                document.documentElement.setAttribute('data-theme', theme);
                localStorage.setItem('asetran-theme', theme);
                
                themeOptions.forEach(opt => opt.classList.remove('active'));
                option.classList.add('active');
            });
        });
    }

    // 7. Animated Hero Canvas (Road Safety Network & Traffic Traces)
    const canvas = document.getElementById('heroCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];
        let pulses = [];

        function resize() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        }
        window.addEventListener('resize', resize);
        resize();

        function getThemeColor() {
            const style = getComputedStyle(document.documentElement);
            let hex = style.getPropertyValue('--color-primary').trim() || '#84A98C';
            hex = hex.replace('#', '');
            if (hex.length === 3) hex = hex.split('').map(x => x + x).join('');
            const num = parseInt(hex, 16);
            return {
                r: (num >> 16) & 255,
                g: (num >> 8) & 255,
                b: num & 255
            };
        }

        class Particle {
            constructor() {
                this.reset();
            }

            reset() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.7;
                this.vy = (Math.random() - 0.5) * 0.7;
                this.size = Math.random() * 2 + 1;
                this.alpha = Math.random() * 0.5 + 0.3;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }

            draw(rgb) {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${this.alpha})`;
                ctx.fill();
            }
        }

        const count = Math.min(Math.floor((width * height) / 12000), 70);
        for (let i = 0; i < count; i++) {
            particles.push(new Particle());
        }

        class Pulse {
            constructor(p1, p2) {
                this.p1 = p1;
                this.p2 = p2;
                this.progress = 0;
                this.speed = 0.01 + Math.random() * 0.015;
            }

            update() {
                this.progress += this.speed;
            }

            draw(rgb) {
                const x = this.p1.x + (this.p2.x - this.p1.x) * this.progress;
                const y = this.p1.y + (this.p2.y - this.p1.y) * this.progress;
                
                ctx.beginPath();
                ctx.arc(x, y, 2.5, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(255, 255, 255, 0.95)`;
                ctx.shadowBlur = 8;
                ctx.shadowColor = `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, 1)`;
                ctx.fill();
                ctx.shadowBlur = 0;
            }
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            const rgb = getThemeColor();

            particles.forEach(p => {
                p.update();
                p.draw(rgb);
            });

            const maxDist = 130;
            const connectedPairs = [];

            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const p1 = particles[i];
                    const p2 = particles[j];
                    const dx = p1.x - p2.x;
                    const dy = p1.y - p2.y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < maxDist) {
                        const alpha = (1 - dist / maxDist) * 0.25;
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${alpha})`;
                        ctx.lineWidth = 1;
                        ctx.stroke();

                        connectedPairs.push({ p1, p2 });
                    }
                }
            }

            if (Math.random() < 0.05 && connectedPairs.length > 0) {
                const pair = connectedPairs[Math.floor(Math.random() * connectedPairs.length)];
                pulses.push(new Pulse(pair.p1, pair.p2));
            }

            for (let i = pulses.length - 1; i >= 0; i--) {
                const pulse = pulses[i];
                pulse.update();
                pulse.draw(rgb);
                if (pulse.progress >= 1) {
                    pulses.splice(i, 1);
                }
            }

            requestAnimationFrame(animate);
        }

        animate();
    }

    // 9. Interactive Technical Service Detail Modal
    const serviceModal = document.getElementById('serviceModal');
    const modalContentBody = document.getElementById('modalContentBody');
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    const servicePortalCards = document.querySelectorAll('.service-portal-card');

    if (serviceModal && modalContentBody) {
        servicePortalCards.forEach(card => {
            card.addEventListener('click', (e) => {
                const serviceKey = card.getAttribute('data-service');
                if (!serviceKey) return; // Allow direct page navigation for <a> links
                
                const template = document.getElementById(`template-${serviceKey}`);
                if (template) {
                    e.preventDefault();
                    modalContentBody.innerHTML = template.innerHTML;
                    serviceModal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            });
        });

        const closeModal = () => {
            serviceModal.classList.remove('active');
            document.body.style.overflow = '';
        };

        if (modalCloseBtn) {
            modalCloseBtn.addEventListener('click', closeModal);
        }

        serviceModal.addEventListener('click', (e) => {
            if (e.target === serviceModal) {
                closeModal();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && serviceModal.classList.contains('active')) {
                closeModal();
            }
        });
    }
});
