import psutil, os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    process_pid = os.getpid()
    pr = psutil.Process(process_pid)
    cpu_percent = pr.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU utilization detected!"
    elif mem_percent > 80:
        message = "High memory utilization detected!"    
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)
