from dataclasses import dataclass

import pandas as pd

# this makes easier to openai api to understand what is the prompt and what is the completion
PROMPT_END = '\n\n###\n\n'


@dataclass
class DatasetLabel:
    start: int
    end: int
    name: str


@dataclass
class ExportedDatasetItem:
    id: int
    text: str
    labels: list[DatasetLabel]


@dataclass
class TrainingDatasetItem:
    prompt: str
    completion: str


def parse_doccano_content(file_content: str):
    # all parsed items
    dataset = list[ExportedDatasetItem]()
    full_dataset = []

    # enumerate files in directory
    json_obj = pd.read_json(file_content, lines=True, encoding='utf8')
    for index, row in json_obj.iterrows():
        item = ExportedDatasetItem(
            id=row['id'],
            text=row['text'],
            labels=list[DatasetLabel]()
        )

        for label in row['label']:
            item.labels.append(
                DatasetLabel(
                    start=label[0],
                    end=label[1],
                    name=label[2].strip()
                )
            )

        dataset.append(item)

    for item in dataset:
        labels_set = set()
        for label in item.labels:
            labels_set.add(item.text[label.start:label.end].strip())

        completion = '\n'.join(labels_set).strip()
        full_dataset.append(
            TrainingDatasetItem(
                prompt=item.text.strip() + PROMPT_END,
                completion=' ' + completion.strip() + PROMPT_END
            )
        )

    return full_dataset
