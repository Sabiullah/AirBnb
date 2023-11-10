import pymongo
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import os
from PIL import Image
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="AirBnb-Analysis!!!", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart:   AirBnb-Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

mongodb_uri = "mongodb+srv://Safy:1234@cluster0.4w8kary.mongodb.net/"  # Replace with your MongoDB Atlas URI

client = pymongo.MongoClient(mongodb_uri)

# Access the database and collection
db = client['AirBnb']
collection = db['airbnb']


# Query data from MongoDB and convert to DataFrame
data = list(collection.find())
df = pd.DataFrame(data)
# Select all columns in the DataFrame
pd.set_option('display.max_columns', None)
# print(df)


# Display the DataFrame
# st.write(df.head(10))

SELECT = option_menu(
    menu_title=None,
    options=["Home", "Explore Data"],
    icons=["house", "bar-chart"],
    default_index=1,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white", "size": "cover", "width": "100"},
            "icon": {"color": "black", "font-size": "20px"},

            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"}
            })

df.rename(columns={'borough': 'neighbourhood_group'}, inplace=True)

#----------------Home----------------------#

if SELECT == "Home":

 st.header('Airbnb Analysis')
 st.subheader("Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.")
 st.subheader('Skills take away From This Project:')
 st.subheader('Python Scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau')
 st.subheader('Domain:')
 st.subheader('Travel Industry, Property management and Tourism')
 # st.write(df.head(5))



 #-------------EXPLORE DATA---------------#



if SELECT == "Explore Data":


    neighbourhood_group = st.sidebar.multiselect("Pick your neighbourhood_group", df["neighbourhood_group"].unique())
    if not neighbourhood_group:
        df2 = df.copy()
    else:
        df2 = df[df["neighbourhood_group"].isin(neighbourhood_group)]

    # Create for neighbourhood
    neighbourhood = st.sidebar.multiselect("Pick the neighbourhood", df2["neighbourhood"].unique())
    if not neighbourhood:
        df3 = df2.copy()
    else:
        df3 = df2[df2["neighbourhood"].isin(neighbourhood)]

    # Filter the data based on neighbourhood_group, neighbourhood


    if not neighbourhood_group and not neighbourhood:
        filtered_df = df
    elif not neighbourhood:
        filtered_df = df[df["neighbourhood_group"].isin(neighbourhood_group)]
    elif not neighbourhood_group:
        filtered_df = df[df["neighbourhood"].isin(neighbourhood)]
    elif neighbourhood:
        filtered_df = df3[df["neighbourhood"].isin(neighbourhood)]
    elif neighbourhood_group:
        filtered_df = df3[df["neighbourhood_group"].isin(neighbourhood_group)]
    elif neighbourhood_group and neighbourhood:
        filtered_df = df3[
            df["neighbourhood_group"].isin(neighbourhood_group) & df3["neighbourhood"].isin(neighbourhood)]
    else:
        filtered_df = df3[
            df3["neighbourhood_group"].isin(neighbourhood_group) & df3["neighbourhood"].isin(neighbourhood)]

    room_type_df = filtered_df.groupby(by=["room_type"], as_index=False)["price"].sum()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Room Type wise Details")
        fig = px.bar(room_type_df, x="room_type", y="price", text=['${:,.2f}'.format(x) for x in room_type_df["price"]],
                     template="seaborn")
        st.plotly_chart(fig, use_container_width=True, height=200)

    with col2:
        st.subheader("Neighbourhood wise Comparison")
        fig = px.pie(filtered_df, values="price", names="neighbourhood_group", hole=0.5)
        fig.update_traces(text=filtered_df["neighbourhood_group"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    # Create a scatter plot for rating vs neighborhood
    # filtered_df['rating'] = filtered_df['rating'].mean().round(1)
    grouped_df = df.groupby(['neighbourhood','neighbourhood_group'])['rating'].mean().reset_index()

    # Sort the DataFrame by 'rating' in descending order
    grouped_df = grouped_df.sort_values(by='rating', ascending=False)

    data1 = px.line(grouped_df, y="rating", x="neighbourhood", color="neighbourhood_group")
    data1['layout'].update(
        title="Rating wise Neighbourhood details using Line Plot.",
        titlefont=dict(size=20), xaxis=dict(title="Neighbourhood", titlefont=dict(size=20)),
        yaxis=dict(title="Rating", titlefont=dict(size=20)))
    st.plotly_chart(data1, use_container_width=True)

    cl1, cl2 = st.columns((2))

    with cl1:
        with st.expander("room_type wise Average Price"):
            room_type_df = filtered_df.groupby(by=["room_type"], as_index=False)["price"].mean()
            st.write(room_type_df.style.background_gradient(cmap="Blues").format({"price": "{:.2f}"}))
            csv = room_type_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="room_type.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')

    with cl2:
        with st.expander("neighbourhood_group wise Average Price"):
            neighbourhood_group = filtered_df.groupby(by="neighbourhood_group", as_index=False)["price"].mean()
            # neighbourhood_group["price"] = neighbourhood_group["price"].round(2)
            st.write(neighbourhood_group.style.background_gradient(cmap="Oranges").format({"price": "{:.2f}"}))
            csv = neighbourhood_group.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="neighbourhood_group.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')

    # Create a scatter plot
    data1 = px.scatter(filtered_df, x="neighbourhood_group", y="neighbourhood", color="room_type")
    data1['layout'].update(title="Room Type vs Neighbourhood Group.",
                           titlefont=dict(size=20), xaxis=dict(title="Neighbourhood_Group", titlefont=dict(size=20)),
                           yaxis=dict(title="Neighbourhood", titlefont=dict(size=20)))
    st.plotly_chart(data1, use_container_width=True)

    with st.expander("Detailed Room Availability and Price View Data in the Neighbourhood"):
        st.write(filtered_df.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))

    # Download orginal DataSet
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name="Data.csv", mime="text/csv")

