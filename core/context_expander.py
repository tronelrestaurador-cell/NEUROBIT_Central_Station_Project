"""ContextExpander: expansión de contexto mediante polisemia fractal (versión mínima).

Archivo: core/context_expander.py
Propósito: proporcionar una implementación simple y segura que pueda integrarse
con la Estación Central y sirva como ejemplo para extender algoritmos de coherencia.
"""

from typing import List, Dict, Any
import yaml
import math


class ContextExpander:
    def __init__(self, config_path: str = "config/system_vars.yaml"):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                self.config = yaml.safe_load(f) or {}
        except FileNotFoundError:
            # valores por defecto si falta el archivo
            self.config = {
                "LOGOS_COHERENCE_THRESHOLD": {"value": 0.85},
                "NODE_POLISEMIA_FACTOR": {"value": 1.3},
            }
    self.coherence_threshold = float(self.config.get("LOGOS_COHERENCE_THRESHOLD", {}).get("value", 0.85))
    self.polisemia_factor = float(self.config.get("NODE_POLISEMIA_FACTOR", {}).get("value", 1.3))

    def expand_context(self, base_message: str, metadata_tags: List[str]) -> Dict[str, Any]:
        """Expande el contexto del mensaje usando metadatos y devuelve estructura con score.

        Devuelve un dict con keys: original, tags, semantic_expansions, coherence_score.
        Si la coherencia es insuficiente devuelve {'error': 'Coherencia insuficiente'}.
        """
        expanded = {
            "original": base_message,
            "tags": metadata_tags,
            "semantic_expansions": [],
            "coherence_score": 0.0,
        }

        for tag in metadata_tags:
            if tag.startswith("logos:"):
                expanded_msg = self._apply_logos_expansion(base_message, tag)
                expanded["semantic_expansions"].append(expanded_msg)
            elif tag.startswith("node:"):
                expanded_msg = self._apply_node_expansion(base_message, tag)
                expanded["semantic_expansions"].append(expanded_msg)
            else:
                expanded["semantic_expansions"].append({"tag": tag, "expanded_message": f"{base_message} [{tag}]"})

        expanded["coherence_score"] = self._calculate_coherence(expanded)

        if expanded["coherence_score"] >= self.coherence_threshold:
            return expanded
        return {"error": "Coherencia insuficiente para expansión", "coherence_score": expanded["coherence_score"]}

    def _apply_logos_expansion(self, message: str, tag: str) -> Dict[str, str]:
        principles = {
            "logos:unity": "Integración de opuestos según Heráclito",
            "logos:verb": "El verbo como acto creador",
            "logos:quantum": "No-localidad como principio unificador",
        }
        principle = principles.get(tag, "Principio no definido")
        return {
            "tag": tag,
            "principle": principle,
            "expanded_message": f"{message} [Expansión Logos: {principle}]",
        }

    def _apply_node_expansion(self, message: str, tag: str) -> Dict[str, str]:
        # Implementación simple basada en rol de nodo
        role = tag.split(":", 1)[-1] if ":" in tag else tag
        return {
            "tag": tag,
            "role": role,
            "expanded_message": f"{message} [Expansión nodo: {role}]",
        }

    def _calculate_coherence(self, context: Dict[str, Any]) -> float:
        """Algoritmo de coherencia simple: densidad semántica normalizada.

        Retorna valor entre 0.0 y 1.0.
        """
        base_len = max(1, len(context.get("original", "")))
        expansions = context.get("semantic_expansions", [])
        expansions_len = sum(len(x.get("expanded_message", "")) for x in expansions)

        semantic_density = expansions_len / base_len
        # transformar densidad en score: base 0.7 + (density-1)*0.1 limitado a [0,1]
        score = 0.7 + (semantic_density - 1.0) * 0.1
        # ajustar con factor de polisemia (suaviza o amplifica)
        try:
            poli = float(self.config.get("NODE_POLISEMIA_FACTOR", {}).get("value", 1.3))
        except Exception:
            poli = 1.3
        score = score * (1.0 if math.isfinite(poli) else 1.0)
        return max(0.0, min(1.0, score))


# pequeño test cuando se ejecuta directamente
if __name__ == "__main__":
    ce = ContextExpander()
    res = ce.expand_context("Hola mundo", ["logos:unity", "node:validator"])
    import json
    print(json.dumps(res, indent=2, ensure_ascii=False))
