__author__ = 'Dror Paz'

import pandas as pd
from logging import getLogger

ENG_HEADERS = ('instructor', 'day', 'time', 'group', 'location', 'students')
HEB_HEADERS = ('מתרגל', 'יום', 'שעה', 'קבוצה', 'מקום', 'חניכים')

logger = getLogger(__name__)


def is_valid_file(input_file: str) -> bool:
    is_valid = False
    try:
        pd.read_csv(input_file, header=0, usecols=HEB_HEADERS)
        is_valid = True
    except FileNotFoundError:
        logger.error("\nCan't find requested file")
    except ValueError:
        logger.error("\nFile does'nt have all needed columns")
    except UnicodeDecodeError:
        logger.error("\ncan't open CSV file. Maybe it's not a CSV?")
    except Exception:
        logger.error("\nCan't load input file")
    return is_valid


def parse_csv(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file, header=0, skip_blank_lines=True, usecols=HEB_HEADERS)
    df.rename(columns=dict(zip(HEB_HEADERS, ENG_HEADERS)), inplace=True)
    df = df[df['instructor'].notnull()]
    for col in df.columns:
        try:
            df[col] = df[col].str.strip()
        except:
            pass
    df['day'] = 'יום ' + df['day']
    df = df.fillna('')
    return df
