import streamlit as st
from shops import SHOPS

st.set_page_config(
    page_title="ShopeeAI",
    page_icon="🛍️",
    layout="wide"
)

# ================= Sidebar =================

st.sidebar.title("🛍️ ShopeeAI")

menu = st.sidebar.radio(
    "Chọn chức năng",
    [
        "🏠 Dashboard",
        "🛒 Shopee",
        "🎵 TikTok",
        "🟦 Facebook",
        "🟧 Lazada",
        "📦 Kho",
        "🤖 AI",
        "⚙️ Cài đặt"
    ]
)

# ================= Dashboard =================

if menu == "🏠 Dashboard":

    st.title("🛍️ ShopeeAI Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Shopee", len(SHOPS["Shopee"]))
    c2.metric("TikTok", len(SHOPS["TikTok"]))
    c3.metric("Lazada", len(SHOPS["Lazada"]))

    st.divider()

    st.subheader("🏪 Danh sách cửa hàng")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🛒 Shopee")
        for shop in SHOPS["Shopee"]:
            st.write("•", shop)

    with col2:
        st.markdown("### 🎵 TikTok")
        for shop in SHOPS["TikTok"]:
            st.write("•", shop)

    with col3:
        st.markdown("### 🟧 Lazada")
        for shop in SHOPS["Lazada"]:
            st.write("•", shop)

# ================= Shopee =================

elif menu == "🛒 Shopee":

    st.title("🛒 Quản lý Shopee")

    shop = st.selectbox(
        "Chọn Shop",
        SHOPS["Shopee"]
    )

    st.success(f"Đang quản lý: {shop}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📦 Đơn hàng",
        "🛍️ Sản phẩm",
        "📢 Quảng cáo",
        "💬 Chat",
        "📈 Doanh thu"
    ])

    with tab1:
        st.subheader("📦 Đơn hàng")
        st.info("Chưa kết nối Shopee API")

    with tab2:
        st.subheader("🛍️ Sản phẩm")
        st.info("Chưa kết nối Shopee API")

    with tab3:
        st.subheader("📢 Quảng cáo")
        st.info("Chưa kết nối Shopee Ads API")

    with tab4:
        st.subheader("💬 Chat khách hàng")
        st.info("Chưa kết nối Shopee Chat")

    with tab5:
        st.subheader("📈 Doanh thu")

        c1, c2, c3 = st.columns(3)

        c1.metric("Doanh thu hôm nay", "0 đ")
        c2.metric("Đơn hàng", "0")
        c3.metric("Lợi nhuận", "0 đ")

# ================= TikTok =================

elif menu == "🎵 TikTok":

    st.title("🎵 TikTok Shop")

    shop = st.selectbox(
        "Chọn Shop TikTok",
        SHOPS["TikTok"]
    )

    st.success(f"Đang quản lý: {shop}")

# ================= Facebook =================

elif menu == "🟦 Facebook":

    st.title("🟦 Facebook")

    st.info("Đang phát triển")

# ================= Lazada =================

elif menu == "🟧 Lazada":

    st.title("🟧 Lazada")

    shop = st.selectbox(
        "Chọn Shop Lazada",
        SHOPS["Lazada"]
    )

    st.success(f"Đang quản lý: {shop}")
# ================= Kho =================

elif menu == "📦 Kho":

    st.title("📦 Quản lý Kho")

    st.info("Đang phát triển")

# ================= AI =================

elif menu == "🤖 AI":

    st.title("🤖 AI Assistant")

    question = st.text_area("Nhập yêu cầu")

    if st.button("Gửi"):
        st.success("AI sẽ trả lời ở đây trong phiên bản tiếp theo.")

# ================= Cài đặt =================

elif menu == "⚙️ Cài đặt":

    st.title("⚙️ Cài đặt")

    st.checkbox("Bật chế độ quản trị")

    st.checkbox("Hiển thị thống kê")

    st.checkbox("Thông báo đơn hàng")

    st.checkbox("Tự động đồng bộ dữ liệu")