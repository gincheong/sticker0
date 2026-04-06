# sticker0 Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** GitHub Pages에 배포할 sticker0 프로젝트 홍보용 1페이지 정적 랜딩 페이지 제작

**Architecture:** Caveman(juliusbrussee.github.io/caveman) 스타일의 다크 터미널 미학. 순수 HTML/CSS/JS, 프레임워크 없음. 3-레이어 배경 시스템(grid + aura + cursor glow) + IntersectionObserver 스크롤 리빌 + 타이핑 효과. 4개 섹션: Hero → Screenshot → Features(Bento Grid) → Installation.

**Tech Stack:** HTML5, CSS3 (CSS Variables, Grid, Flexbox, backdrop-filter), Vanilla JS (IntersectionObserver, Clipboard API). Google Fonts (Inter + JetBrains Mono).

**GitHub Pages:** main 브랜치 `/docs` 폴더에서 서빙. URL: `https://lee-do-jun.github.io/sticker0/`

---

## File Structure

```
docs/
  index.html          — 메인 페이지 (HTML + SEO 메타 + JSON-LD)
  style.css            — 전체 스타일 (변수, 리셋, 배경, 컴포넌트, 반응형)
  script.js            — 인터랙션 (커서 글로우, 스크롤 리빌, 타이핑, 클립보드)
  assets/
    screenshot-1.png   — 앱 스크린샷 (리포 루트 assets/에서 복사)
```

**디자인 토큰 (CSS Variables):**

| Token | Value | 용도 |
|-------|-------|------|
| `--bg` | `#09090b` | 페이지 배경 |
| `--bg-elevated` | `#18181b` | 카드/프레임 배경 |
| `--border` | `#27272a` | 보더, 구분선 |
| `--border-hover` | `#3f3f46` | 호버 보더 |
| `--text-primary` | `#fafafa` | 본문 텍스트 |
| `--text-secondary` | `#a1a1aa` | 보조 텍스트 |
| `--text-tertiary` | `#52525b` | 약한 텍스트 |
| `--accent` | `#f59e0b` | 액센트 (앰버, 스티키 노트 연상) |
| `--accent-glow` | `rgba(245,158,11,0.15)` | 글로우/아우라 |

---

### Task 1: Project Scaffold

**Files:**
- Create: `docs/index.html` (빈 뼈대)
- Create: `docs/style.css` (빈 파일)
- Create: `docs/script.js` (빈 파일)
- Create: `docs/assets/` (디렉터리)
- Copy: `assets/screenshot-1.png` → `docs/assets/screenshot-1.png`

- [ ] **Step 1: 디렉터리 생성 및 스크린샷 복사**

```bash
mkdir -p docs/assets
cp assets/screenshot-1.png docs/assets/screenshot-1.png
```

- [ ] **Step 2: 빈 CSS, JS 파일 생성**

```bash
touch docs/style.css docs/script.js
```

- [ ] **Step 3: 최소 HTML 뼈대 작성**

`docs/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>sticker0</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>sticker0</h1>
  <script src="script.js"></script>
</body>
</html>
```

- [ ] **Step 4: 브라우저에서 확인**

```bash
open docs/index.html
```

Expected: 흰 배경에 "sticker0" 텍스트만 표시

- [ ] **Step 5: 커밋**

```bash
git add docs/
git commit -m "scaffold: landing page project structure with screenshot asset"
```

---

### Task 2: HTML Structure + SEO

**Files:**
- Modify: `docs/index.html`

전체 HTML 구조를 한 번에 작성한다. SEO 메타 태그, Open Graph, JSON-LD 포함.

- [ ] **Step 1: index.html 전체 작성**

