from flask import Flask, request, redirect

app = Flask(__name__)

# Default Login Details
users = {
    "Pranali": "pass@123"
}


# Login Page
@app.route("/", methods=["GET", "POST"])
def login():

    error = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Correct username and password check
        if username in users and users[username] == password:

            return f"""
            <div style="text-align:center; margin-top:100px;">
                <h1 style="color:green;">Login Successful 🎉</h1>
                <h2>Welcome, {username}!</h2>
                <a href="/">Logout</a>
            </div>
            """

        else:
            error = "Invalid Username or Password ❌"

    return f"""
<!DOCTYPE html>
<html>
<head>

    <title>Login Page</title>

    <style>

        * {{
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }}

        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
        }}

        .box {{
            width: 380px;
            background: white;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            text-align: center;
        }}

        h1 {{
            color: #333;
            margin-bottom: 25px;
        }}

        input {{
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 15px;
        }}

        button {{
            width: 100%;
            padding: 14px;
            margin-top: 15px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }}

        button:hover {{
            background: #4c5fd5;
        }}

        .signup {{
            display: block;
            margin-top: 20px;
            text-decoration: none;
            color: #667eea;
            font-weight: bold;
        }}

        .error {{
            color: red;
            margin-top: 15px;
        }}

    </style>

</head>

<body>

    <div class="box">

        <h1>Welcome Back 👋</h1>

        <form method="POST">

            <input 
                type="text" 
                name="username"
                placeholder="Enter Username"
                required
            >

            <input 
                type="password" 
                name="password"
                placeholder="Enter Password"
                required
            >

            <button type="submit">Login</button>

        </form>

        <p class="error">{error}</p>

        <a class="signup" href="/signup">
            Don't have an account? Create Account
        </a>

    </div>

</body>
</html>
"""


# Signup Page
@app.route("/signup", methods=["GET", "POST"])
def signup():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:

            message = "Username already exists ❌"

        else:

            users[username] = password

            message = "Account Created Successfully 🎉"

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>Create Account</title>

    <style>

        * {{
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }}

        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #764ba2, #667eea);
        }}

        .box {{
            width: 380px;
            background: white;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            text-align: center;
        }}

        h1 {{
            color: #333;
        }}

        input {{
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
        }}

        button {{
            width: 100%;
            padding: 14px;
            margin-top: 15px;
            background: #764ba2;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }}

        .message {{
            color: green;
            margin-top: 15px;
        }}

        a {{
            display: block;
            margin-top: 20px;
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }}

    </style>

</head>

<body>

    <div class="box">

        <h1>Create Account 📝</h1>

        <form method="POST">

            <input
                type="text"
                name="username"
                placeholder="Create Username"
                required
            >

            <input
                type="password"
                name="password"
                placeholder="Create Password"
                required
            >

            <button type="submit">
                Sign Up
            </button>

        </form>

        <p class="message">{message}</p>

        <a href="/">
            Already have an account? Login
        </a>

    </div>

</body>

</html>
"""


# Run Application
if __name__ == "__main__":
    app.run(debug=True)