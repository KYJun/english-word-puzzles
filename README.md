# 🧩 Today's English Word Puzzles

매일 업데이트되는 영어 단어 퍼즐 정답과 영어 학습 팁 블로그

## 🚀 GitHub Pages 세팅 방법

### 1단계: GitHub 레포지토리 생성

1. GitHub에서 **New Repository** 클릭
2. Repository name: `english-word-puzzles`
3. **Public** 선택
4. **Create repository** 클릭

### 2단계: 파일 업로드

```bash
# 이 폴더를 클론한 레포에 복사 후
cd english-word-puzzles
git init
git remote add origin https://github.com/YOUR_USERNAME/english-word-puzzles.git
git add .
git commit -m "Initial blog setup"
git push -u origin main
```

### 3단계: GitHub Pages 활성화

1. GitHub 레포지토리 → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `/ (root)` 선택
4. **Save** 클릭
5. 약 1~2분 후 `https://YOUR_USERNAME.github.io/english-word-puzzles/` 에서 확인

### 4단계: (선택) 커스텀 도메인 연결

1. Settings → Pages → Custom domain에 도메인 입력
2. DNS 설정에서 CNAME 레코드 추가

---

## 📝 글 작성 방법

### 수동 작성

`_posts/` 폴더에 `YYYY-MM-DD-제목.md` 형식으로 파일 생성:

```markdown
---
layout: post
title: "Bonza 정답 (2026년 2월 12일) - 테마: Food"
date: 2026-02-12
game: "Bonza"
tags: [Bonza, Netflix, 영어단어]
english_tip: "오늘의 영어 학습 팁"
---

포스트 내용을 마크다운으로 작성...
```

### 자동 발행 (Python 스크립트)

```python
from scripts.publish import publish_post

publish_post(
    title="Bonza 정답 (2026년 2월 12일) - 테마: Food",
    game="Bonza",
    tags=["Bonza", "Netflix", "영어단어", "Food"],
    english_tip="학습 팁",
    content="## 오늘의 퍼즐\n\n내용..."
)
```

---

## 📁 프로젝트 구조

```
english-word-puzzles/
├── _config.yml          # Jekyll 설정
├── _layouts/            # 레이아웃 템플릿
│   ├── default.html     # 기본 레이아웃
│   ├── home.html        # 홈페이지
│   ├── post.html        # 개별 포스트
│   └── page.html        # 일반 페이지
├── _includes/           # 공통 컴포넌트
│   ├── header.html
│   └── footer.html
├── _posts/              # 블로그 포스트 (여기에 글 추가)
├── _pages/              # 정적 페이지
├── assets/css/          # 스타일시트
├── scripts/             # 자동화 스크립트
│   └── publish.py       # 자동 포스팅
├── index.md             # 홈페이지
├── Gemfile              # Ruby 의존성
└── README.md
```

## ⚙️ 자동화 파이프라인 (향후)

```
스크래핑 (FandomWire) → LLM 글 생성 → publish.py → git push → 자동 발행
```
