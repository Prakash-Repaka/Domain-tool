from flask import Flask, request, render_template
import whois
import datetime

app = Flask(__name__)

def whois_lookup(domain):
    w = whois.whois(domain)
    return w

def clean_data(data):
    cleaned_data = {}
    cleaned_data['domain_name'] = data.get('domain_name', [])
    cleaned_data['registrar'] = data.get('registrar', "N/A").replace("'", "").strip()
    cleaned_data['creation_date'] = parse_dates(data.get('creation_date', []))[1]
    cleaned_data['expiration_date'] = parse_dates(data.get('expiration_date', []))[1]
    cleaned_data['name_servers'] = [name_server.replace("'", "").strip() for name_server in data.get('name_servers', [])]
    cleaned_data['status'] = [status.replace("'", "").strip() for status in data.get('status', [])]
    cleaned_data['emails'] = [email.replace("'", "").strip() for email in data.get('emails', [])]
    cleaned_data['org'] = data.get('org', "N/A").replace("'", "").strip()
    cleaned_data['state'] = data.get('state', "N/A").replace("'", "").strip()
    cleaned_data['country'] = data.get('country', "N/A").replace("'", "").strip()
    return cleaned_data

def parse_dates(date_list):
    if not date_list:
        return "N/A"
    if isinstance(date_list, list):
        parsed_dates = []
        for date in date_list:
            if isinstance(date, datetime.datetime):
                parsed_dates.append(date.strftime('%Y-%m-%d %H:%M:%S %Z'))
            else:
                parsed_dates.append(str(date))
        return parsed_dates
    elif isinstance(date_list, datetime.datetime):
        return date_list.strftime('%Y-%m-%d %H:%M:%S %Z')
    else:
        return str(date_list)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    website = request.form['website']
    results = {}
    try:
        
        whois_data = whois_lookup(website)

        
        results = clean_data(whois_data)

        return render_template('results.html', results=results)
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
