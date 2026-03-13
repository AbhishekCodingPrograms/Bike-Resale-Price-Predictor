/* ═══════════════════════════════════════════
   ABHISHEK MAURYA — Portfolio Script
   Animations: Stars · Code Typer · Typed Roles
                · Counter · Scroll Reveal · Nav
═══════════════════════════════════════════ */

/* ── 1. ANIMATED STARFIELD ── */
(function () {
  const canvas = document.getElementById('stars');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let stars = [];

  function resize() {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function makeStars(n) {
    stars = [];
    for (let i = 0; i < n; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 1.4 + 0.2,
        phase: Math.random() * Math.PI * 2,
        speed: Math.random() * 0.003 + 0.001,
      });
    }
  }

  function draw(t) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (const s of stars) {
      const alpha = 0.15 + 0.55 * Math.abs(Math.sin(t * s.speed + s.phase));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${alpha.toFixed(2)})`;
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  resize();
  makeStars(220);
  requestAnimationFrame(draw);
  window.addEventListener('resize', () => { resize(); makeStars(220); });
})();


/* ── 2. NAVBAR: blur on scroll + active link ── */
(function () {
  const nav   = document.getElementById('navbar');
  const links = document.querySelectorAll('.nav-link');
  const secs  = Array.from(document.querySelectorAll('section[id]'));

  function onScroll() {
    // blur background
    if (window.scrollY > 30) {
      nav.style.background   = 'rgba(0,0,0,0.82)';
      nav.style.borderBottom = '1px solid rgba(255,255,255,0.06)';
    } else {
      nav.style.background   = '';
      nav.style.borderBottom = '';
    }
    // active link
    const y = window.scrollY + 130;
    let active = '';
    secs.forEach(s => { if (s.offsetTop <= y) active = s.id; });
    links.forEach(l => {
      l.classList.toggle('active', l.getAttribute('href').replace('#', '') === active);
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();


/* ── 3. SMOOTH ANCHOR SCROLL ── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  });
});


/* ── 4. SCROLL REVEAL ── */
(function () {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll(
    '.section, .feature-card, .exp-card, .edu-card, .ach-card, .project-card, .skill-card'
  ).forEach((el, i) => {
    el.classList.add('reveal');
    // stagger cards inside grids
    if (el.closest('.projects-grid') || el.closest('.skills-grid') || el.closest('.ach-grid')) {
      el.style.transitionDelay = `${(i % 4) * 0.1}s`;
    }
    io.observe(el);
  });
})();


/* ── 5. TYPING ROLES (hero subtitle) ── */
(function () {
  const el = document.querySelector('.typed-role');
  if (!el) return;

  const roles = [
    'AI & ML Enthusiast',
    'Data Analyst',
    'Python Developer',
    'Problem Solver',
    'Deep Learning Explorer',
  ];
  let ri = 0, ci = 0, deleting = false;

  function tick() {
    const role = roles[ri];
    if (!deleting) {
      el.textContent = role.slice(0, ++ci);
      if (ci === role.length) { deleting = true; setTimeout(tick, 1800); return; }
      setTimeout(tick, 65);
    } else {
      el.textContent = role.slice(0, --ci);
      if (ci === 0) { deleting = false; ri = (ri + 1) % roles.length; setTimeout(tick, 400); return; }
      setTimeout(tick, 35);
    }
  }
  setTimeout(tick, 800);
})();


/* ── 6. ANIMATED CODE TYPER ── */
(function () {
  const body = document.getElementById('codeBody');
  if (!body) return;

  // Color-tagged spans for syntax highlighting
  const lines = [
    [
      { cls: 'kw', t: 'import' }, { cls: 'op', t: ' transformers, torch' }
    ],
    [],
    [
      { cls: 'var', t: 'model_id' }, { cls: 'op', t: ' = ' }, { cls: 'st', t: '"meta-llama/Llama-3.1-8B"' }
    ],
    [],
    [
      { cls: 'var', t: 'pipeline' }, { cls: 'op', t: ' = ' },
      { cls: 'fn', t: 'transformers' }, { cls: 'op', t: '.pipeline(' },
      { cls: 'st', t: '"text-generation"' }, { cls: 'op', t: ', model...)' }
    ],
    [],
    [
      { cls: 'var', t: 'response' }, { cls: 'op', t: ' = ' },
      { cls: 'fn', t: 'pipeline' }, { cls: 'op', t: '(' },
      { cls: 'st', t: '"Create AI solutions"' }, { cls: 'op', t: ')' }
    ],
    [],
    [
      { cls: 'fn', t: 'print' }, { cls: 'op', t: '(' },
      { cls: 'st', t: '"Building intelligent systems"' }, { cls: 'op', t: ')' }
    ],
    [],
    [
      { cls: 'cm', t: '# Transforming ideas into reality 🚀' }
    ],
  ];

  let lineIdx = 0;

  function renderLine(tokens, lineNum) {
    const row = document.createElement('div');
    row.className = 'code-line';
    const ln = document.createElement('span');
    ln.className = 'ln';
    ln.textContent = lineNum;
    row.appendChild(ln);

    const content = document.createElement('span');
    tokens.forEach(tok => {
      const s = document.createElement('span');
      s.className = tok.cls;
      s.textContent = tok.t;
      content.appendChild(s);
    });
    row.appendChild(content);
    return row;
  }

  function renderEmptyLine(lineNum) {
    const row = document.createElement('div');
    row.className = 'code-line';
    const ln = document.createElement('span');
    ln.className = 'ln';
    ln.textContent = lineNum;
    row.appendChild(ln);
    return row;
  }

  // Typing cursor indicator (last line)
  const cursorEl = document.createElement('span');
  cursorEl.className = 'typing-cursor';

  function addNextLine() {
    if (lineIdx >= lines.length) {
      // After all lines, restart after pause
      setTimeout(() => {
        body.innerHTML = '';
        lineIdx = 0;
        addNextLine();
      }, 4000);
      return;
    }

    const tokens = lines[lineIdx];
    const displayNum = lineIdx + 1;

    // Remove cursor from previous line if exists
    if (cursorEl.parentNode) cursorEl.parentNode.removeChild(cursorEl);

    if (tokens.length === 0) {
      body.appendChild(renderEmptyLine(displayNum));
      lineIdx++;
      setTimeout(addNextLine, 120);
    } else {
      const row = renderLine(tokens, displayNum);
      body.appendChild(row);
      row.lastChild.appendChild(cursorEl);
      lineIdx++;
      setTimeout(addNextLine, 380 + Math.random() * 180);
    }

    // Auto-scroll code body
    body.scrollTop = body.scrollHeight;
  }

  setTimeout(addNextLine, 1000);
})();


/* ── 7. NUMBER COUNTERS ── */
(function () {
  const nums = document.querySelectorAll('.stat-num[data-target]');
  if (!nums.length) return;

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el     = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const dur    = 1400;
      const step   = 16;
      const steps  = dur / step;
      let cur = 0;

      const timer = setInterval(() => {
        cur = Math.min(cur + Math.ceil(target / steps), target);
        el.textContent = cur;
        if (cur >= target) clearInterval(timer);
      }, step);

      io.unobserve(el);
    });
  }, { threshold: 0.6 });

  nums.forEach(n => io.observe(n));
})();