#******************************************
    # import plotly.figure_factory as ff
    #
    # st.subheader(":point_right: Neighbourhood_group wise with Room_type")
    # with st.expander("Summary_Table"):
    #     df_sample = df[0:20][
    #         ["neighbourhood_group", "neighbourhood", "reviews_per_month", "room_type", "price",
    #          "host_name"]]
    #     fig = ff.create_table(df_sample, colorscale="Cividis")
    #     st.plotly_chart(fig, use_container_width=True)
#***************************************************
    import plotly.figure_factory as ff

    st.subheader(":point_right: Average Rating & Price by Room Type & Neighbourhood")
    with st.expander("Summary_Table"):
        df_sample = df.groupby(["neighbourhood_group", "neighbourhood", "room_type"]).agg({
            "reviews_per_month": "mean",
            "price": "mean",
            "host_name": "count"  # Just to count the number of hosts, you can change it to any aggregate function
        }).reset_index()

        # Round the average values to 2 decimal places
        df_sample["reviews_per_month"] = df_sample["reviews_per_month"].round(2)
        df_sample["price"] = df_sample["price"].round(2)

        # Rename the columns if needed
        df_sample = df_sample.rename(columns={
            "reviews_per_month": "Avg_Reviews_Per_Month",
            "price": "Avg_Price",
            "host_name": "Host_Count"
        })

        fig = ff.create_table(df_sample, colorscale="Cividis")
        st.plotly_chart(fig, use_container_width=True)

    # map function for room_type

    st.subheader("Airbnb Analysis in Map view")

    # If your DataFrame has columns 'Latitude' and 'Longitude':
    df = df.rename(columns={"Latitude": "lat", "Longitude": "lon"})

    # Check if neighborhoods are selected in the sidebar
    if not neighbourhood:
        # No neighborhoods selected, show all data on the map
        st.map(df)
    else:
        # Filter the DataFrame based on selected neighborhoods
        filtered_df_for_map = filtered_df.copy()  # Assuming filtered_df is the DataFrame after neighborhood filtering

        # If 'neighbourhood' is not available in the DataFrame, adjust it accordingly
        if 'neighbourhood' in filtered_df_for_map.columns:
            filtered_df_for_map = filtered_df_for_map[filtered_df_for_map["neighbourhood"].isin(neighbourhood)]

        # Display the map
        st.map(filtered_df_for_map)