`docs/index.html` 내용을 아래로 교체:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>sticker0 — Terminal Sticky Notes</title>
  <meta name="description" content="A mouse-first TUI sticky notes app for your terminal. Drag, resize, customize colors and themes. Built with Python and Textual.">
  <meta name="keywords" content="terminal sticky notes, terminal sticker, TUI app, terminal notes, sticky notes CLI, textual app, python TUI, terminal post-it">
  <link rel="canonical" href="https://lee-do-jun.github.io/sticker0/">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://lee-do-jun.github.io/sticker0/">
  <meta property="og:title" content="sticker0 — Terminal Sticky Notes">
  <meta property="og:description" content="A mouse-first TUI sticky notes app. Drag, resize, and organize notes inside your terminal.">
  <meta property="og:image" content="https://lee-do-jun.github.io/sticker0/assets/screenshot-1.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="sticker0 — Terminal Sticky Notes">
  <meta name="twitter:description" content="A mouse-first TUI sticky notes app. Drag, resize, and organize notes inside your terminal.">
  <meta name="twitter:image" content="https://lee-do-jun.github.io/sticker0/assets/screenshot-1.png">

  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📌</text></svg>">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="style.css">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "sticker0",
    "applicationCategory": "DeveloperApplication",
    "operatingSystem": "Linux, macOS, Windows",
    "description": "A mouse-first TUI sticky notes app for your terminal. Built with Python and Textual.",
    "url": "https://github.com/lee-do-jun/sticker0",
    "downloadUrl": "https://pypi.org/project/sticker0/",
    "softwareVersion": "0.5.0",
    "license": "https://opensource.org/licenses/MIT",
    "programmingLanguage": "Python",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }
  }
  </script>
</head>
<body>

  <!-- Background layers -->
  <div class="bg-grid"></div>
  <div class="ambient-aura"></div>
  <div class="cursor-glow"></div>

  <!-- Hero -->
  <section class="hero">
    <div class="reveal">
      <a class="hero-repo" href="https://github.com/lee-do-jun/sticker0" target="_blank" rel="noopener">
        lee-do-jun / sticker0
      </a>
      <h1>
        <span class="line typing-text" data-text="Sticky notes."></span>
        <span class="line typing-text accent" data-text="In your terminal." data-delay="800"></span>
      </h1>
      <p class="hero-subtitle">
        A mouse-first TUI app for sticky notes that live right in your terminal.
        Drag, resize, color, and organize — powered by Python + Textual.
      </p>
      <div class="cli-install">
        <span class="cli-prompt">❯</span>
        <code>uv tool install sticker0</code>
        <button onclick="copyInstall(this)">Copy</button>
      </div>
      <div>
        <a class="hero-cta" href="https://github.com/lee-do-jun/sticker0" target="_blank" rel="noopener">
          View on GitHub
        </a>
      </div>
    </div>
  </section>

  <!-- 01 // Preview -->
  <section class="section">
    <div class="container reveal">
      <span class="section-badge">01 // Preview</span>
      <h2 class="section-title">See it in action</h2>
      <p class="section-desc">
        Colorful sticky notes, right inside your terminal.
        Create, drag, resize, and organize with pure mouse interactions.
      </p>
      <div class="preview-container">
        <div class="preview-frame">
          <div class="preview-dots">
            <span></span><span></span><span></span>
          </div>
          <img src="assets/screenshot-1.png" alt="sticker0 running in a terminal — multiple colorful sticky notes on a dark board" loading="lazy" width="1920" height="1080">
        </div>
      </div>
    </div>
  </section>

  <!-- 02 // Features -->
  <section class="section">
    <div class="container reveal">
      <span class="section-badge">02 // Features</span>
      <h2 class="section-title">What it does</h2>
      <p class="section-desc">
        Everything you need for terminal-native note-taking. No keyboard shortcuts to memorize.
      </p>
      <div class="bento-grid">
        <div class="bento-box">
          <span class="bento-icon">🖱️</span>
          <h3>Mouse-First</h3>
          <p>Right-click context menus for everything. Create, delete, change colors — all from your mouse.</p>
        </div>
        <div class="bento-box">
          <span class="bento-icon">📌</span>
          <h3>Drag & Resize</h3>
          <p>Move stickers anywhere on the board. Resize from corners. Minimize with a double-click.</p>
        </div>
        <div class="bento-box">
          <span class="bento-icon">🎨</span>
          <h3>Themes & Colors</h3>
          <p>10+ sticker color presets and 6+ board themes built in. Add your own via config.</p>
        </div>
        <div class="bento-box">
          <span class="bento-icon">📁</span>
          <h3>Workspace Mode</h3>
          <p>Per-project sticker boards with <code>stk -w</code>. Each project keeps its own notes and theme.</p>
        </div>
        <div class="bento-box">
          <span class="bento-icon">💾</span>
          <h3>Auto-Save</h3>
          <p>Every edit saved instantly. Close and reopen — your notes are right where you left them.</p>
        </div>
        <div class="bento-box">
          <span class="bento-icon">📋</span>
          <h3>Clipboard</h3>
          <p>Copy sticker text, paste from clipboard, or create new stickers from clipboard content.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 03 // Get Started -->
  <section class="section">
    <div class="container reveal">
      <span class="section-badge">03 // Get Started</span>
      <h2 class="section-title">One command away</h2>
      <p class="section-desc">
        Install with uv or pip. Requires Python 3.11+.
      </p>
      <div class="install-terminal">
        <div class="term-header">
          <div class="term-dots">
            <span></span><span></span><span></span>
          </div>
          <span class="term-title">terminal</span>
        </div>
        <div class="term-body">
          <div class="term-line">
            <span class="term-prompt">❯</span>
            <span class="term-cmd">uv tool install sticker0</span>
          </div>
          <div class="term-output">Installed 1 package</div>
          <div class="term-line">
            <span class="term-prompt">❯</span>
            <span class="term-cmd">stk</span>
            <span class="term-comment"># launch</span>
          </div>
          <div class="term-line dim">
            <span class="term-prompt">❯</span>
            <span class="term-cmd">stk -w</span>
            <span class="term-comment"># workspace mode</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p>
        <a href="https://github.com/lee-do-jun/sticker0" target="_blank" rel="noopener">sticker0</a>
        · MIT License ·
        Built with <a href="https://textual.textualize.io/" target="_blank" rel="noopener">Textual</a>
      </p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

