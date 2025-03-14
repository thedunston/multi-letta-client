from flask import Flask, send_from_directory
import argparse

app = Flask(__name__, static_folder='static', template_folder='templates')

def parse_args():
    """Parse command line arguments for host and port configuration."""
    parser = argparse.ArgumentParser(description='Run the multi-agent chat server.')
    parser.add_argument('--host', type=str, default='0.0.0.0',
                       help='Host address to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=5051,
                       help='Port to run the server on (default: 5051)')
    return parser.parse_args()

@app.route('/')
def index():
    """Serve the main chat interface."""
    return send_from_directory('templates', 'multi_agent.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files from the static directory."""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    args = parse_args()
    print(f"Starting server on {args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=True)
