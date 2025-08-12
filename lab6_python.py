import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pet Store", layout="wide")
products = [
    {"name": "Dog Food Pedigree", "price": 60.00, "img": "data:image/jpeg;base64,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", "stock": 50},
    {"name": "Cat Bed", "price": 200.00, "img": "https://m.media-amazon.com/images/I/619RYcukVUL._UF350,350_QL80_.jpg","stock": 30},
    {"name": "Hamster Cage", "price": 240.00, "img": "https://m.media-amazon.com/images/I/81q2XtkbeKL.jpg", "stock": 20}
]

if "cart" not in st.session_state:
    st.session_state.cart = {p["name"]: 0 for p in products}
if "stock" not in st.session_state:
    st.session_state.stock = {p["name"]: p["stock"] for p in products}
if "feedback" not in st.session_state:
    st.session_state.feedback = []  

page = st.sidebar.radio("Navigation", ["Shop", "Analytics", "Feedback"])
if page == "Shop":
    st.title(" Pet Store Inventory")

    for product in products:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(product["img"], width=250)
        with col2:
            st.subheader(product["name"])
            st.write(f" Price: **Rs{product['price']}**")
            st.write(f"Stock Available: **{st.session_state.stock[product['name']]}**")
            
            qty = st.number_input(
                f"Quantity for {product['name']}",
                min_value=0,
                max_value=st.session_state.stock[product['name']],
                value=0,
                key=product["name"]
            )
            
            if st.button(f"Add {product['name']} to Cart"):
                if qty > 0:
                    st.session_state.cart[product["name"]] += qty
                    st.session_state.stock[product["name"]] -= qty
                    st.success(f"Added {qty} x {product['name']} to cart!")
                else:
                    st.warning("Please select at least 1 quantity.")

    st.subheader("Cart Summary")
    total = sum(products[i]["price"] * qty for i, qty in enumerate(st.session_state.cart.values()))
    st.write(f"**Total: Rs{total:.2f}**")
    if st.button("Checkout"):
        st.success("Order placed successfully!")
        st.balloons()

elif page == "Analytics":
    st.title("Sales & Stock Analytics")
    cart_data = pd.DataFrame({
        "Product": [p["name"] for p in products],
        "Quantity Sold": list(st.session_state.cart.values()),
        "Remaining Stock": list(st.session_state.stock.values()),
        "Revenue": [products[i]["price"] * qty for i, qty in enumerate(st.session_state.cart.values())]
    })
    st.write("**Current Sales Data:**")
    st.dataframe(cart_data)
    st.subheader("Remaining Stock per Product")
    st.bar_chart(cart_data.set_index("Product")["Remaining Stock"])
    st.subheader("Quantity Sold per Product")
    st.bar_chart(cart_data.set_index("Product")["Quantity Sold"])
    st.subheader("Revenue per Product")
    st.bar_chart(cart_data.set_index("Product")["Revenue"])

elif page == "Feedback":
    st.title("Customer Feedback")
    st.write("We value your feedback! Please rate and share your thoughts.")
    rating = st.slider("Rate your shopping experience:", 1, 5, 3)
    comment = st.text_area("Your feedback:")
    if st.button("Submit Feedback"):
        if comment.strip():
            st.session_state.feedback.append({"rating": rating, "comment": comment})
            st.success(" Thank you for your feedback!")
        else:
            st.warning("Please enter a comment before submitting.")
    
    if st.session_state.feedback:
        st.subheader(" Feedback Summary")
        feedback_df = pd.DataFrame(st.session_state.feedback)
        st.write(feedback_df)
        st.bar_chart(feedback_df["rating"].value_counts().sort_index())

