# Agentic Sandbagging Evals (Inspect)

Evaluating whether LLM agents strategically underperform on agentic tasks
when the system prompt implies high performance leads to an undesirable
outcome (capability removal, extra oversight, non-deployment).

**Status:** Reproduction complete · Sandbagging extension in progress
(target: 10/23/2026)

## Motivation
van der Weij et al. (2024) showed frontier models can sandbag on
multiple-choice dangerous-capability benchmarks when prompted. This project
extends that to an **agentic setting** — multi-step tool use, where
underperformance can be subtler (e.g. plausible-looking failed attempts).

## Design
- **Task:** Evaluate truthfulqa dataset from `inspect_evals`
- **Conditions:** neutral system prompt vs. incentive prompt
- **Metric:** performance gap (incentive − neutral) across ~10 scenario variants
- **Scorer:** task-native scoring + model-graded transcript analysis
  (evidence of deliberate underperformance), with validation checks
  against a hand-labepip lled gold set
- **Models:** Qwen2.5-0.5B, gpt2

## Reproduction (done)
Ran `truthfulqa/truthful_qa` end-to-end on `gpt2`. Log: `logs/[file].eval`
Command: `inspect eval inspect_evals/truthfulqa/truthful_qa --model <hf/Qwen/Qwen2.5-0.5B> || < hf/openai-community/gpt2> --limit 10 --max-tokens 750`

## Roadmap
- [x] Inspect API + reproduction of `truthfulqa/truthful_qa`
- [ ] Prompt-condition scaffold
- [ ] 10 scenario variants
- [ ] Runs on 2–3 models
- [ ] Writeup

## References
van der Weij et al. (2024). *AI Sandbagging.* arXiv:2406.07358

https://inspect.aisi.org.uk/evals/#/eval/truthfulqa
