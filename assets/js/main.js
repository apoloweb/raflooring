// RA Flooring — shared behavior
(function () {
  'use strict';

  // sticky header
  var header = document.getElementById('siteHeader');
  var onScroll = function () {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // mobile nav
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('mainNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
      document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        toggle.classList.remove('open');
        nav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
    var dropToggle = nav.querySelector('.drop-toggle');
    if (dropToggle && window.matchMedia('(max-width:1080px)').matches) {
      dropToggle.addEventListener('click', function (e) {
        e.preventDefault();
        dropToggle.closest('.nav-drop').classList.toggle('open');
      });
    }
  }

  // reveal on scroll
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('visible');
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  // animated counters — <span data-count="512" data-suffix="+">
  var counters = document.querySelectorAll('[data-count]');
  var animateCounter = function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var decimals = (String(el.getAttribute('data-count')).split('.')[1] || '').length;
    var dur = 1800, start = null;
    var step = function (ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          animateCounter(en.target);
          cio.unobserve(en.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.textContent = el.getAttribute('data-count') + (el.getAttribute('data-suffix') || '');
    });
  }

  // before/after slider
  document.querySelectorAll('.ba-wrap').forEach(function (wrap) {
    var after = wrap.querySelector('.ba-after');
    var handle = wrap.querySelector('.ba-handle');
    var setPos = function (clientX) {
      var r = wrap.getBoundingClientRect();
      var x = Math.min(Math.max(clientX - r.left, 0), r.width);
      var pct = (x / r.width) * 100;
      after.style.clipPath = 'inset(0 0 0 ' + pct + '%)';
      handle.style.left = pct + '%';
    };
    var dragging = false;
    wrap.addEventListener('mousedown', function (e) { dragging = true; setPos(e.clientX); });
    window.addEventListener('mousemove', function (e) { if (dragging) setPos(e.clientX); });
    window.addEventListener('mouseup', function () { dragging = false; });
    wrap.addEventListener('touchstart', function (e) { dragging = true; setPos(e.touches[0].clientX); }, { passive: true });
    wrap.addEventListener('touchmove', function (e) { if (dragging) setPos(e.touches[0].clientX); }, { passive: true });
    window.addEventListener('touchend', function () { dragging = false; });
  });

  // gallery videos: pause the others when one plays
  var videos = document.querySelectorAll('.video-card video');
  videos.forEach(function (v) {
    v.addEventListener('play', function () {
      videos.forEach(function (o) { if (o !== v) o.pause(); });
    });
  });

  // contact form: point the redirect at this site's thank-you page
  var next = document.querySelector('input[name="_next"]');
  if (next && !next.value) {
    next.value = location.href.replace(/[^/]*$/, '') + 'thank-you.html';
  }

  // footer year
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();
})();
