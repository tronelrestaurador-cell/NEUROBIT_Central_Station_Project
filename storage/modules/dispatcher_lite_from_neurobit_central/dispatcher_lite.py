# dispatcher_lite.py (versión corregida)
import requests
import json
import time
import os
from pathlib import Path

def dispatch_to_agent(agent, task):
    """Versión mejorada para Llama3.2 local"""
    target_url = {
        "SIMON": "http://localhost:8081/inbox",
        "EVA": "http://localhost:8082/messages",
        "TRON": "http://localhost:8080/user"
    }.get(agent, f"http://localhost:9000/{agent}")
    
    try:
        response = requests.post(target_url, json=task, timeout=30)
        return {
            "status": "DELIVERED" if response.status_code == 200 else "FAILED",
            "timestamp": time.isoformat(),
            "agent": agent,
            "response_code": response.status_code,
            "response_body": response.json() if response.status_code == 200 else None
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e),
            "agent": agent,
            "timestamp": time.isoformat()
        }

def generate_delivery_report(results):
    """Genera reporte para Memoria EVA"""
    report = {
        "round_id": f"R_{int(time.time())}",
        "timestamp": time.isoformat(),
        "results": results,
        "summary": {
            "delivered": sum(1 for r in results if r.get("status") == "DELIVERED"),
            "failed": sum(1 for r in results if r.get("status") == "FAILED")
        }
    }
    # Guardar en Memoria EVA
    reports_dir = Path("~/neurobit/reports").expanduser()
    reports_dir.mkdir(exist_ok=True)
    report_path = reports_dir / f"delivery_report_{int(time.time())}.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    return report_path