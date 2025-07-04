from flask import Flask, render_template, request
import requests
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

# 🔹 Your API token from Travelpayouts
API_TOKEN = "2cefd113a75891d0dd28716f84b32b30"  # Replace this with your token

# 🔹 Function to fetch popular routes
def fetch_popular_routes(origin="SYD"):
    url = "https://api.travelpayouts.com/v1/city-directions"
    params = {
        "origin": origin,
        "currency": "usd",
        "token": API_TOKEN
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print("Failed to fetch data:", response.status_code)
        return []

# 🔹 Home route
@app.route("/", methods=["GET"])
def home():
    origin = request.args.get("origin", "SYD")  # default: SYD

    all_routes = fetch_popular_routes(origin)
    routes = list(all_routes.values())[:10]
    # Compute insights
    cheapest = min(routes, key=lambda x: x["price"]) if routes else None
    most_expensive = max(routes, key=lambda x: x["price"]) if routes else None
    average_price = round(sum([r["price"] for r in routes]) / len(routes), 2) if routes else 0


    # Chart data
    destinations = [r["destination"] for r in routes]
    prices = [r["price"] for r in routes]

    bar = go.Bar(x=destinations, y=prices, marker_color="skyblue")
    layout = go.Layout(title=f"Flight Prices from {origin} (Top 10 Routes)")
    fig = go.Figure(data=[bar], layout=layout)
    chart_html = pyo.plot(fig, output_type="div", include_plotlyjs=False)

    return render_template("index.html",
                       routes=routes,
                       chart_html=chart_html,
                       origin=origin,
                       cheapest=cheapest,
                       most_expensive=most_expensive,
                       average_price=average_price)


# 🔹 Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8080)
