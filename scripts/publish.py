#!/usr/bin/env python3
"""
자동 포스팅 스크립트 - Today's English Word Puzzles
사용법: python publish.py --title "제목" --game "Bonza" --content "내용"
또는: 스크래핑 스크립트에서 import하여 사용
"""

import subprocess
import os
from datetime import datetime
from pathlib import Path

# 블로그 레포지토리 로컬 경로 (본인 환경에 맞게 수정)
BLOG_DIR = Path(__file__).parent.parent


def create_post(title: str, content: str, game: str = "", 
                tags: list = None, english_tip: str = "", 
                date: str = None):
    """
    마크다운 포스트를 생성하고 git push합니다.
    
    Args:
        title: 포스트 제목
        content: 포스트 본문 (마크다운 형식)
        game: 게임 이름 (Bonza, Crossover, Waywords, Keysmash)
        tags: 태그 리스트
        english_tip: 영어 학습 팁
        date: 날짜 (기본: 오늘, 형식: YYYY-MM-DD)
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    if tags is None:
        tags = [game, "Netflix", "영어단어"] if game else ["영어단어"]
    
    # 파일명 생성 (한글 제거, 슬러그화)
    slug = title.lower()
    slug = slug.replace(" ", "-")
    # 영문/숫자/하이픈만 유지
    slug = "".join(c for c in slug if c.isalnum() or c == "-")
    slug = slug.strip("-")
    
    if not slug:
        slug = f"{game.lower()}-{date}" if game else f"post-{date}"
    
    filename = f"{date}-{slug}.md"
    filepath = BLOG_DIR / "_posts" / filename
    
    # Front matter 생성
    tags_str = ", ".join(tags)
    frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
game: "{game}"
tags: [{tags_str}]
english_tip: "{english_tip}"
---

{content}
"""
    
    # 파일 쓰기
    filepath.write_text(frontmatter, encoding="utf-8")
    print(f"✅ 포스트 생성: {filepath}")
    
    return filepath


def git_push(message: str = None):
    """생성된 포스트를 git push합니다."""
    os.chdir(BLOG_DIR)
    
    if message is None:
        message = f"Add post: {datetime.now().strftime('%Y-%m-%d')}"
    
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Git push 완료! 잠시 후 블로그에 반영됩니다.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 오류: {e}")


def publish_post(title: str, content: str, game: str = "", 
                 tags: list = None, english_tip: str = "",
                 auto_push: bool = True):
    """포스트 생성 + git push를 한번에 처리합니다."""
    filepath = create_post(title, content, game, tags, english_tip)
    
    if auto_push:
        git_push(f"Add post: {title}")
    
    return filepath


# ===== 사용 예시 =====
if __name__ == "__main__":
    # 예시: Bonza 포스트 발행
    publish_post(
        title="Bonza 정답 (2026년 2월 12일) - 테마: Food",
        game="Bonza",
        tags=["Bonza", "Netflix", "영어단어", "Food"],
        english_tip="'Cuisine'은 특정 나라나 지역의 요리 스타일을 뜻합니다.",
        content="""## 오늘의 Bonza 퍼즐

**테마: Food** 🍕

## 정답

| 단어 | 뜻 |
|------|-----|
| **CUISINE** | 요리법, 요리 |
| **RECIPE** | 조리법, 레시피 |
| **INGREDIENT** | 재료, 성분 |
| **SEASONING** | 양념, 조미료 |

## 핵심 단어 학습

### CUISINE
- **발음:** /kwɪˈziːn/
- **뜻:** (특정 나라·지역의) 요리
- **예문:** "Korean cuisine is famous for its bold flavors and fermented dishes."
""",
        auto_push=False  # 테스트시 False로 설정
    )
