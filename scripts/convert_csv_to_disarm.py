# batch_csv_to_disarm_json.py

import os
import pandas as pd
import json

# === Configuration ===
script_dir = os.path.dirname(os.path.abspath(__file__))
input_csv_dir = script_dir
output_json_dir = os.path.join(script_dir, "disarm_json_output")
os.makedirs(output_json_dir, exist_ok=True)

# === Function to Generate DISARM Layer ===
def create_disarm_layer(df, name):
    df['account_creation_date'] = pd.to_datetime(df['account_creation_date'], errors='coerce')
    df['is_control'] = df['is_control'].astype(bool)

    top_creation = df[~df['is_control']]['account_creation_date'].value_counts().head(1)
    mass_comment = "No significant account creation spikes observed."
    if not top_creation.empty:
        mass_comment = f"Mass creation of accounts observed on {top_creation.index[0].date()} with {top_creation.iloc[0]} accounts."

    lang_counts = df[~df['is_control']]['post_language'].value_counts().to_dict()
    lang_comment = ", ".join([f"{lang}: {count}" for lang, count in lang_counts.items()]) or "No language data available."

    repost_count = df[(~df['is_control']) & (df['is_repost'])].shape[0]
    repost_comment = f"{repost_count} reposts observed among IO accounts."

    client_counts = df[~df['is_control']]['application_name'].value_counts().head(5)
    automation_comment = ", ".join([f"{client}: {count}" for client, count in client_counts.items()]) or "No automation activity detected."

    techniques = [
        {
            "techniqueID": "T0074",
            "tactic": "plan-strategy",
            "color": "#ff6666",
            "comment": mass_comment,
            "enabled": True,
            "metadata": [],
            "links": [],
            "showSubtechniques": True
        },
        {
            "techniqueID": "T0081",
            "tactic": "target-audience-analysis",
            "color": "#ffe766",
            "comment": f"Top languages: {lang_comment}",
            "enabled": True,
            "metadata": [],
            "links": [],
            "showSubtechniques": True
        },
        {
            "techniqueID": "T0095",
            "tactic": "amplify-message",
            "color": "#8ec843",
            "comment": repost_comment,
            "enabled": True,
            "metadata": [],
            "links": [],
            "showSubtechniques": True
        },
        {
            "techniqueID": "T0094",
            "tactic": "amplify-message",
            "color": "#85c1f2",
            "comment": f"Top automation clients: {automation_comment}",
            "enabled": True,
            "metadata": [],
            "links": [],
            "showSubtechniques": True
        }
    ]

    return {
        "name": name,
        "versions": {
            "attack": "1",
            "navigator": "4.8.2",
            "layer": "4.4"
        },
        "domain": "DISARM",
        "description": "Automatically generated from CSV metadata analysis.",
        "filters": {"platforms": ["Windows", "Linux", "Mac"]},
        "sorting": 0,
        "layout": {
            "layout": "side",
            "aggregateFunction": "average",
            "showID": False,
            "showName": True,
            "showAggregateScores": False,
            "countUnscored": False
        },
        "hideDisabled": False,
        "techniques": techniques,
        "gradient": {
            "colors": ["#ff6666ff", "#ffe766ff", "#8ec843ff"],
            "minValue": 0,
            "maxValue": 100
        },
        "legendItems": [],
        "metadata": [],
        "links": [],
        "showTacticRowBackground": False,
        "tacticRowBackground": "#dddddd",
        "selectTechniquesAcrossTactics": True,
        "selectSubtechniquesWithParent": False
    }

# === Batch Convert CSVs to DISARM JSON ===
converted = []
for filename in os.listdir(input_csv_dir):
    if filename.endswith(".csv"):
        csv_path = os.path.join(input_csv_dir, filename)
        json_path = os.path.join(output_json_dir, filename.replace(".csv", ".json"))
        try:
            df = pd.read_csv(csv_path)
            disarm_json = create_disarm_layer(df, name=filename.replace(".csv", " - DISARM Layer"))
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(disarm_json, f, indent=2)
            converted.append(f"✅ {filename} → {json_path}")
        except Exception as e:
            converted.append(f"❌ {filename} - Failed: {e}")

# === Output Summary ===
print("\nBatch CSV to DISARM JSON Conversion Summary:")
for entry in converted:
    print(entry)
print("\n✅ All conversions completed!")

