from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>1337x Torrent Uploader Leaderboard</title>
    <meta http-equiv="refresh" content="120">
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Courier New', monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px;
        }

        h1 {
            color: #58a6ff;
            margin-bottom: 20px;
            font-size: 2em;
        }

        table {
            border-collapse: collapse;
            width: 80%;
            max-width: 800px;
            background-color: #161b22;
            box-shadow: 0 0 10px rgba(88,166,255,0.2);
            border-radius: 12px;
            overflow: hidden;
        }

        th, td {
            padding: 16px;
            text-align: left;
        }

        th {
            background-color: #21262d;
            color: #58a6ff;
            font-size: 1.1em;
            border-bottom: 2px solid #30363d;
        }

        tr:nth-child(even) {
            background-color: #1c2128;
        }

        tr:hover {
            background-color: #2a2f38;
            transition: 0.2s ease;
        }

        td {
            border-bottom: 1px solid #30363d;
        }
    </style>
</head>
<body>
    <h1>🏴‍☠️ 1337x Torrent Uploader Leaderboard</h1>
    <table>
        <tr><th>Uploader</th><th>Uploads (Today)</th></tr>
        {% for name, count in leaderboard %}
        <tr><td>{{ name }}</td><td>{{ count }}</td></tr>
        {% endfor %}
    </table>
</body>
</html>
'''


@app.route("/")
def leaderboard():
    url = "https://1337x.to/popular-movies"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        rows = soup.select('table.table-list tbody tr')

        uploaders = {}
        for row in rows:
            uploader_tag = row.select_one('td.coll-5 a')
            if uploader_tag:
                uploader = uploader_tag.text.strip()
                uploaders[uploader] = uploaders.get(uploader, 0) + 1

        sorted_uploaders = sorted(uploaders.items(), key=lambda x: x[1], reverse=True)
        return render_template_string(TEMPLATE, leaderboard=sorted_uploaders[:10])

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
