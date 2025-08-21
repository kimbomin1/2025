import streamlit as st

# ----------------------------
# MBTI별 직업 추천 데이터
# ----------------------------
mbti_jobs = {
    "INTJ": ["🧠 데이터 사이언티스트", "📊 전략 컨설턴트", "🔬 연구원"],
    "ENTP": ["🚀 기업가", "📢 마케팅 기획자", "💡 벤처 창업가"],
    "INFJ": ["💬 상담가", "✍️ 작가", "🧘 심리학자"],
    "ENFP": ["🎭 광고 기획자", "👩‍🏫 교사", "🌱 스타트업 운영자"],
    "ISTJ": ["📑 회계사", "⚖️ 법무사", "🏛️ 공무원"],
    "ESFP": ["🎤 배우", "🎉 이벤트 플래너", "📺 홍보 담당자"],
    "ENTJ": ["💼 CEO", "📈 경영 컨설턴트", "🦾 프로젝트 매니저"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎶 음악가"]
}

# ----------------------------
# 앱 레이아웃
# ----------------------------
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="wide")

st.title("🌈 MBTI 기반 진로 추천 웹앱")
st.markdown("당신의 성격 유형에 맞는 멋진 직업을 찾아보세요! 💼✨")

# MBTI 선택 박스
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요!",
    options=list(mbti_jobs.keys())
)

# ----------------------------
# 직업 추천 출력
# ----------------------------
if mbti:
    st.markdown(f"### 🌟 {mbti} 유형에 어울리는 직업 추천 🔮")

    jobs = mbti_jobs.get(mbti, [])

    # 3열 카드 레이아웃
    cols = st.columns(3)
    for i, job in enumerate(jobs):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background-color:#fef6e4;
                            padding:20px;
                            margin:10px;
                            border-radius:20px;
                            box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
                            text-align:center;
                            font-size:20px;">
                    {job}
                </div>
                """,
                unsafe_allow_html=True
            )

# ----------------------------
# 푸터
# ----------------------------
st.markdown("---")
st.markdown("✨ Made with ❤️ using Streamlit ✨")
