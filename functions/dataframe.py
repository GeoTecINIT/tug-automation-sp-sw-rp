import datetime
import pandas as pd

from dateutil import tz

def load_subjects_info(path):
    subjects_info = pd.read_csv(path)
    age = subjects_info['Age']
    age_info = f'Age info: min={age.min():.2f}, max={age.max():.2f}, mean={age.mean():.2f}, std={age.std():.2f}'
    gender = subjects_info['Gender'].value_counts()
    male_count = gender['M']
    female_count = gender['F']
    gender_info = f'Gender info: male={male_count} ({male_count/(male_count+female_count) * 100}), female={gender["F"]} ({female_count/(male_count+female_count) * 100})'
    return subjects_info, age_info, gender_info


def records_to_dataframe(records_file):
    tidy_samples = []

    for records in records_file:
        for sample in records['samples']:
            sample_type = records['type']
            tidy_samples.append({
                "type": sample_type,
                "timestamp": sample['timestamp'],
                "x": sample['x'],
                "y": sample['y'],
                "z": sample['z']
            })
    df = pd.DataFrame(tidy_samples)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    return df


def datetime_from(execution):
    return datetime.datetime(
        execution.year,
        execution.month,
        execution.day,
        execution.hour - 2,  ## Datetimes were recorded in UTC + 2
        execution.minute,
        execution.second, 
        execution.ms * 1000,
        tzinfo = tz.UTC
        #tzinfo = tz.gettz('Europe/Madrid')
    )