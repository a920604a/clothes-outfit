import streamlit as st
from db_conn import query_clothes


# Streamlit應用程序
def main():
    st.title("衣服篩選器")

    st.sidebar.header("篩選條件")
    color = st.sidebar.text_input("顏色", "")
    sex = st.sidebar.selectbox(
        "性別", [0, 1], format_func=lambda x: "男" if x == 0 else "女"
    )

    if st.sidebar.button("篩選"):
        if color and sex is not None:
            df = query_clothes(color, sex)
            if not df.empty:
                st.write(f"找到 {len(df)} 件衣服")
                for index, row in df.iterrows():
                    st.image(row["image_url"], caption=row["category"])
                    st.write(f"分類: {row['category']}")
                    st.write(f"顏色: {row['color']}")
                    st.write(f"[查看詳細]({row['post_url']})")
                    st.write("---")
            else:
                st.write("未找到匹配的衣服")
        else:
            st.write("請輸入顏色並選擇性別")


if __name__ == "__main__":
    main()
