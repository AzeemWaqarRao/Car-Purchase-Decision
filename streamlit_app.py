import streamlit as st 
import pickle

model = pickle.load(open('model.pkl', 'rb'))


def main():
    st.title("Car Purchase Decision")
    st.markdown("This model classifies whether a person will buy a car or not")

    gender = st.selectbox("Gender" , ['Male', 'Female'])
    age = st.number_input("Age")
    salary = st.number_input("Anuual Salary")

    if gender == "Male":
        gender = 1
    else:
        gender = 0

    if st.button("submit"):
        result = model.predict([[age,salary,gender]])
        if result:
            out = "Person will buy the car"
        else:
            out = "Person will not buy the car"
        st.success(out)





if __name__ == "__main__":
    main()