## 功能：基本計算器

### 情境：正整數相加
- Given 兩個正整數 a=2, b=3
- When 呼叫 add(a, b)
- Then 回傳 5

### 情境：負整數相加
- Given 兩個負整數 a=-1, b=-5
- When 呼叫 add(a, b)
- Then 回傳 -6

### 情境：正整數相減
- Given a=5, b=2
- When 呼叫 subtract(a, b)
- Then 回傳 3

### 情境：正整數相除
- Given a=10, b=2
- When 呼叫 divide(a, b)
- Then 回傳 5.0

### 情境：除以零
- Given a=5, b=0
- When 呼叫 divide(a, b)
- Then 拋出 ZeroDivisionError

### 情境：abs_diff 正整數
- Given a=5, b=3
- When 呼叫 abs_diff(a, b)
- Then 回傳 2

### 情境：abs_diff 相同數字
- Given a=7, b=7
- When 呼叫 abs_diff(a, b)
- Then 回傳 0

### 情境：abs_diff 含負數（此 Then 故意未寫測試）
- Given a=-5, b=3
- When 呼叫 abs_diff(a, b)
- Then 回傳 8（因為 |-5-3| = 8）

### 情境：abs_diff 順序對稱（此 Then 故意未寫測試）
- Given a=3, b=-5
- When 呼叫 abs_diff(a, b)
- Then 回傳 8（因為 |3-(-5)| = 8，結果應與上一情境相同）
