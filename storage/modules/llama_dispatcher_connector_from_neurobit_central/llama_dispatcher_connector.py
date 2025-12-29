# llama_dispatcher_connector.py
import subprocess
import json
import sys

def llama_dispatch(message_yaml_path):
    """Llama local invoca este script para distribuir mensajes"""
    try:
        # Cargar el mensaje YAML
        with open(message_yaml_path, 'r') as f:
            import yaml
            message = yaml.safe_load(f)
        
        # Determinar destinatarios según el protocolo
        targets = message.get("DESTINO", ["TRON"])  # Por defecto al NODO_SEMILLA
        results = []
        
        from dispatcher_lite import dispatch_to_agent
        
        for target in targets:
            result = dispatch_to_agent(target, message)
            results.append(result)
        
        # Generar reporte
        from dispatcher_lite import generate_delivery_report
        report_path = generate_delivery_report(results)
        
        return {
            "status": "COMPLETED",
            "report": str(report_path),
            "results": results
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "error": str(e)
        }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        result = llama_dispatch(sys.argv[1])
        print(json.dumps(result, indent=2))
    else:
        print("Uso: python3 llama_dispatcher_connector.py <ruta_mensaje.yaml>")