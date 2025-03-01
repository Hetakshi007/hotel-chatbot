import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample FAQs for Bharat Avenue Hotel
faq_data = {
    "What are the check-in and check-out times?": "Check-in is from 12:00 PM, and check-out is until 11:00 AM.",
    "Do you offer free Wi-Fi?": "Yes, we provide complimentary Wi-Fi to all our guests.",
    "Is breakfast included in the stay?": "Yes, complimentary breakfast is included with your booking.",
    "Do you have airport pickup and drop services?": "Yes, we offer airport transfer services at an additional cost.",
    "Are pets allowed?": "Unfortunately, pets are not allowed in our hotel.",
    "Do you have parking facilities?": "Yes, we have free parking available for our guests.",
    "Can I modify or cancel my booking?": "Yes, you can modify or cancel your booking based on our cancellation policy. Please contact reception for assistance.",
    "What payment methods do you accept?": "We accept credit/debit cards, UPI, and cash payments.",
    "Do you have conference or banquet halls?": "Yes, we have conference and banquet facilities for business meetings and events.",
    "Is there a swimming pool at the hotel?": "No, we do not have a swimming pool at our property."
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message", "").strip()
    response = faq_data.get(user_input, "I'm sorry, I couldn't find an answer to your question. Please contact our reception for assistance.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
