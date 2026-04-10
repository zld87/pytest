def zld_2_1_1():
    import pandas as pd
    # 加载数据集并显示数据集的前五行 1分
    file = 'file/2.1.1/auto-mpg.csv'
    data = pd.read_csv(file)
    print(data.shape)
    # print(data['model year'])
    # print('.....a')
    # print(data[['model year']])

    print("数据集的前五行:")
    print(data.head())

    # 显示每一列的数据类型
    print(data.dtypes)
    print('显示每一列的数据类型。。。。。。')
    # 检查缺失值并删除缺失值所在的行  2分
    print(data.isnull().sum())
    # 删除缺失值
    data = data.dropna()
    # print(data.isnull().sum())
    # print(type(data))
    print('已删除缺失值所在行。。。。。。')

    # 将 'horsepower' 列转换为数值类型，并处理转换中的异常值 1分
    data['horsepower'] = pd.to_numeric(data['horsepower'], errors='coerce')
    data = data.dropna(subset=['horsepower'])
    print(data)

    # 显示每一列的数据类型
    print(data.horsepower.dtypes)
    print('显示每一列的数据类型。。。。。。')

    # 检查清洗后的缺失值
    print(data.isnull().sum())
    print('检查清洗后的缺失值。。。。。。')


    # 对数值型数据进行标准化处理
    from sklearn.preprocessing import StandardScaler
    numerical_features = ['displacement', 'horsepower', 'weight', 'acceleration']
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    # print(data[numerical_features])
    print('对数值型数据进行标准化处理')


    # 选择特征，创建自变量与目标变量得2分
    from sklearn.model_selection import train_test_split
    selected_features = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year',
                         'origin']  # 特征==自变量
    X = data[selected_features]
    y = data['mpg']  # 目标变量==因变量
    # print(X)
    # 划分数据集为训练集与测试集得1分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(y_test)

    # 将特征和目标变量合并到一个数据框中
    cleaned_data = X.copy()
    cleaned_data['mpg'] = y
    # print(cleaned_data)
    # 保存清洗和处理后的数据得1分
    # cleaned_data.to_csv('file/2.1.1/2.1.1_cleaned_data.csv', index=False)



def zld_2_1_2():
    import pandas as pd
    # 数据集正确加载得1分
    data = pd.read_excel(f'file/2.1.2/大学生低碳生活行为的影响因素数据集.xlsx')
    # print(data.head(10))

    # 删除缺失值所在行正确得1分，获取处理前和处理后的数据行数正确得1分，总计得2分；
    # 显示文件的行列总数
    print(data.shape)
    initial_row_count = data.shape[0]
    # 删除缺失值
    data = data.dropna()
    final_row_count = data.shape[0]
    print(f'处理前的数据行数{initial_row_count},处理后数据行数: {final_row_count}, 删除的行数: {initial_row_count - final_row_count}')

    # 删除重复数据得1分
    data = data.drop_duplicates()
    print('删除重复行之后的行数')
    print(data.shape)

    # 数据标准化处理得1分
    from sklearn.preprocessing import StandardScaler
    numerical_features = ['4.您的月生活费○≦1,000元   ○1,001-2,000元   ○2,001-3,000元   ○≧3,001元']
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(X=data[numerical_features])
    print(data[numerical_features])

    # 选择特征变量和目标变量得2分
    from sklearn.model_selection import train_test_split
    selected_features = [
        '1.您的性别○男性   ○女性',
        '2.您的年级○大一   ○大二   ○大三   ○大四',
        '3.您的生源地○农村   ○城镇（乡镇）   ○地县级城市  ○省会城市及直辖市',
        '4.您的月生活费○≦1,000元   ○1,001-2,000元   ○2,001-3,000元   ○≧3,001元',
        '5.您进行过绿色低碳的相关生活方式吗?',
        '6.您觉得“低碳”，与你的生活关系密切吗？',
        '7.低碳生活是否会成为未来的主流生活方式？',
        '8.您是否认为低碳生活会提高您的生活质量？'
    ]
    X = data[selected_features]
    y = data['低碳行为积极性']
    # 划分数据集为训练集与测试集得1分
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 合并与保存处理后的数据得2分
    # 方式一
    # cleaned_data1 = X.copy()
    # cleaned_data1['低碳行为积极性'] = y
    # cleaned_data1.to_csv('file/2.1.2/2.1.2_cleaned_data1.csv', index=False)
    # print(cleaned_data1)
    # 方式二
    cleaned_data = pd.concat([X, y], axis=1)
    print(cleaned_data)

    # cleaned_data.to_csv('file/2.1.2/2.1.2_cleaned_data.csv', index=False)



