import pandas as pd
a = {
    'huynya': [1, 2, 3]
}

b = pd.DataFrame(a['huynya'], columns=['huynya'])
print(b)