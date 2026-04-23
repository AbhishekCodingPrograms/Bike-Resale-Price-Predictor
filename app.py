import pickle
import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bike Price Predictor", page_icon="🏍️")

dic_img = {
    "Royal Enfield": './images/Royal Enfield.jpg',
    "Bajaj":         './images/bajaj.jpg',
    "Hero":          './images/Hero.jpg',
    "Honda":         './images/Honda.png',
    "KTM":           './images/KTM.jpg',
    "Other":         './images/Other.jpg',
    "Suzuki":        './images/Suzuki.jpg',
    "TVS":           './images/TVS.png',
    "Yamaha":        './images/yamaha.png'
}

# ── Auto-train if pkl files are missing (e.g. first run on Streamlit Cloud) ──
@st.cache_resource(show_spinner="Training model for first time… this takes ~60s ☕")
def load_model():
    if os.path.exists('bike_predictor_rf.pkl') and os.path.exists('search.pkl'):
        with open('bike_predictor_rf.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('search.pkl', 'rb') as sf:
            search_txt = pickle.load(sf)
        return model, search_txt

    # If pkl files don't exist, retrain from CSV
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.ensemble import RandomForestRegressor

    df = pd.read_csv('Used_Bikes.csv')

    list_city = df['city'].value_counts()[:23].index
    df['city'] = df['city'].apply(lambda x: x if x in list_city else 'Other')

    major_brands = ['Bajaj', 'Hero', 'Royal Enfield', 'Yamaha',
                    'Honda', 'Suzuki', 'TVS', 'KTM']
    df['brand'] = df['brand'].apply(lambda x: x if x in major_brands else 'Other')
    df.dropna(inplace=True)

    X = df[['brand', 'kms_driven', 'power', 'age', 'city']]
    y = df['price']

    search_txt = {
        'brand': sorted(X['brand'].unique().tolist()),
        'city':  sorted(X['city'].unique().tolist())
    }

    preprocessor = ColumnTransformer(transformers=[
        ('ohe',    OneHotEncoder(handle_unknown='ignore', sparse_output=False), ['brand', 'city']),
        ('scaler', StandardScaler(), ['kms_driven', 'power', 'age'])
    ])

    model = Pipeline(steps=[
        ('trf1', preprocessor),
        ('rf',   RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
    ])
    model.fit(X, y)

    with open('bike_predictor_rf.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('search.pkl', 'wb') as sf:
        pickle.dump(search_txt, sf)

    return model, search_txt


model, search_txt = load_model()

# ── UI ────────────────────────────────────────────────────────────────────────
st.title('Bike Price Predictor! 🏍️')
st.write("###### Created By [Abhishek Maurya](https://github.com/AbhishekCodingPrograms), "
         "[Source Code](https://github.com/AbhishekCodingPrograms/Bike-Resale-Price-Predictor)")

brand      = st.sidebar.selectbox("Brand Name",        search_txt['brand'])
kms_driven = st.sidebar.number_input('Kms Driven',     value=6100)
power      = st.sidebar.number_input("Power (CC)",     value=350)
age        = st.sidebar.number_input('Age (years)',     value=3)
city       = st.sidebar.selectbox('City',              search_txt['city'])

if st.sidebar.button("Predict Bike Price"):
    with st.container():
        img_col, txt_col = st.columns((1, 2))
        with img_col:
            st.image(dic_img[brand], width=200)
        with txt_col:
            st.write(f"#### {brand}")
            st.write(f"**Kms Driven:** {kms_driven:,}")
            st.write(f"**Power:** {power} CC")
            st.write(f"**Age:** {age} year(s)")
            st.write(f"**City:** {city}")

    input_df = pd.DataFrame([{
        'brand':      brand,
        'kms_driven': float(kms_driven),
        'power':      float(power),
        'age':        float(age),
        'city':       city
    }])
    y_pred = model.predict(input_df)
    st.success(f"### Estimated Resale Price: ₹ {round(y_pred[0], 2):,.2f}")
