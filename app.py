import streamlit as st

# 1. 리스트 및 데이터 구조 정의 (문화권, 국가 목록, 주문 표현 데이터)
regions = ["1. 아시아", "2. 유럽", "3. 영미"]

countries_by_region = {
    "1. 아시아": ["일본", "중국"],
    "2. 유럽": ["프랑스", "독일"],
    "3. 영미": ["영국", "미국"]
}

# 각 국가별 주문 표현 리스트 (현지어, 발음, 한국어 해석)
order_phrases = {
    "일본": [
        ("すみません、注文をお願いします。", "스미마센, 츄-몬오 오네가이시마스.", "저기요, 주문 부탁합니다."),
        ("おすすめは何ですか？", "오스스메와 난데스카?", "추천 메뉴는 무엇인가요?"),
        ("お会計をお願いします。", "오카이케-오 오네가이시마스.", "계산 부탁드립니다.")
    ],
    "중국": [
        ("服务员，点菜！", "푸우위안, 디엔차이!", "종업원, 주문할게요!"),
        ("有什么推荐的菜吗？", "요우 션머 투이지엔 더 차이 마?", "추천할 만한 요리가 있나요?"),
        ("买单！", "마이단!", "계산할게요!")
    ],
    "프랑스": [
        ("S'il vous plaît, je voudrais commander.", "실 부 플레, 쥬 부드레 코망데.", "실례합니다, 주문하고 싶습니다."),
        ("Qu'est-ce que vous recommandez ?", "께스끄 부 흐꼬망데?", "무엇을 추천하시나요?"),
        ("L'addition, s'il vous plaît.", "라디시옹, 실 부 플레.", "계산서 좀 부탁드립니다.")
    ],
    "독일": [
        ("Entschuldigung, ich möchte bestellen.", "엔슐디궁, 이히 뫼히테 베슈텔렌.", "실례합니다, 주문하고 싶습니다."),
        ("Was können Sie empfehlen?", "바스 쾨넨 지 엠펠렌?", "무엇을 추천해 주실 수 있나요?"),
        ("Die Rechnung, bitte.", "디 레히눙, 비테.", "계산서 부탁합니다.")
    ],
    "영국": [
        ("Excuse me, could we order please?", "익스큐즈 미, 쿠드 위 오더 플리즈?", "실례합니다, 주문해도 될까요?"),
        ("What would you recommend?", "왓 우드 유 레커멘드?", "무엇을 추천하시겠어요?"),
        ("Could we have the bill, please?", "쿠드 위 해브 더 빌, 플리즈?", "계산서 좀 주시겠어요?")
    ],
    "미국": [
        ("Hi, can we place an order?", "하이, 캔 위 플레이스 언 오더?", "안녕하세요, 주문할 수 있을까요?"),
        ("What's good here?", "왓츠 굿 히어?", "여기 뭐가 맛있나요?"),
        ("Can we get the check, please?", "캔 위 겟 더 체크, 플리즈?", "계산서 좀 갖다 주시겠어요?")
    ]
}

# 2. 함수 정의: 선택한 국가의 주문 표현을 화면에 출력하는 함수
def display_phrases(country):
    st.subheader(f"🍽️ {country}의 음식 주문 표현 가이드")
    
    # 조건문: 해당 국가의 데이터가 있는지 확인
    if country in order_phrases:
        phrases = order_phrases[country]
        
        # 반복문: 리스트에 담긴 표현들을 하나씩 꺼내어 출력
        for idx, (local_lang, pronunciation, korean) in enumerate(phrases, start=1):
            with st.container(border=True):
                st.markdown(f"**표현 {idx}.**")
                st.markdown(f"🗣️ **현지어:** `{local_lang}`")
                st.markdown(f"🔊 **발음:** {pronunciation}")
                st.markdown(f"🇰🇷 **해석:** {korean}")
    else:
        st.error("해당 국가의 표현 데이터가 없습니다.")

# 3. 메인 웹 앱 UI 구성 함수
def main():
    st.set_page_config(page_title="문화권별 음식 주문 가이드", page_icon="🌍")
    st.title("🌍 문화권별 음식 주문 표현 가이드")
    st.write("여행 가고 싶은 문화권 번호를 입력하고, 국가를 선택해 현지 주문 표현을 배워보세요!")
    
    st.divider()
    
    # 문화권 목록 안내 (반복문 활용)
    st.markdown("### 1단계: 문화권 번호 입력")
    cols = st.columns(3)
    for i, region in enumerate(regions):
        cols[i].info(region)
        
    # 사용자 입력 (번호 선택)
    region_num = st.number_input("문화권 번호를 입력하세요 (1: 아시아, 2: 유럽, 3: 영미)", min_value=1, max_value=3, step=1)
    
    # 조건문: 입력된 번호에 따라 문화권 및 국가 리스트 매핑
    selected_region = ""
    if region_num == 1:
        selected_region = "1. 아시아"
    elif region_num == 2:
        selected_region = "2. 유럽"
    elif region_num == 3:
        selected_region = "3. 영미"
        
    # 해당 문화권의 국가 두 개 가져오기 (리스트)
    available_countries = countries_by_region[selected_region]
    
    st.divider()
    st.markdown(f"### 2단계: 국가 선택 ({selected_region})")
    st.write(f"선택 가능한 국가: **{available_countries[0]}**, **{available_countries[1]}**")
    
    # 라디오 버튼으로 국가 선택
    selected_country = st.radio("표현을 확인할 국가를 선택하세요:", available_countries, horizontal=True)
    
    st.divider()
    
    # 함수 호출하여 결과 출력
    display_phrases(selected_country)

if __name__ == "__main__":
    main() 