- [ ] **Step 2: 브라우저에서 확인**

```bash
open docs/index.html
```

Expected: 스타일 없는 상태로 모든 텍스트 콘텐츠가 올바르게 표시됨. 스크린샷 이미지 로드됨. 페이지 `<title>`이 "sticker0 — Terminal Sticky Notes"로 표시됨.

- [ ] **Step 3: 커밋**

```bash
git add docs/index.html
git commit -m "feat: complete HTML structure with SEO meta, OG tags, and JSON-LD"
```

---

### Task 3: CSS — Foundation & Background System

**Files:**
- Modify: `docs/style.css`

CSS 변수, 리셋, 타이포그래피, 3-레이어 배경 시스템(grid, aura, cursor glow), 스크롤 리빌 트랜지션을 작성한다.

- [ ] **Step 1: CSS 변수, 리셋, 배경 시스템 작성**

`docs/style.css`에 아래 내용 작성:

```css
/* === Variables === */
:root {
  --bg: #09090b;
  --bg-elevated: #18181b;
  --border: #27272a;
  --border-hover: #3f3f46;
  --text-primary: #fafafa;
  --text-secondary: #a1a1aa;
  --text-tertiary: #52525b;
  --accent: #f59e0b;
  --accent-glow: rgba(245, 158, 11, 0.15);
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}

/* === Reset === */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

::selection {
  background: var(--accent);
  color: var(--bg);
}

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text-primary);
  line-height: 1.6;
  overflow-x: hidden;
}

a {
  color: var(--accent);
  text-decoration: none;
  transition: color 0.2s;
}
a:hover { text-decoration: underline; }

code { font-family: var(--font-mono); }

img { max-width: 100%; height: auto; }

.container {
  max-width: 1040px;
  margin: 0 auto;
  padding: 0 24px;
}

/* === Background System (3 layers) === */
.bg-grid {
  position: fixed;
  inset: 0;
  z-index: -3;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse at 50% 50%, black 30%, transparent 80%);
  -webkit-mask-image: radial-gradient(ellipse at 50% 50%, black 30%, transparent 80%);
}

.ambient-aura {
  position: fixed;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 600px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
  z-index: -2;
  animation: breathe 12s ease-in-out infinite;
  pointer-events: none;
}

@keyframes breathe {
  0%, 100% { opacity: 0.4; transform: translateX(-50%) scale(1); }
  50% { opacity: 0.7; transform: translateX(-50%) scale(1.1); }
}

.cursor-glow {
  position: fixed;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
  z-index: -1;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s;
  mix-blend-mode: screen;
}

/* === Scroll Reveal === */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

- [ ] **Step 2: 브라우저에서 확인**

```bash
open docs/index.html
```

Expected: 다크 배경(#09090b). 희미한 그리드 패턴이 중앙에 비네트 형태로 보임. 상단에 앰버색 아우라가 부드럽게 호흡하듯 애니메이션됨. 텍스트가 보이지 않음(reveal이 아직 JS 없이 opacity:0 상태) — 이것은 정상.

- [ ] **Step 3: 커밋**

```bash
git add docs/style.css
git commit -m "style: CSS foundation — variables, reset, 3-layer background system"
```

---

### Task 4: CSS — Hero Section

**Files:**
- Modify: `docs/style.css` (append)

히어로 섹션 스타일: 풀스크린 중앙 정렬, 리포 배지, 타이핑 H1, 서브타이틀, CLI 설치 위젯, CTA 버튼.

- [ ] **Step 1: 히어로 CSS 추가**

`docs/style.css` 끝에 추가:

```css
/* === Hero === */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px 24px;
}

