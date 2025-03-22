import streamlit as st

# 初始化
st.title("🎬 电影版《思想辩证区域》测试")
st.markdown("请直觉作答，每题选一个最认同的选项。")

questions = {
    1: {
        "question": "你要策划一场电影展，你会选择哪个主题？",
        "options": {
            "A": ("“时代的呐喊”", {"女权": 1, "开放": 1}),
            "B": ("“银河彼岸”", {"先锋": 1, "硬核影迷": 1}),
            "C": ("“现实的重量”", {"开放": 1, "独立": 1}),
            "D": ("“光影遗产”", {"经典": 1, "保守": 1})
        }
    },
    # ... 添加所有15题
}

scores = {}

for qid, content in questions.items():
    choice = st.radio(content["question"], list(content["options"].keys()), key=qid)
    for dim, val in content["options"][choice][1].items():
        scores[dim] = scores.get(dim, 0) + val

# 展示结果
if st.button("提交并查看结果"):
    st.subheader("🧠 你的电影人格特质分布")
    st.write(scores)
