from inspect_ai import Task, task
from inspect_ai.dataset import FieldSpec, hf_dataset
from inspect_ai.scorer import exact
from inspect_ai.solver import generate

@task
def simpleqa():
    return Task(
        dataset=hf_dataset(
            "codelion/SimpleQA-Verified",
            split="train[:2]",
            sample_fields=FieldSpec(
                input="problem",
                target="answer",
            ),
        ),
        solver=generate(max_tokens=750),
        scorer=exact(),
    )