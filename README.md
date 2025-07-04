#Airline Booking Demand Dashboard (Python + Flask + API + Plotly)

This is a Python web app that fetches airline booking market demand data using the Travelpayouts API and visualizes it with an interactive dashboard.

---

##Features

- 🔍 Input origin city code (e.g. SYD, MEL, BNE)
- 📊 Shows top 10 popular routes by demand
- 💰 Displays insights: Cheapest, Most Expensive, and Average price
- 📈 Interactive bar chart for flight price trends
- ✅ Built using free and public API

---

##How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/shivam3886/airline-demand-app.git
   cd airline-demand-app
2. Install dependencies:
    bash
    pip install -r requirements.txt
3. Replace API_TOKEN in app.py with your own API key from https://www.travelpayouts.com
4. Run the app:
   bash
   python app.py
5. Open your browser and go to:
   http://127.0.0.1:8080
