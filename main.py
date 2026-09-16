from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
Path("reports").mkdir(exist_ok=True)

print("AI Meeting & Executive Reporting Assistant")
print("-" * 50)
data = input("Enter project/change/schedule/meeting information: ").strip()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"""You are a construction project-management reporting assistant.
Transform the supplied meeting notes into:
## Executive Summary
## Key Decisions
## Project Updates
## Risks / Issues
## Action Items
## Open Questions
## Management Attention Required
Keep responsibilities and dates tied to information actually provided.

Project information:
{data}"""
)

print("\n" + response.output_text)
Path("reports/analysis.txt").write_text(response.output_text, encoding="utf-8")
print("\nSaved to reports/analysis.txt")