def zld_2_1_3():
    import pandas as pd
    # 数据集正确加载并显示前五行得1分
    data = pd.read_csv('file/2.1.3/finance数据集.csv')
    print(data.head())
    print(data.dtypes)

    import matplotlib.pyplot as plt
    import seaborn as sns
    # 设置图像尺寸
    plt.figure(figsize=(8, 4))

    # 识别数值列用于箱线图
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    print(numeric_cols)

    # 创建箱线图
    for i, col in enumerate(numeric_cols, 1):
        print(i, col)
        # plt.subplot(3, 4, i)
        # sns.boxplot(x=data[col])
        # plt.title(col)

    plt.tight_layout()
    # plt.show()

    # 使用IQR处理异常值得2分
    # 处理异常值
    Q1 = data[numeric_cols].quantile(0.25)
    Q3 = data[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1
    # # print(data[numeric_cols])
    print(IQR)
    # print(Q3)
    # print(Q3 + 1.5 * IQR)
    # 移除异常值
    print(~((data[numeric_cols] < (Q1 - 1.5 * IQR)) | (data[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1))
    print(data[numeric_cols])


    # 移除异常值
    data_cleaned = data[
        ~((data[numeric_cols] < (Q1 - 1.5 * IQR)) | (data[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)
    ]

    print(data_cleaned)

    # 处理重复值得1分
    # 检查重复值
    duplicates = data_cleaned.duplicated()
    print('检查重复值')
    print(duplicates)
    num_duplicates = duplicates.sum()
    data_cleaned = data_cleaned[~duplicates]
    print(f'删除的重复行数: {num_duplicates}')
    print(data_cleaned)

    # 对数据进行归一化处理得1分；
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data_cleaned[numeric_cols] = scaler.fit_transform(X=data_cleaned[numeric_cols])

    # 设置目标变量得1分
    target_variable = 'SeriousDlqin2yrs'
    # 定义特征和目标得2分
    X = data_cleaned.drop(columns=[target_variable])
    y = data_cleaned[target_variable]
    # print(X)

    # 划分数据集为训练集与测试集得1分
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # 显示划分后的数据形状
    print(f'训练数据形状: {X_train.shape}')
    print(f'测试数据形状: {X_test.shape}')

    # 保存清洗后得数据得1分
    cleaned_file_path = 'file/2.1.3/2.1.3_cleaned_data.csv'
    # data_cleaned.to_csv(cleaned_file_path, index=False)



def zld_2_1_4():
    import pandas as pd
    # 加载数据集并指定编码为gbk正确得1分, 查看表结构基本信息正确得1分
    data = pd.read_csv('file/2.1.4/medical_data.csv', encoding='gbk')
    # print(data.head())
    # 查看数据类型和表结构
    print(data.dtypes)
    # 查看表结构基本信息正确得1分
    print('表结构基本信息')
    print(data.info())
    # 显示每一列的空缺值数量
    print('显示每一列的空缺值数量')
    print(data.isnull().sum())

    # 规范日期格式
    data['就诊日期'] = pd.to_datetime(data['就诊日期'])
    data['诊断日期'] = pd.to_datetime(data['诊断日期'])
    # 修改列名正确得1分
    data.rename(columns={'病人ID': '患者ID'}, inplace=True)
    # 查看修改后的表结构
    print(data.head())

    from datetime import datetime
    # 增加诊断延迟和病程列得1分
    # print(data['诊断日期'])
    # print(data['就诊日期'])
    data['诊断延迟'] = (data['诊断日期'] - data['就诊日期']).dt.days
    data['病程'] = (datetime(2024, 9, 1) - data['诊断日期']).dt.days
    # print(data['诊断延迟'])
    # print(data['病程'])

    # 删除不合理数据得1分
    data = data[(data['诊断延迟'] >= 0) & (data['年龄'] > 0) & (data['年龄'] < 120)]
    # print((data['诊断延迟'] >= 0) & (data['年龄'] > 0) & (data['年龄'] < 120))

    # 查看修改后的数据
    print('查看修改后的数据')
    print(data.describe())

    # 删除重复值并记录删除的行数
    initial_rows = data.shape[0]
    # print(initial_rows)
    data.drop_duplicates(inplace=True)
    # print(data.shape[0])
    deleted_rows = initial_rows - data.shape[0]
    print(f'删除的重复行数: {deleted_rows}')

    # 归一化处理得1分
    from sklearn.preprocessing import MinMaxScaler
    columns_to_normalize = ['年龄', '体重', '身高']
    scaler = MinMaxScaler()
    data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])
    # 查看归一化后的数据
    print(data.head())

    # 统计不同疾病类型的治疗结果分布，并画出柱状图
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    # 统计治疗结果分布
    print('统计治疗结果分布')
    treatment_outcome_distribution = data.groupby('疾病类型')['治疗结果'].value_counts().unstack()
    print(treatment_outcome_distribution)

    # 设置中文字体
    font_path = 'ttf/SFNSItalic.ttf'  # 根据你的系统调整字体路径
    my_font = fm.FontProperties(fname=font_path)

    # 绘制柱状图正确得1分
    treatment_outcome_distribution.plot(kind='bar', stacked=True)
    plt.title('不同疾病类型的治疗结果分布', fontproperties=my_font)
    plt.xlabel('疾病类型', fontproperties=my_font)
    plt.ylabel('治疗结果数量', fontproperties=my_font)
    plt.xticks(rotation=45, fontproperties=my_font)
    plt.legend(prop=my_font)
    plt.tight_layout()
    # plt.show()

    # 分析年龄和疾病严重程度的关系，绘制出散点图
    plt.scatter(data['年龄'], data['疾病严重程度'])
    plt.title('年龄和疾病严重程度的关系', fontproperties=my_font)
    plt.xlabel('年龄', fontproperties=my_font)
    plt.ylabel('疾病严重程度', fontproperties=my_font)
    plt.xticks(fontproperties=my_font)  # 设置x轴刻度标签的字体
    plt.yticks(fontproperties=my_font)  # 设置y轴刻度标签的字体
    plt.legend(prop=my_font)  # 设置图例字体
    # plt.show()

    # 保存处理后得数据得1分
    output_path = 'file/2.1.4/2.1.4_cleaned_data.csv'
    # data.to_csv(output_path, index=False)



def zld_2_1_5():
    import pandas as pd
    # 加载数据集得1分
    data = pd.read_csv('file/2.1.5/健康咨询客户数据集.csv')
    # 查看表结构基本信息得1分
    print(data.info())
    # 显示每一列的空缺值数量得1分
    print('显示每一列的空缺值数量')
    print(data.isnull().sum())

    # 删除含有缺失值的行
    data_cleaned = data.dropna()
    # print('.....')
    # print(data_cleaned.loc[:, 'How important is exercise to you ?'])
    # print('.....')
    # 转换 'Your age' 列的数据类型为整数类型，并处理异常值得1分
    data_cleaned.loc[:, 'Your age'] = pd.to_numeric(data_cleaned['Your age'], errors='coerce')
    print(data_cleaned[['Your age']])
    data_cleaned = data_cleaned.dropna(subset=['Your age'])
    data_cleaned = data_cleaned[data_cleaned['Your age'] >= 0]
    data_cleaned.loc[:, 'Your age'] = data_cleaned['Your age'].astype(int)

    print(data_cleaned['Your age'].dtype)

    # 检查和删除重复值得1分
    duplicates_removed = data_cleaned.duplicated().sum()
    data_cleaned = data_cleaned.drop_duplicates()
    print(f"Removed {duplicates_removed} duplicate rows")

    # 数据归一化处理得1分
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    data_cleaned['How do you describe your current level of fitness ?'] = \
        label_encoder.fit_transform(data_cleaned['How do you describe your current level of fitness ?'])

    print(data_cleaned['How do you describe your current level of fitness ?'].unique())

    from sklearn.preprocessing import LabelEncoder
    import matplotlib.pyplot as plt

    # 去掉列名中的空格
    data.columns = data.columns.str.strip()
    # 显示数据集的列名
    print(data.columns)

    # 删除包含缺失值的行
    data_cleaned = data.dropna(subset=['How often do you exercise?'])
    # 统计不同健身频率的分布情况
    exercise_frequency_counts = data_cleaned['How often do you exercise?'].value_counts()
    print(exercise_frequency_counts)

    # 绘制饼图得1分
    plt.figure(figsize=(10, 6))
    exercise_frequency_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Exercise Frequency')
    plt.ylabel('')
    plt.show()

    import pandas as pd
    from sklearn.model_selection import train_test_split
    import matplotlib.pyplot as plt

    # 填充缺失值
    data_filled = data.apply(lambda x: x.fillna(x.mode()[0]))
    print('填充值')
    print(data_filled)
    # 划分数据（测试集占比20%)
    train_data, test_data = train_test_split(data_filled, test_size=0.2, random_state=42)

    # 保存处理后的数据
    cleaned_file_path = 'file/2.1.5/2.1.5_cleaned_data.csv'
    data_filled.to_csv(cleaned_file_path, index=False)







# zld_2_1_1()
# zld_2_1_2()
# zld_2_1_3()
# zld_2_1_4()
zld_2_1_5()

