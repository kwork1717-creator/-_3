from flask import Flask, request
from math import gcd

app = Flask(__name__)


EMAIL_SLUG = "9aazizbek9@gmail.com"


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def parse_natural(value):
    if value is None:
        return None
    try:
        # Запрещаем float-строки типа "3.0", "1e2", " 3 "
        if not str(value).strip().lstrip('+').isdigit():
            return None
        n = int(value)
        if n >= 1:
            return n
        return None
    except (ValueError, TypeError):
        return None


@app.route(f"/{EMAIL_SLUG}")
def compute_lcm():
    x = parse_natural(request.args.get("x"))
    y = parse_natural(request.args.get("y"))

    if x is None or y is None:
        return "NaN", 200, {"Content-Type": "text/plain"}

    result = lcm(x, y)
    return str(result), 200, {"Content-Type": "text/plain"}


@app.route("/")
def index():
    return (
        f"LCM service is running.<br>"
        f"Use: <code>/{EMAIL_SLUG}?x=12&amp;y=18</code>"
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
