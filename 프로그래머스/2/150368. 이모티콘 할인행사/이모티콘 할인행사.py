from itertools import product

def solution(users, emoticons):
    # users: [이모티콘 사는 할인율, 구매 비용 임계점 넘으면-> 이모티콘 플러스]
    # 1. 이모티콘 플러스 가입자 늘리기 2. 그 중에서 판매액이 최대
    # 10, 20, 30, 40% 할인율 존재
    
    m_cnt = m_paid = 0
    emoPrice = [[(10, round(n*.9)), (20, round(n*.8)), (30, round(n*.7)), (40, round(n*.6))] for n in emoticons]
    
    for prod in product(*emoPrice):         # 이모티콘 가격 조합
        cnt = paid = 0                      # 이모티콘 플러스 가입할 사람 & 번 돈
        for user in users:                  # 사용자마다 확인            
            # 임계 할인율 넘기면 장바구니에 넣기
            bag = sum([p[1] for p in prod if p[0] >= user[0]])
            if bag >= user[1]:              # 장바구니 가격이 임계 가격을 넘으면
                cnt += 1                    # 가입!
            else:
                paid += bag                 # 가입 안하고 그냥 삼
        
        if cnt > m_cnt:
            m_cnt = cnt
            m_paid = paid
        elif cnt == m_cnt and paid > m_paid:
            m_paid = paid
    
    return [m_cnt, m_paid]