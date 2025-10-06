def solution(today, terms, privacies):
    n_year, n_month, n_day = map(int, today.split('.'))
    term_splited = [term.split() for term in terms]
    terms_dict = {term[0]: 28*int(term[1]) - 1 for term in term_splited}
    
    result = []
    for i, privacy in enumerate(privacies):
        when, what = privacy.split()
        year, month, day = map(int, when.split('.'))
        
        # 날짜 계산
        day += terms_dict[what]
        month_added, day = divmod(day, 28)
        if day == 0:
            day = 28
            month_added -= 1
        month += month_added
        year_added, month = divmod(month, 12)
        if month == 0:
            month = 12
            year_added -= 1
        year += year_added
        # print(f"now: {n_year}.{n_month}.{n_day}")
        # print(f"til: {year}.{month}.{day}")
        # 여부 확인
        if n_year > year:
            result.append(i+1)
        elif n_year == year:
            if n_month > month:
                result.append(i+1)
            elif n_month == month:
                if n_day > day:
                    result.append(i+1)
    
    return result