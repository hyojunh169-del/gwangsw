import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 1. 스트림릿 페이지 기본 설정
st.set_page_config(
    page_title="뚱냥이 키우기 극악 버전",
    page_icon="🐱",
    layout="centered"
)

# 2. 페이지 상단 타이틀 및 설명 표시
st.title("🐱 뚱냥이 키우기 서비스")
st.write("진화와 돌연사의 갈림길! 당신의 뚱냥이를 1톤(t) 이상의 '강승우'로 무사히 진화시켜 보세요.")

# 3. 프로젝트 폴더 구조에 따른 상대 경로 설정
html_file_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 4. 파일 존재 여부 확인 후 브라우저에 렌더링
if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML/CSS/JS가 포함된 index.html 내용을 안전하게 렌더링
    components.html(html_content, height=850, scrolling=True)
else:
    # 파일을 찾을 수 없을 때 출력하는 친절한 한국어 경고 메시지
    st.error("앗! 게임 화면을 불러올 수 없습니다. 😿")
    st.warning(f"현재 지정된 위치에 파일이 있는지 확인해 주세요.\n경로: `{html_file_path}`")
