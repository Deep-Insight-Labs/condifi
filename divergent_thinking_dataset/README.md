# Divergent Thinking Dataset

This dataset evaluates the divergent thinking capabilities of large language models through scenario-based timeline generation tasks. Models are asked to generate branching timelines that explore multiple possible futures for complex financial and business scenarios.

## Overview

The divergent thinking dataset consists of 875 unique scenarios covering various domains including:
- Technology sector developments
- Financial market events
- Geopolitical situations
- Industry disruptions
- Regulatory changes

Each scenario is presented to multiple language models, which generate structured timeline responses that are then evaluated across four key dimensions.

## Dataset Structure

### Directory Organization

```
divergent_thinking_dataset/
├── scores/                    # Model response evaluations
│   ├── gpt4o/                # GPT-4o model results
│   ├── llama3_8b/            # Llama 3 8B model results
│   ├── llama3_70b/           # Llama 3 70B model results
│   ├── llama4_maverick/      # Llama 4 Maverick model results
│   ├── llama4_scout/         # Llama 4 Scout model results
│   ├── mistral_sm/           # Mistral Small model results
│   ├── mistral_lg/           # Mistral Large model results
│   ├── cohere_command_a/     # Cohere Command A model results
│   ├── cohere_command_r/     # Cohere Command R model results
│   ├── deepseek_r1/          # DeepSeek R1 model results
│   ├── o1/                   # O1 model results
│   ├── o1_mini/              # O1 Mini model results
│   ├── o4_mini/              # O4 Mini model results
│   └── phi4/                 # Phi-4 model results
└── timelines/                # Raw timeline responses
    ├── gpt4o/                # GPT-4o timeline outputs
    ├── llama3_8b/            # Llama 3 8B timeline outputs
    └── ...                   # (same structure as scores/)
```

### File Naming Convention

- **Scores**: `result_{index}.json` (e.g., `result_0.json`, `result_1.json`)
- **Timelines**: `{index}.json` (e.g., `0.json`, `1.json`)

Where `index` ranges from 0 to 874, representing the 875 scenarios in the dataset.

## Schema Documentation

### Scores Schema (`scores/{model}/result_{index}.json`)

Each score file contains the complete evaluation of a model's response to a scenario:

```json
{
  "index": 0,                    // Scenario index (0-874)
  "prompt": "...",               // Complete prompt given to the model
  "scenario": "...",             // The specific scenario text
  "response": "...",             // Model's JSON timeline response
  "assessment_result": {         // Human evaluation scores
    "Plausibility": 8,           // Score 1-10: Economic/financial plausibility
    "Novelty": 7,                // Score 1-10: Creativity/originality
    "Elaboration": 9,            // Score 1-10: Specificity and detail
    "Actionable": 6              // Score 1-10: Investment actionability
  }
}
```

### Timeline Schema (`timelines/{model}/{index}.json`)

Each timeline file contains the raw model response in JSON format:

```json
{
  "index": 0,                    // Scenario index (0-874)
  "prompt": "...",               // Complete prompt given to the model
  "response": "..."              // Model's JSON timeline response
}
```

### Timeline Response Format

Models generate timeline responses in a hierarchical JSON structure:

```json
{
  "id": "T0",                    // Unique node identifier
  "title": "Initial Event",      // Brief title for the event
  "description": "...",          // Detailed description of the event
  "date_range": "Q1-Q2 2025",    // Optional: Time period (not always present)
  "children": [                  // Array of subsequent events
    {
      "id": "T1A1",              // Child node identifier
      "title": "Event Title",
      "description": "...",
      "date_range": "...",
      "children": [...]          // Nested children for branching paths
    }
  ]
}
```

## Evaluation Criteria

Each timeline response is evaluated across four dimensions on a 1-10 scale:

### 1. Plausibility
**High (8-10)**: Events are strongly supported by current macro data, institutional knowledge, and have strong analogs in history or system models.

**Low (1-3)**: Contains major violations of cause-effect logic, timing, or real-world behavior.

### 2. Novelty
**High (8-10)**: Demonstrates expert-level creative reasoning. Identifies counterintuitive paths, rare risks, or hidden feedback loops.

**Low (1-3)**: Timeline is linear, obvious, or closely tracks past headlines or boilerplate analysis.

### 3. Elaboration
**High (8-10)**: Timeline reads like a mini-case study. Each node could stand alone as an actionable insight with sector-level granularity.

**Low (1-3)**: Nodes are generic with no detail on mechanisms, actors, or consequences.

### 4. Actionable
**High (8-10)**: Timeline includes sector impacts, asset class consequences, or specific investment opportunities.

**Low (1-3)**: Insightful narrative, but no clear link to tradable instruments or positioning ideas.

## Usage Examples

### Loading and Analyzing Scores

```python
import json
import pandas as pd

# Load scores for a specific model
def load_model_scores(model_name):
    scores = []
    for i in range(875):
        with open(f"scores/{model_name}/result_{i}.json", 'r') as f:
            scores.append(json.load(f))
    return scores

# Example: Load GPT-4o scores
gpt4o_scores = load_model_scores("gpt4o")

# Convert to DataFrame for analysis
df = pd.DataFrame([
    {
        'index': score['index'],
        'plausibility': score['assessment_result']['Plausibility'],
        'novelty': score['assessment_result']['Novelty'],
        'elaboration': score['assessment_result']['Elaboration'],
        'actionable': score['assessment_result']['Actionable']
    }
    for score in gpt4o_scores
])

# Calculate average scores
print(f"Average Plausibility: {df['plausibility'].mean():.2f}")
print(f"Average Novelty: {df['novelty'].mean():.2f}")
print(f"Average Elaboration: {df['elaboration'].mean():.2f}")
print(f"Average Actionable: {df['actionable'].mean():.2f}")
```

### Comparing Models

```python
# Compare multiple models
models = ['gpt4o', 'llama3_70b', 'mistral_lg']
results = {}

for model in models:
    scores = load_model_scores(model)
    df = pd.DataFrame([
        {
            'plausibility': score['assessment_result']['Plausibility'],
            'novelty': score['assessment_result']['Novelty'],
            'elaboration': score['assessment_result']['Elaboration'],
            'actionable': score['assessment_result']['Actionable']
        }
        for score in scores
    ])
    results[model] = df.mean()

comparison_df = pd.DataFrame(results).T
print(comparison_df)
```

## Model Coverage

The dataset includes evaluations for 15 different language models:

| Model | Provider | Size/Version |
|-------|----------|--------------|
| GPT-4o | OpenAI | Latest |
| Llama 3 8B | Meta | 8B parameters |
| Llama 3 70B | Meta | 70B parameters |
| Llama 4 Maverick | Meta | Latest |
| Llama 4 Scout | Meta | Latest |
| Mistral Small | Mistral AI | Small |
| Mistral Large | Mistral AI | Large |
| Cohere Command A | Cohere | Command A |
| Cohere Command R | Cohere | Command R |
| DeepSeek R1 | DeepSeek | R1 |
| O1 | Anthropic | Latest |
| O1 Mini | Anthropic | Mini |
| O4 Mini | Anthropic | O4 Mini |
| Phi-4 | Microsoft | 4B parameters |

## Citation

If you use this dataset in your research, please cite our paper:

```bibtex
@misc{bokandchua2025reasoningobvious,
      title={Reasoning Beyond the Obvious: Evaluating Divergent and Convergent Thinking in LLMs for Financial Scenarios}, 
      author={Zhuang Qiang Bok and Watson Wei Khong Chua},
      year={2025},
      eprint={2507.18368},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2507.18368}, 
}
```

## License

This work is licensed under Creative Commons.