.hero-repo {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--text-secondary);
  border: 1px solid var(--border);
  padding: 6px 16px;
  border-radius: 100px;
  margin-bottom: 32px;
  transition: border-color 0.2s, color 0.2s;
}

.hero-repo:hover {
  border-color: var(--accent);
  color: var(--accent);
  text-decoration: none;
}

.hero h1 {
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  margin-bottom: 24px;
  min-height: 2.4em;
}

.hero h1 .line {
  display: block;
}

.hero h1 .accent {
  color: var(--accent);
}

.cursor-blink {
  color: var(--accent);
  animation: blink 1s step-end infinite;
  font-weight: 400;
}

@keyframes blink {
  50% { opacity: 0; }
}

.hero-subtitle {
  font-size: clamp(1rem, 2vw, 1.25rem);
  color: var(--text-secondary);
  max-width: 540px;
  margin: 0 auto 40px;
  line-height: 1.7;
}

.cli-install {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  margin-bottom: 24px;
}

.cli-prompt { color: var(--accent); }

.cli-install code { color: var(--text-primary); }

.cli-install button {
  background: var(--border);
  border: none;
  color: var(--text-secondary);
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  transition: background 0.2s, color 0.2s;
}

.cli-install button:hover {
  background: var(--accent);
  color: var(--bg);
}

.hero-cta {
  display: inline-block;
  padding: 12px 28px;
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text-primary);
  font-weight: 500;
  transition: border-color 0.2s, background 0.2s;
}

.hero-cta:hover {
  border-color: var(--accent);
  background: var(--accent-glow);
  text-decoration: none;
}
```

- [ ] **Step 2: 커밋**

```bash
git add docs/style.css
git commit -m "style: hero section — repo badge, title, CLI widget, CTA"
```

---

### Task 5: CSS — Sections, Preview, Bento Grid, Terminal, Footer

**Files:**
- Modify: `docs/style.css` (append)

나머지 섹션 전체를 한 번에 작성: 공통 섹션 스타일, 스크린샷 프리뷰 프레임, 벤토 그리드, 설치 터미널, 푸터.

- [ ] **Step 1: 섹션 공통 + 프리뷰 CSS 추가**

`docs/style.css` 끝에 추가:

```css
/* === Sections (shared) === */
.section {
  padding: 120px 0;
}

.section-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 16px;
}

.section-title {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 700;
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}

.section-desc {
  color: var(--text-secondary);
  font-size: 1.1rem;
  max-width: 600px;
  margin-bottom: 48px;
}

/* === Preview (Screenshot) === */
.preview-container {
  max-width: 900px;
  margin: 0 auto;
}

.preview-frame {
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  background: var(--bg-elevated);
  box-shadow: 0 0 80px var(--accent-glow);
}

.preview-dots {
  display: flex;
  gap: 6px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
}

.preview-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--border-hover);
}

.preview-frame img {
  width: 100%;
  display: block;
}
```

- [ ] **Step 2: 벤토 그리드 CSS 추가**

`docs/style.css` 끝에 추가:

```css
/* === Bento Grid === */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.bento-box {
  background: rgba(9, 9, 11, 0.95);
  padding: 32px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: background 0.3s;
}

.bento-box:hover {
  background: rgba(24, 24, 27, 0.95);
}

