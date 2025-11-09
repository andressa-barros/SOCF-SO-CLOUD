from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

nomes = "Andressa de Oliveira Barros"

@app.route("/")
def home():
    return """
    <h1>SO em Cloud</h1>
    <p>Escolha uma rota:</p>
    <ul>
        <li><a href="/info">/info - Mostrar integrantes da equipe</a></li>
        <li><a href="/metricas">/metricas - Mostrar métricas do sistema em JSON</a></li>
    </ul>
    """

@app.route("/info")
def info():
    return f"Integrantes da equipe: {nomes}"

@app.route("/metricas")
def metricas():
   
    pid = os.getpid()

    processo = psutil.Process(pid)

    memoria = processo.memory_info().rss / (1024 * 1024)

    cpu = processo.cpu_percent(interval=0.5)

    so = f"{platform.system()} ({platform.release()})"

    return jsonify({
        "PID":pid,
        "Memoria": round(memoria, 2),
        "CPU": round(cpu, 2),
        "Sistema_Operacional": so
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)