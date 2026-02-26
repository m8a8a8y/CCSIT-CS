from flask import Flask, request, render_template, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>High Level Challenge - Network Tools</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Roboto Mono', monospace; background: #0f172a; color: #f8fafc; text-align: center; padding: 2rem; }
            .container { max-width: 600px; margin: 0 auto; background: rgba(15, 23, 42, 0.6); padding: 2rem; border-radius: 8px; border: 1px solid rgba(0, 224, 255, 0.3); }
            input { padding: 10px; width: 70%; background: #1e293b; border: 1px solid #334155; color: white; }
            button { padding: 10px 20px; background: #00e0ff; border: none; font-weight: bold; cursor: pointer; color: #000; }
            button:hover { background: #00b8d4; }
            pre { background: #000; color: #0f0; padding: 1rem; text-align: left; overflow-x: auto; margin-top: 1rem; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Network Status Check</h1>
            <p>Ping a server to check connectivity.</p>
            <form action="/ping" method="POST">
                <input type="text" name="host" placeholder="Enter IP or Hostname (e.g., google.com)" required>
                <button type="submit">Ping</button>
            </form>
            <div style="margin-top: 2rem; font-size: 0.8rem; color: #64748b;">
                System Maintenance: Admins run <code>sudo /opt/scripts/healthcheck.py</code> periodically.
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/ping', methods=['POST'])
def ping():
    host = request.form.get('host', '')

    # VULNERABLE: Direct concatenation allowing command injection
    # e.g., 127.0.0.1; ls -la
    cmd = f"ping -c 3 {host}"

    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        result = output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        result = e.output.decode('utf-8')
    except Exception as e:
        result = str(e)

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ping Result</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Roboto Mono', monospace; background: #0f172a; color: #f8fafc; padding: 2rem; }}
            pre {{ background: #000; color: #0f0; padding: 1rem; border-radius: 4px; }}
            a {{ color: #00e0ff; }}
        </style>
    </head>
    <body>
        <h1>Execution Result</h1>
        <pre>{result}</pre>
        <a href="/">Back</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
