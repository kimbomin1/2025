# -*- coding: utf-8 -*-
# Streamlit Zodiac Info App
# 파일명: app.py

import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(
    page_title="✨ 별자리 안내", page_icon="✨", layout="wide"
)

# ---------------------- 커스텀 CSS ----------------------
CUSTOM_CSS = """
<style>
.stApp {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  color: #EEE;
}
.main-title {
  font-size: 42px; font-weight: 800;
  background: linear-gradient(90deg, #FFD166, #F4978E, #9B5DE5, #4CC9F0);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.card {
  background: rgba(255,255,255,0.08);
  border-radius: 16px; padding: 18px; margin-bottom: 16px;
  text-align: center;
}
.big-emoji { font-size: 64px; display: block; margin-bottom: 10px; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------- 별자리 데이터 ----------------------
ZODIAC_INFO = [
    ("🐐", "염소자리", "12/22 ~ 1/19", ["책임감", "성실함", "목표지향"]),
    ("🌊", "물병자리", "1/20 ~ 2/18", ["독창적", "자유로움", "진보적"]),
    ("🐟", "물고기자리", "2/19 ~ 3/20", ["감수성", "상상력", "희생정신"]),
    ("🐏", "양자리", "3/21 ~ 4/19", ["도전적", "열정적", "리더십"]),
    ("🐂", "황소자리", "4/20 ~ 5/20", ["끈기", "안정", "실용적"]),
    ("👯", "쌍둥이자리", "5/21 ~ 6/21", ["호기심", "사교적", "재치"]),
    ("🦀", "게자리", "6/22 ~ 7/22", ["가족애", "보호적", "감성적"]),
    ("🦁", "사자자리", "7/23 ~ 8/22", ["자신감", "창의적", "카리스마"]),
    ("🌿", "처녀자리", "8/23 ~ 9/23", ["분석적", "세심함", "실용적"]),
    ("⚖️", "천칭자리", "9/24 ~ 10/22", ["조화", "사교성", "균형감"]),
    ("🦂", "전갈자리", "10/23 ~ 11/22", ["열정", "집중력", "비밀스러움"]),
    ("🏹", "사수자리", "11/23 ~ 12/21", ["자유", "탐험", "낙관적"]),
]

# ---------------------- 메인 화면 ----------------------
st.markdown("<h1 class='main-title'>✨ 별자리 안내 ✨</h1>", unsafe_allow_html=True)
st.write("자신의 별자리를 선택하고, 날짜와 특징을 확인하세요!")

for emoji, name, date_range, traits in ZODIAC_INFO:
    with st.container():
        st.markdown(f"""
        <div class='card'>
            <span class='big-emoji'>{emoji}</span>
            <h3>{name}</h3>
            <p><b>생일:</b> {date_range}</p>
            <p><b>특징:</b> {', '.join(traits)}</p>
        </div>
        """, unsafe_allow_html=True)

