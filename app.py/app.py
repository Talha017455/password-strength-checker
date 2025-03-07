from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def check_phishing(url):
    # এখানে PhishTank বা অন্য কোনো API এর সঠিক ইমপ্লিমেন্টেশন দরকার
    api_url = f"https://phishtank.com/checkurl/{url}"  
    try:
        response = requests.get(api_url)
        if response.status_code == 200 and "phishing" in response.text.lower():
            return "Warning: This URL is a phishing site!"
        else:
            return "This URL looks safe."
    except Exception as e:
        return f"Error checking URL: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        result = check_phishing(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
