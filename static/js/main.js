/* ============================================
   NIRMALA WOMEN'S CARE - MAIN JS
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

  // ---- NAVBAR SCROLL ----
  const nav = document.getElementById('mainNav');
  const scrollThreshold = 60;

  function handleNavScroll() {
    if (window.scrollY > scrollThreshold) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll();

  // ---- SMOOTH SCROLL NAV LINKS ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });

        // Close mobile menu
        const navCollapse = document.getElementById('navbarMain');
        if (navCollapse && navCollapse.classList.contains('show')) {
          const toggler = document.querySelector('.navbar-toggler');
          if (toggler) toggler.click();
        }
      }
    });
  });

  // ---- AOS ANIMATION ----
  const aosElements = document.querySelectorAll('[data-aos]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.getAttribute('data-aos-delay') || 0;
        setTimeout(() => {
          entry.target.classList.add('aos-animate');
        }, parseInt(delay));
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  aosElements.forEach(el => observer.observe(el));

  // ---- ANIMATED COUNTERS ----
  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current) + (el.getAttribute('data-suffix') || '');
    }, 16);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
        entry.target.classList.add('counted');
        animateCounter(entry.target);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.counter-num[data-target]').forEach(el => counterObserver.observe(el));

  // ---- TESTIMONIAL SLIDER ----
  const track = document.querySelector('.testimonial-track');
  const dots = document.querySelectorAll('.slider-dot');
  const prevBtn = document.querySelector('.slider-prev');
  const nextBtn = document.querySelector('.slider-next');

  if (track) {
    let currentSlide = 0;
    const cards = track.querySelectorAll('.testimonial-card');
    let slidesPerView = getSlidesPerView();
    let totalSlides = Math.ceil(cards.length / slidesPerView);
    let autoSlide;

    function getSlidesPerView() {
      if (window.innerWidth >= 1024) return 3;
      if (window.innerWidth >= 768) return 2;
      return 1;
    }

    function updateSlider() {
      const offset = -(currentSlide * (100 / slidesPerView) * slidesPerView);
      track.style.transform = `translateX(${offset / (cards.length / slidesPerView)}%)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === currentSlide));
    }

    function goTo(idx) {
      slidesPerView = getSlidesPerView();
      totalSlides = Math.ceil(cards.length / slidesPerView);
      currentSlide = ((idx % totalSlides) + totalSlides) % totalSlides;
      const offset = -(currentSlide * 100 * slidesPerView / cards.length);
      track.style.transform = `translateX(${offset}%)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === currentSlide));
    }

    if (prevBtn) prevBtn.addEventListener('click', () => { goTo(currentSlide - 1); resetAuto(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { goTo(currentSlide + 1); resetAuto(); });
    dots.forEach((d, i) => d.addEventListener('click', () => { goTo(i); resetAuto(); }));

    function startAuto() { autoSlide = setInterval(() => goTo(currentSlide + 1), 5000); }
    function resetAuto() { clearInterval(autoSlide); startAuto(); }
    startAuto();

    window.addEventListener('resize', () => goTo(0));

    // Touch swipe
    let touchStart = 0;
    track.addEventListener('touchstart', e => touchStart = e.changedTouches[0].screenX, { passive: true });
    track.addEventListener('touchend', e => {
      const diff = touchStart - e.changedTouches[0].screenX;
      if (Math.abs(diff) > 50) { goTo(diff > 0 ? currentSlide + 1 : currentSlide - 1); resetAuto(); }
    });
  }

  // ---- GALLERY LIGHTBOX ----
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');

  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', function() {
      const img = this.querySelector('img');
      if (img && lightbox && lightboxImg) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (lightbox) {
    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox || e.target.classList.contains('lightbox-close')) {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
      }
    });

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  // ---- BACK TO TOP ----
  const backTop = document.getElementById('backTop');
  if (backTop) {
    window.addEventListener('scroll', () => {
      backTop.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });
    backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  // ---- FORM VALIDATION ENHANCEMENT ----
  document.querySelectorAll('.needs-validation').forEach(form => {
    form.addEventListener('submit', function(e) {
      if (!form.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
      }
      form.classList.add('was-validated');
    });
  });

  // ---- AUTO DISMISS ALERTS ----
  setTimeout(() => {
    document.querySelectorAll('.alert').forEach(alert => {
      alert.style.transition = 'opacity 0.5s';
      alert.style.opacity = '0';
      setTimeout(() => alert.remove(), 500);
    });
  }, 5000);

});
