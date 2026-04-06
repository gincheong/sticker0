(function () {
  'use strict';

  // --- Cursor Glow ---
  var glow = document.querySelector('.cursor-glow');
  if (glow) {
    document.addEventListener('mousemove', function (e) {
      glow.style.transform =
        'translate(calc(' + e.clientX + 'px - 50%), calc(' + e.clientY + 'px - 50%))';
      glow.style.opacity = '1';
    });
    document.addEventListener('mouseleave', function () {
      glow.style.opacity = '0';
    });
  }

  // --- Scroll Reveal ---
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
          }
        });
      },
      { threshold: 0.1 }
    );
    reveals.forEach(function (el) { observer.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

  // --- Typing Effect ---
  function typeText(element, text, speed) {
    speed = speed || 60;
    return new Promise(function (resolve) {
      element.textContent = '';
      var i = 0;
      var timer = setInterval(function () {
        element.textContent += text.charAt(i);
        i++;
        if (i >= text.length) {
          clearInterval(timer);
          resolve();
        }
      }, speed);
    });
  }

  function initTyping() {
    var lines = document.querySelectorAll('.typing-text');
    var chain = Promise.resolve();

    lines.forEach(function (line) {
      var text = line.getAttribute('data-text');
      var delay = parseInt(line.getAttribute('data-delay') || '0', 10);
      if (!text) return;

      chain = chain.then(function () {
        if (delay > 0) {
          return new Promise(function (r) { setTimeout(r, delay); });
        }
      }).then(function () {
        return typeText(line, text);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', initTyping);

  // --- Copy Install Command ---
  window.copyInstall = function (btn) {
    if (!navigator.clipboard) {
      fallbackCopy('uv tool install sticker0');
      showCopied(btn);
      return;
    }
    navigator.clipboard.writeText('uv tool install sticker0').then(function () {
      showCopied(btn);
    });
  };

  function showCopied(btn) {
    btn.textContent = 'Copied!';
    btn.style.background = 'var(--accent)';
    btn.style.color = 'var(--bg)';
    setTimeout(function () {
      btn.textContent = 'Copy';
      btn.style.background = '';
      btn.style.color = '';
    }, 2000);
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
  }
})();
