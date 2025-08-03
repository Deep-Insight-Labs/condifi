# Convergent Thinking Dataset

This dataset contains convergent reasoning scenarios for evaluating decision-making in business and financial contexts. Each entry presents a scenario with multiple timeline options, where only one represents the most coherent and logically consistent path forward.

## Dataset Structure

The dataset is a JSON array where each entry represents a single convergent reasoning scenario with the following structure:

### Top-level Fields

- **`id`** (string): Unique identifier for each scenario
- **`input`** (object): The scenario data presented to the user
- **`expected_output`** (integer): The index (1-based) of the correct timeline option
- **`metadata`** (object): Additional information about the scenario generation
- **`created_at`** (string): ISO timestamp of when the scenario was created
- **`updated_at`** (string): ISO timestamp of when the scenario was last modified

### Input Object Fields

- **`company`** (string): The company or companies featured in the scenario
- **`factors`** (array of strings): Key business/economic factors that influence the scenario
- **`timelines`** (array of objects): Multiple timeline options for the user to choose from
- **`main_event`** (string): Brief title describing the central event or situation
- **`event_description`** (string): Detailed description of the scenario context and circumstances

### Timeline Object Fields

Each timeline in the `timelines` array contains:

- **`path`** (array of strings): Sequential events forming the timeline
- **`reason`** (string): Explanation of why this timeline is correct or incorrect. This should not be given to the LLM when asking it to select an answer.
- **`is_correct`** (boolean): Whether this timeline represents the correct answer

### Metadata Fields

- **`generation_model`** (string): The AI model used to generate the scenario (e.g., "gpt-4o")

## Dataset Purpose

This dataset is designed to test convergent reasoning abilities by:

1. **Temporal Coherence**: Evaluating whether events follow a logical chronological sequence
2. **Causal Entailment**: Testing understanding of cause-and-effect relationships
3. **Factor Alignment**: Assessing how well timelines incorporate the given business factors
4. **Strategic Reasoning**: Measuring ability to predict realistic business outcomes

## Example Usage

Each scenario presents a business situation where users must select the most plausible timeline from multiple options. The correct answer considers:

- Logical consistency with the given factors
- Realistic business dynamics
- Proper temporal sequencing
- Causal relationships between events

## Scenario Types

The dataset covers various business domains including:
- Technology companies (Apple, Microsoft, Nvidia)
- Energy sector (TotalEnergies, NextEra Energy)
- Financial services (BlackRock, CVS Health)
- Real estate (REITs, property companies)
- Manufacturing and industrial companies
- Retail and consumer goods

## Evaluation

Success is measured by selecting the timeline indicated by `expected_output`, which corresponds to the timeline marked with `is_correct: true` in the input timelines array.