.bento-icon {
  font-size: 1.5rem;
  display: block;
  margin-bottom: 12px;
}

.bento-box h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 8px;
}

.bento-box p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.6;
}

.bento-box code {
  color: var(--accent);
  font-size: 0.85rem;
}
```

- [ ] **Step 3: 설치 터미널 + 푸터 CSS 추가**

`docs/style.css` 끝에 추가:

```css
/* === Install Terminal === */
.install-terminal {
  max-width: 600px;
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  background: rgba(255, 255, 255, 0.03);
}

.term-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
}

.term-dots {
  display: flex;
  gap: 6px;
}

.term-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--border-hover);
}

.term-title {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-tertiary);
}

.term-body {
  padding: 20px;
  font-family: var(--font-mono);
  font-size: 0.9rem;
}

.term-line {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
  align-items: baseline;
}

.term-line:last-child { margin-bottom: 0; }

.term-prompt { color: var(--accent); }

.term-cmd { color: var(--text-primary); }

.term-comment {
  color: var(--text-tertiary);
  font-size: 0.8rem;
}

.term-output {
  color: var(--text-tertiary);
  font-size: 0.85rem;
  margin-bottom: 8px;
  padding-left: 20px;
}

.term-line.dim { opacity: 0.6; }

/* === Footer === */
footer {
  border-top: 1px solid var(--border);
  padding: 40px 0;
  text-align: center;
  color: var(--text-tertiary);
  font-size: 0.85rem;
}

footer a { color: var(--text-secondary); }
footer a:hover { color: var(--accent); }
```

- [ ] **Step 4: 브라우저에서 확인**

```bash
open docs/index.html
```

Expected: 다크 배경에 전체 레이아웃이 표시됨. 히어로는 아직 숨겨진 상태(reveal JS 필요). 하지만 DevTools에서 `.reveal` 요소에 수동으로 `visible` 클래스를 추가하면 스타일이 올바르게 적용됨을 확인 가능:
- 히어로: 중앙 정렬, 리포 배지(라운드 pill), CLI 위젯(글래스모피즘), CTA 버튼
- 스크린샷: 윈도우 프레임(점 3개) 안에 이미지, 앰버색 글로우
- 벤토 그리드: 3열, 1px 보더 구분, 호버 시 약간 밝아짐
- 터미널: 윈도우 프레임, 프롬프트 색상(앰버), 커맨드
- 푸터: 상단 보더, 중앙 정렬 텍스트

- [ ] **Step 5: 커밋**

```bash
git add docs/style.css
git commit -m "style: preview frame, bento grid, install terminal, footer"
```

---

### Task 6: CSS — Responsive Design

**Files:**
- Modify: `docs/style.css` (append)

모바일/태블릿 반응형 처리.

- [ ] **Step 1: 반응형 미디어 쿼리 추가**

`docs/style.css` 끝에 추가:

```css
/* === Responsive === */
@media (max-width: 768px) {
  .bento-grid {
    grid-template-columns: 1fr;
  }

  .hero h1 {
    font-size: clamp(2.2rem, 10vw, 3.5rem);
    min-height: 3em;
  }

  .section {
    padding: 80px 0;
  }

  .cli-install {
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
    font-size: 0.85rem;
  }

  .section-desc {
    font-size: 1rem;
  }

  .term-body {
    font-size: 0.8rem;
    padding: 16px;
  }
}

@media (max-width: 480px) {
  .hero h1 {
    font-size: 2rem;
  }

  .bento-box {
    padding: 24px;
  }

  .container {
    padding: 0 16px;
  }
}

