# 数据字段列表（去除重复）
fields = list(set([
    "fnd17_oxlcxspebq", "fnd17_shsoutbs", "fnd28_value_05191q", "fnd28_value_05192q", "fnd28_value_05301q",
    "fnd28_value_05302", "fnd17_pehigh", "fnd17_pelow", "fnd17_priceavg150day", "fnd17_priceavg200day",
    "fnd17_priceavg50day", "fnd17_pxedra", "fnd17_tbea", "fnd28_newa3_value_18191a", "fnd28_newa3_value_18198a",
    "fnd28_value_02300a", "mdl175_ebitda", "mdl175_pain"
]))

# 初始化一个计数器
combination_count = 0

# 遍历所有可能的字段对
for i in range(len(fields)):
    for j in range(i + 1, len(fields)):  # 保证A和B不同
        A = fields[i]
        B = fields[j]
        # 输出生成的Alpha表达式
        alpha_expr = f"ts_regression(ts_zscore({A}, 500), ts_zscore({B}, 500), 500)"
        print(alpha_expr)
        combination_count += 1

# 输出总组合数
print(f"Total combinations: {combination_count}")

