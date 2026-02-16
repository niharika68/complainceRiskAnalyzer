# Compliance Risk Analyzer - Workflow

## Graph Structure

```mermaid
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD;
        __start__([Start]):::first
        retrieve_metrics(retrieve_metrics)
        retrieve_kb(retrieve_kb)
        evaluate_risks(evaluate_risks)
        search_regulations(search_regulations)
        retrieve_hrsa(retrieve_hrsa)
        generate_report(generate_report)
        __end__([End]):::last
        __start__ --> retrieve_metrics;
        evaluate_risks --> search_regulations;
        generate_report --> __end__;
        retrieve_hrsa --> generate_report;
        retrieve_kb --> evaluate_risks;
        retrieve_metrics --> retrieve_kb;
        search_regulations --> retrieve_hrsa;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
```

## Node Descriptions

- **retrieve_metrics**: Fetch customer metrics from Bedrock Knowledge Base
- **retrieve_kb**: Fetch risk definitions from Bedrock KB & pre-index risk descriptions
- **evaluate_risks**: Evaluate metrics against thresholds, generate risk evaluations
- **search_regulations**: Search DuckDuckGo for regulatory updates
- **retrieve_hrsa**: Search DuckDuckGo for latest HRSA 340B guidance
- **generate_report**: Generate Claude summary + formatted compliance report
