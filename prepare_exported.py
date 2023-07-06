# set up directories
import os
from dataclasses import dataclass
import pandas as pd

from src.tools.file import write_file

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
DIRECTORY_DATA = os.path.join(CURRENT_DIRECTORY, 'datasets')
DIRECTORY_EXPORTED = os.path.join(DIRECTORY_DATA, '3_exported')
DIRECTORY_READY = os.path.join(DIRECTORY_DATA, '4_ready')
TRAINING_DATASET_NAME = 'training_dataset.jsonl'
VALIDATION_DATASET_NAME = 'validation_dataset.jsonl'

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


def prepare_exported():
    # all parsed items
    dataset = list[ExportedDatasetItem]()
    fill_dataset = []

    # enumerate files in directory
    for file in os.listdir(DIRECTORY_EXPORTED):
        if not file.endswith('.jsonl'):
            continue

        print('processing file: ' + file)
        file_path = os.path.join(DIRECTORY_EXPORTED, file)
        json_obj = pd.read_json(file_path, lines=True, encoding='utf8')
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
        fill_dataset.append(
            TrainingDatasetItem(
                prompt=item.text.strip() + PROMPT_END,
                completion=' ' + completion.strip() + PROMPT_END
            )
        )

    print(f"Total items: {len(dataset)}")

    # split dataset into training and validation
    validation_dataset = fill_dataset[0:5]
    training_dataset = fill_dataset[5:]

    print('validation dataset size: ' + str(len(validation_dataset)))
    print('training dataset size: ' + str(len(training_dataset)))

    df_training = pd.DataFrame([vars(f) for f in training_dataset])
    df_validation = pd.DataFrame([vars(f) for f in validation_dataset])

    training_file_path = os.path.join(DIRECTORY_READY, TRAINING_DATASET_NAME)
    validation_file_path = os.path.join(DIRECTORY_READY, VALIDATION_DATASET_NAME)

    write_file(training_file_path, df_training.to_json(lines=True, orient='records'))
    write_file(validation_file_path, df_validation.to_json(lines=True, orient='records'))


def main():
    prepare_exported()


if __name__ == '__main__':
    main()