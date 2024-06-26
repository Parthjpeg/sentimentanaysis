from attr import has
import streamlit as st
from helper import *


def app():

    st.set_page_config(
        page_title="Social Dashboard",
        page_icon="icon.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.header("Social Media Analytics Dashboard")

    function_option = "Twitter"#st.sidebar.selectbox("Select the platform: ",["Twitter", "Facebook", "Instagram"] )

    if function_option == "Twitter":
        # st.image('banner.png')
        #st.sidebar.checkbox("Include retweets")
        
        st.write(" ")
        st.write(" ")
        st.write(" ")
        word_query = st.text_input("Enter a Tweet to check semtiment", placeholder="Data")
        print(word_query)
        # st.write(" ")
        # number_of_tweets = st.slider("How many tweets would you like to analyse {}".format(word_query), min_value=100, max_value=10000)
        # st.info("1 Tweets takes approx 0.05 sec so you may have to wait 5 seconds for 100 Tweets.")

        if st.button("Analyse Sentiment"):

            data = preprocessing_data(word_query)
            analyse = graph_sentiment(data)
            # mention = analyse_mention(data)
            # hastag = analyse_hastag(data)

            st.write(" ")
            st.write(" ")
            st.header("Extracted and Preprocessed Dataset")
            st.write(data)
            #download_data(data, label="twitter_sentiment_filtered")
            st.write(" ")

            col1, col2, col3 = st.columns(3)
            with col2:
                st.markdown("## Analysis of the Data")


            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("{} is the Subjectivity of this tweet".format(data["Subjectivity"]))
            with col2:
                st.markdown("{} is the Polarity of this tweet".format(data["Polarity"]))
            with col3:
                st.markdown("This tweet has a {} Sentiment".format(data["Analysis"]))
            
            # col3, col4 = st.columns(2)
            # with col3:
            #     st.text("Top 10 Used Links for {} tweets".format(number_of_tweets))
            #     st.bar_chart(data["links"].value_counts().head(10).reset_index())

            # with col4:
            #     st.text("All the Tweets that containes top 10 links used")
            #     filtered_data = data[data["links"].isin(data["links"].value_counts().head(10).reset_index()["index"].values)]
            #     st.write(filtered_data)

            # st.subheader("Twitter Sentment Analysis")
            # st.bar_chart(analyse)

    else: st.header("Coming Soon")

if __name__ == '__main__':
    app()   
