import numpy as np

data = np.array([[1, 2], 
                 [3, 4], 
                 [5, 6]])

# 조건에 맞는 boolean 배열 생성
bool_mask = data > 3
print("Boolean 마스크:\n", bool_mask)
# [[False False]
#  [False  True]
#  [ True  True]]

# 마스크를 사용해 True 위치의 값만 추출 (1차원 배열로 반환됨)
print("\n3보다 큰 값들:", data[bool_mask]) # 출력: [4 5 6]

# 조건을 직접 인덱스에 넣어도 동일하게 동작합니다.
print("짝수만 추출:", data[data % 2 == 0]) # 출력: [2 4 6]

raw_data = np.array([15.5, -99, 42.0, 150.3, 10.1, 85.2, -5, 200.0])
print(f"1. 원본 데이터: {raw_data}")

# 0보다 큰 정상 데이터만 추출 (정제)
cleaned_data = raw_data[raw_data > 0]
print(f"2. 음수 에러 제거 후: {cleaned_data}")

# 100을 넘는 위험 수치는 100으로 고정 (보정)
cleaned_data[cleaned_data > 100] = 100.0
print(f"3. 이상치(100초과) 보정 후: {cleaned_data}")

# 예를 들어, 50보다 큰 데이터는 '위험 물체', 50 이하는 '안전 물체'라고 정의한다면?
danger_objects = cleaned_data[cleaned_data > 50]
safe_objects = cleaned_data[cleaned_data <= 50]

print(f"4. 위험 물체 데이터만 추출: {danger_objects}")
print(f"5. 안전 물체 데이터만 추출: {safe_objects}")
