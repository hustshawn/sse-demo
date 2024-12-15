from flask import Flask, Response
import time

app = Flask(__name__)


# Add a root route for testing
@app.route("/")
def home():
    return "Server is running!"


@app.route("/events")
def events():
    def generate():
        # Send initial message
        yield "data: Connected to server\n\n"

        # Simulate sending updates from the server
        counter = 0
        while True:
            counter += 1
            # Write the event stream format
            yield f"data: Message {counter}\n\n"
            time.sleep(2)  # Wait for 2 seconds

    # Set headers for SSE
    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


if __name__ == "__main__":
    print("SSE server started on port 3000")
    # Make sure to set host to '0.0.0.0' to allow external connections
    app.run(host="0.0.0.0", port=3000, debug=True)
