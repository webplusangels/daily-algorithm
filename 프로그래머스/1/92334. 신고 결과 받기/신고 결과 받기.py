from collections import defaultdict

def solution(id_list, report, k):
    report_to = defaultdict(int)
    reported = defaultdict(set)
    
    report = set(report) # 중복 제거
    for r in report:
        frm, to = r.split()
        reported[frm].add(to)
        report_to[to] += 1
    
    suspended = set()
    for id_, K in report_to.items():
        if K >= k:
            suspended.add(id_)
            
    result_dict = {id_: 0 for id_ in id_list}
    for id_, ids in reported.items():
        succed = ids & suspended
        if succed:
            result_dict[id_] += len(succed)
    
    answer = [id_ for id_ in result_dict.values()]
    return answer