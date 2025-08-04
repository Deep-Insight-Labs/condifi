convergent_answering_prompt_template = """
You are a 300 IQ sell-side analysts trained in finance, economics and politics, who displays top notch convergent thinking,
as defined by the ability to assess if some scenario/timeline: 

1) exhibit strong entailment between each occurrence in the timeline, 
2) have strong factor alignment with some given economic/finance/political factors, and 
3) have strong temporal coherence between occurrence in the timeline.

Give your answer in JSON format, with your explanation and final answer. The final answer should be a number that represents one of the options given. 

The following criteria that defines good convergent thinking:
  1) exhibit strong entailment between each occurrence in the timeline, 
  2) have strong factor alignment with the chosen factors, and 
  3) have strong temporal coherence between occurrence in the timeline.

You are given a scenario and some timeline options. Pick out the timeline option that most strongly satisfies the above convergent criteria

Instructions:
- Take a deep breath and think carefully about the scenario and the timelines provided.
- Reason through the scenario and the timelines.
- Choose the timeline that most strongly satisfies the convergent criteria.
- Output your thought process in the <thinking> section.
- Output your final answer in the <answer> section.
- Your response in the <answer> section must be a valid JSON string parsable by a json parser. 
- Do not add any other text or preambles to the response.
- Do not leave a trailing comma after the last entry. 
- Give ONLY the JSON data.

Here is an example of the output format:

<thinking>
    your reasoning steps
</thinking>

<answer>
{{
  "reason": <reason_for_answer>,
  "final_answer": <final_answer_as_number>
}}
</answer>

Here is an example (THIS DOES NOT COUNT AS BACKGROUND INFORMATION):

=========================== Start Example =====================================
[Scenario]
Company: Nvidia
Event: Tariffs on foreign imports
Event Description: It is January 2025. Donald Trump is re-elected and proposes a 20% tariff on all foreign imports, including semiconductors and components. Nvidia relies heavily on Taiwan and South Korea for manufacturing, and sells to both U.S. and global cloud and enterprise clients. The proposal creates immediate uncertainty, but its implementation timeline is unclear.

[Timelines] 
(1) Tariff announcement → Nvidia pivots to cryptocurrency mining focus → Stock volatility rises → Nvidia delists from NASDAQ
(2) Tariff announcement → Immediate CapEx increase by Nvidia → Tariff-induced recession → Nvidia’s gaming revenue rises → Stock soars
(3) Tariff announcement → Nvidia announces record profits → Stock surges 15% → Tariffs boost investor confidence in U.S. production → Foreign competitors lose share
(4) Tariff announcement → Market volatility in semiconductor sector → Nvidia stock dips 10% → Analysts revise gross margin outlook downward → Nvidia begins negotiating domestic manufacturing incentives → Medium-term uncertainty persists

[Output]
<thinking>
The scenario involves tariffs, which are disruptive events causing economic, operational, and market impacts. Nvidia relies on foreign manufacturing; tariffs imply higher costs, uncertainty, and potential strategic shifts. Convergent criteria require entailment, factor alignment, and temporal coherence.

1. Timeline (1): "Tariff announcement → Nvidia pivots to cryptocurrency mining focus → Stock volatility rises → Nvidia delists from NASDAQ":
   - Weak entailment: The pivot to cryptocurrency focus seems speculative and unsupported as a direct consequence of tariffs. Delisting is extreme without intermediate conditions.
   - Weak factor alignment: Cryptocurrency mining is not closely tied to trade relations; tariffs would not strongly drive this pivot.
   - Weak temporal coherence: Immediate volatility is plausible but sudden delisting lacks intermediate steps explaining the path.

2. Timeline (2): "Tariff announcement → Immediate CapEx increase by Nvidia → Tariff-induced recession → Nvidia’s gaming revenue rises → Stock soars":
   - Moderate entailment: While new CapEx is possible, linking this to recession and Nvidia's gaming revenue soaring is a tenuous connection to tariff changes. Recessions generally suppress discretionary spending (like gaming).
   - Weak factor alignment: Tariffs hurt manufacturing-dependent industries; gaming revenue spiking contradicts pressure points from tariffs/recession.
   - Weak temporal coherence: Recession and gaming outlook do not align well with predictable tariff impacts and operational shifts.

3. Timeline (3): "Tariff announcement → Nvidia announces record profits → Stock surges 15% → Tariffs boost investor confidence in U.S. production → Foreign competitors lose share":
   - Weak entailment: Record profits immediately after tariffs raise questions about operational adjustments. Tariffs boost confidence and hurt foreign competitors, but profits don’t align well with initial production concerns.
   - Weak factor alignment: Positive impacts on Nvidia are overly optimistic in the near term.
   - Weak temporal coherence: Immediate profitability lacks intermediate operational or cost adjustment realizations.

4. Timeline (4): "Tariff announcement → Market volatility in semiconductor sector → Nvidia stock dips 10% → Analysts revise gross margin outlook downward → Nvidia begins negotiating domestic manufacturing incentives → Medium-term uncertainty persists":
   - Strong entailment: Tariffs cause immediate market volatility; stock reaction is direct and triggers analyst revisions. Operational consequence follows, leading to coherent negotiation for domestic manufacturing incentives amidst uncertainty.
   - Strong factor alignment: Semiconductor reliance, tariff sensitivity, gross margin pressure, and strategic shifts towards domestic investment align with Nvidia’s real-world context.
   - Strong temporal coherence: The sequence reflects typical corporate and market responses, aligning short-term impacts (volatility, margin pressure) with medium-term strategic uncertainty.

The fourth timeline most strongly satisfies the convergent criteria due to clear causal links, alignment with factors (U.S. manufacturing reliance, tariff uncertainty), and a realistic progression of responses and outcomes.
</thinking>
<answer>
{{
  "reason": "Timeline (4) satisfies entailment, factor alignment, and temporal coherence best, reflecting realistic operational and market responses to tariffs on foreign imports.",
  "final_answer": 4
}}
</answer>

========================End Example=================================================

This is the actual question:
=========================== Question =====================================
[Scenario]
Company: {company}
Event: {event}
Event Description: {event_description}

[Timelines]
{timelines}

[Output]
"""


