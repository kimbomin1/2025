import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "연구원"],
    "ENTP": ["기업가", "마케팅 기획자", "벤처 창업가"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "ENFP": ["광고 기획자", "교사", "스타트업 운영자"],
    "ISTJ": ["회계사", "법무사", "공무원"],
    "ESFP": ["배우", "이벤트 플래너", "홍보 담당자"],
    # 필요하면 더 추가 가능
}

st.title("🔎 MBTI 기반 진로 추천 웹앱")
st.write("당신의 MBTI를 선택하면 적절한 직업을 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=list(mbti_jobs.keys())
)

if mbti:
    st.subheader(f"✅ {mbti} 유형에 어울리는 직업 추천")
    jobs = mbti_jobs.get(mbti, [])
    for job in jobs:
        st.write(f"- {job}")

