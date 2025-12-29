import re
def analyze_text(text):
    # Lógica simplificada de pesos M (Mental) / E (Emocional)
    logical = 1.0 - (len(re.findall(r'pero|aunque|sin embargo', text.lower())) * 0.1)
    affective = len(re.findall(r'siento|honrado|disculpa|perdón', text.lower()))
    m_score = logical # Simplificación para R001
    e_score = -(affective * 0.2)
    return {"M": round(m_score, 2), "E": round(e_score, 2)}
