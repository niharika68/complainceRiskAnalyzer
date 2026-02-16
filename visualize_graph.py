from app import app

# Simple Mermaid diagram (works in markdown, GitHub, etc.)
print("Compliance Risk Analyzer - Workflow Structure\n")
print(app.get_graph().draw_mermaid())
