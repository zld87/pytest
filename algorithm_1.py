import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE


# 加载数据得1分
data = pd.read_csv('file/2.2.1/finance数据集.csv')

# 显示前五行的数据得1分
print(data.head())

# 选择自变量和因变量
X = data.drop(['SeriousDlqin2yrs', 'Unnamed: 0'], axis=1)
"y = data['SeriousDlqin2yrs']\n",
"\n",
"# 分割训练集和测试集（测试集20%）\n",
"X_train, X_test, y_train, y_test = __________(__________, random_state=42)\n",
"\n",
"# 训练Logistic回归模型（最大迭代次数为1000次）\n",
"model = __________\n",
"#训练 Logistic 回归模型\n",
"__________\n",
"\n",
"# 保存模型\n",
"with open('2.2.1_model.pkl', 'wb') as file:\n",
"    pickle.__________\n",
"\n",
"# 预测并保存结果\n",
"y_pred = __________\n",
"pd.DataFrame(y_pred, columns=['预测结果']).to_csv('2.2.1_results.txt', index=False)\n",
"\n",
"# 生成测试报告\n",
"report = classification_report(y_test, y_pred, zero_division=1)\n",
"with open('2.2.1_report.txt', 'w') as file:\n",
"    file.write(report)\n",
"\n",
"# 分析测试结果\n",
"accuracy = __________\n",
"print(f\"模型准确率: {accuracy:.2f}\")\n",
"\n",
"# 处理数据不平衡\n",
"smote = SMOTE(random_state=42)\n",
"X_resampled, y_resampled = __________\n",
"\n",
"# 重新训练模型\n",
"__________\n",
"# 重新预测\n",
"y_pred_resampled = __________\n",
"\n",
"# 保存新结果\n",
"pd.DataFrame(y_pred_resampled, columns=['预测结果']).to_csv('2.2.1_results_xg.txt', index=False)\n",
"\n",
"# 生成新的测试报告\n",
"report_resampled = classification_report(y_test, y_pred_resampled, zero_division=1)\n",
"with open('2.2.1_report_xg.txt', 'w') as file:\n",
"    file.write(report_resampled)\n",
"\n",
"# 分析新的测试结果\n",
"accuracy_resampled = __________\n",
"print(f\"重新采样后的模型准确率: {accuracy_resampled:.2f}\")\n"