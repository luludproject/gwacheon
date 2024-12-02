import pandas as pd
from itertools import product

list1 = ["과천","관문동", "문원동", "갈현동", "막계동", "과천동", "주암동", "중앙동", "원문동", "별양동", "부림동"]

list2 = ["변기막힘", "변기뚫는업체", "변기수리", "싱크대막힘", "하수구막힘", "변기뚫음"]


# 모든 조합 생성
all_combinations = list(product(list1, list2))

# 3개씩 묶어서 새로운 조합 생성
chunk_size = 2
result_combinations = [', '.join(f'{combo[0]}{combo[1]}' for combo in all_combinations[i:i+chunk_size]) for i in range(0, len(all_combinations), chunk_size)]

# 데이터 생성
data = {'Keyword': result_combinations}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임을 엑셀 파일로 저장
excel_file = '하수구_과천시.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'키워드 조합이 {excel_file} 파일로 저장되었습니다.')