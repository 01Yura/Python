from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Password Strength Calculator</title>
</head>
<body>
    <h1>Password Strength Calculator</h1>
    <form method="post">
        <label for="length">Enter your Wi-Fi password length:</label><br>
        <input type="number" id="length" name="length"><br><br>

        <label>Do you use digits? y/n</label><br>
        <input type="text" name="digits"><br><br>

        <label>Do you use uppercase letters? y/n</label><br>
        <input type="text" name="upper_case"><br><br>

        <label>Do you use lowercase letters? y/n</label><br>
        <input type="text" name="lower_case"><br><br>

        <label>Do you use special symbols like @&*+-$ and others? y/n</label><br>
        <input type="text" name="spec_symb"><br><br>

        <input type="submit" value="Calculate">
    </form>

    {% if result %}
        <h2>Results:</h2>
        <p>Amount combinations of your password: {{ result['pass_comb'] }}</p>
        <p>Using Video Card that costs around $100 your password can be hacked in: {{ result['time_to_hack'] }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        length = int(request.form['length'])
        digits = request.form['digits']
        upper_case = request.form['upper_case']
        lower_case = request.form['lower_case']
        spec_symb = request.form['spec_symb']

        k = 0
        if digits == 'y':
            k += 10
        if upper_case == 'y':
            k += 26
        if lower_case == 'y':
            k += 26
        if spec_symb == 'y':
            k += 31
        
        pass_comb = length ** k
        vga_speed_per_sec = 200000
        minutes = pass_comb / vga_speed_per_sec / 60
        hours = minutes / 60
        days = hours / 24
        months = days / 30.5
        years = months / 12
        century = years / 100
        
        if pass_comb > 10**20: 
            time_to_hack = "Several millions years"
        elif pass_comb > 10**13: 
            time_to_hack = f"{round(years, 1)} years"
        elif pass_comb > 10**12:
            time_to_hack = f"{round(months, 1)} months"
        elif pass_comb > 10**10:
            time_to_hack = f"{round(days, 1)} days"
        elif pass_comb > 10**9:
            time_to_hack = f"{round(hours, 1)} hours"
        else:    
            time_to_hack = f"{round(minutes, 1)} minutes"
        
        result = {
            'pass_comb': pass_comb,
            'time_to_hack': time_to_hack
        }

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)