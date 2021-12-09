import pandas as pd 

catering_sale = 'data/catering_sale.xls' #餐饮数据
data = pd.read_excel(catering_sale, index_col='日期') #读取数据，制定“日期”列为索引列
# 过滤异常数据
data = data[(data['销量'] > 400) & (data['销量'] < 5000)]
# 保存基本统计量
statistics = data.describe()

# 极差
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
# 变异函数
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
# 四分位数间距
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

print(statistics)