import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 페이지 기본 설정
st.set_page_config(
    page_title="뚱냥이 키우기",
    page_icon="🐱",
    layout="centered"
)

# 페이지 제목 및 간단한 소개
st.title("🐱 뚱냥이 키우기 웹앱")
st.write("나만의 고양이를 건강하고 포동포동하게 키워보세요! 아래 화면에서 바로 시작할 수 있습니다.")

# index.html 파일 경로 설정
html_file_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 파일 존재 여부 확인 후 렌더링
if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 렌더링 (앱이 잘 보이도록 충분한 높이를 지정합니다)
    components.html(html_content, height=850, scrolling=True)
else:
    # 파일이 없을 경우 친절한 안내 메시지 출력
    st.error("앗! 화면을 불러올 수 없어요. 😿")
    st.warning(f"'{html_file_path}' 경로에 파일이 올바르게 있는지 확인해 주세요.")