@media (hover: none) {
  .cursor-glow { display: none; }
}
```

마지막 `@media (hover: none)` 규칙은 터치 디바이스에서 커서 글로우를 숨긴다.

- [ ] **Step 2: DevTools 반응형 모드로 확인**

브라우저 DevTools → 반응형 디자인 모드 → iPhone SE(375px), iPad(768px) 크기에서 확인.

Expected:
- 375px: 벤토가 1열, 히어로 타이틀 2rem, 패딩 축소
- 768px: 벤토가 1열, 섹션 패딩 80px

- [ ] **Step 3: 커밋**

```bash
git add docs/style.css
git commit -m "style: responsive design — mobile and tablet breakpoints"
```

---

### Task 7: JavaScript — Interactions & Animations

**Files:**
- Modify: `docs/script.js`

커서 글로우 트래킹, IntersectionObserver 스크롤 리빌, 타이핑 효과, 클립보드 복사 기능.

- [ ] **Step 1: script.js 전체 작성**

`docs/script.js` 내용:

```javascript
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
```

**주요 결정:**
- IIFE로 전역 스코프 오염 방지 (`copyInstall`만 `window`에 노출)
- `IntersectionObserver` 미지원 시 폴백으로 즉시 `visible` 추가
- `navigator.clipboard` 미지원 시 `document.execCommand('copy')` 폴백
- Promise chain으로 타이핑 순서 보장

- [ ] **Step 2: 브라우저에서 전체 기능 확인**

```bash
open docs/index.html
```

Expected:
1. 히어로가 자동으로 보임(IntersectionObserver reveal)
2. "Sticky notes."가 한 글자씩 타이핑됨 → 800ms 후 "In your terminal."이 타이핑됨
3. 마우스 이동 시 앰버색 글로우가 커서를 따라다님
4. 스크롤 시 각 섹션이 아래에서 위로 페이드인
5. CLI 위젯의 "Copy" 버튼 클릭 → "Copied!" 표시 → 2초 후 "Copy"로 복원 → 클립보드에 `uv tool install sticker0` 복사됨

- [ ] **Step 3: 커밋**

```bash
git add docs/script.js
git commit -m "feat: JS interactions — cursor glow, scroll reveal, typing effect, clipboard"
```

---

### Task 8: Final Verification & Cleanup

**Files:**
- Review: `docs/index.html`, `docs/style.css`, `docs/script.js`

전체 페이지 최종 검증.

- [ ] **Step 1: 로컬 HTTP 서버로 확인**

`file://` 프로토콜에서는 일부 기능(clipboard API)이 동작하지 않을 수 있으므로 HTTP 서버로 확인:

```bash
cd docs && python3 -m http.server 8000
```

브라우저에서 `http://localhost:8000` 접속.

**체크리스트:**
- [ ] 다크 배경 + 그리드 패턴 + 앰버 아우라 호흡 애니메이션
- [ ] 커서 글로우가 마우스 따라다님
- [ ] 히어로 타이핑 효과 ("Sticky notes." → "In your terminal.")
- [ ] 리포 배지 호버 시 앰버색 전환
- [ ] CLI Copy 버튼 동작 → 클립보드 확인
- [ ] CTA "View on GitHub" 클릭 시 새 탭에서 깃헙 열림
- [ ] 스크롤 시 각 섹션 페이드인
- [ ] 스크린샷 이미지가 프레임 안에 표시됨
- [ ] 벤토 그리드 3열, 호버 시 밝아짐
- [ ] 터미널 위젯 표시
- [ ] 푸터 링크 동작
- [ ] DevTools → 모바일 뷰 (375px) 확인
- [ ] View Source → `<title>`, `<meta>`, OG 태그, JSON-LD 정상

- [ ] **Step 2: HTML 유효성 검증**

```bash
# W3C validator로 검증 (온라인: https://validator.w3.org/#validate_by_input)
# 로컬에서는 내용을 복사해서 붙여넣기
```

- [ ] **Step 3: Lighthouse SEO 체크**

DevTools → Lighthouse → SEO 카테고리 실행.

Expected: SEO 점수 90+ (meta description, OG tags, canonical, JSON-LD 모두 포함)

- [ ] **Step 4: 최종 커밋**

```bash
git add docs/
git commit -m "docs: sticker0 landing page — dark terminal aesthetic, 4 sections, SEO"
```

---

## Summary

| Task | 설명 | 예상 파일 |
|------|------|-----------|
| 1 | Project Scaffold | dirs, screenshot copy |
| 2 | HTML + SEO | `index.html` |
| 3 | CSS Foundation + Background | `style.css` |
| 4 | CSS Hero | `style.css` |
| 5 | CSS Sections/Preview/Bento/Terminal/Footer | `style.css` |
| 6 | CSS Responsive | `style.css` |
| 7 | JavaScript Interactions | `script.js` |
| 8 | Final Verification | all files |

총 8개 태스크, 약 25개 스텝. 예상 소요: 45-60분.
