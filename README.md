# Airbnb Data Analysis through interactive Dashboard

**Introduction**
This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends

**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Contact

**Key Technologies and Skills**
- Python
- Pandas
- MongoDb
- Streamlit
- Plotly

**Installation**

To run this project, you need to install the following packages:

```python
pip install pandas
pip install requests
pip install streamlit
pip install plotly
```

**Usage**

To use this project, follow these steps:

1. Install the required packages: ```pip install -r requirements.txt```
2. Run the Streamlit app: ```streamlit run airbnb.py```
3. Access the app in your browser at ```http://localhost:8501```

**Features**

- **Data Collection:** Download sample data from MongoDB.

- **Upload Data to Jupiter Notebook:** Clean the data by removing duplicates, and replacing NaT values where ever requried, especially in Numerical Data.

- **Upload cleaned Data to MongoDB:** Create a connection betweeen Jupiter Notebook and MongoDb and move the cleaned data to MongoDb.

- **Streamlit:** The Streamlit app provides an intuitive interface to interact with the charts and explore the data visually. Users can customize the visualizations, filter data, and zoom in or out to focus on specific aspects of the analysis.

- **Plotly:** Utilizing the power of Plotly, users can create various types of charts, including line charts, bar charts, scatter plots, pie charts, and more. These visualizations enhance the understanding of the data and make it easier to identify patterns, trends, and correlations.

- **Data Insights and Exploration:** Embark on an analytical journey with interactive Plotly charts and maps, offering insights with Room Type and Neighbourhood Group, and Price comparison among various categorical values.


- **Top Performers Highlight:** Easily understand the no. of max users and Neighbourgood group wise Ratings which will help to choose the room by user easily.

- **User-Focused Dashboard:** Navigate through an intuitive Streamlit dashboard designed for user convenience, making exploration a breeze.

- **Data-Driven Decision Making:** Empower your decision-making process by leveraging valuable trends, patterns, and statistics derived from the airbnb data.

  **Contact**

📧 Email: safycosting@gmail.com

🌐 LinkedIn: https://www.linkedin.com/posts/sabiullah-noor-mohamed-83507386

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
