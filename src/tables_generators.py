__author__ = 'Dror Paz'

from pathlib import Path

from pandas import DataFrame

from .templates import PDF_TEMPLATE, TABLE_STYLE

TIME_COLUMN = 'זמן'
RESTRICTED_CHARS = '"?*/\\'


def df_to_pdf(df: DataFrame, name: str, output_location: Path):
    df.columns.name = ''

    df.index = df.index.set_levels(
        [f'{i:.0f}:00' for i in df.index.levels[df.index.names.index('time')]],
        level='time',
    )
    df.index.names = [None] * 3

    styles = TABLE_STYLE

    s = df.style.set_table_styles(styles, axis=1) \
        .format(na_rep='')
    html = s.render()

    template_vars = {"title": f'לו"ז שבועי של {name}',
                     "table": html}
    html_out = PDF_TEMPLATE.render(template_vars)
    file_name = [i for i in name if i not in RESTRICTED_CHARS]
    out_file = Path(output_location / f'{file_name}.html')
    print(f'Writing {out_file}')
    with out_file.open('w') as file:
        file.write(html_out)


def generate_by_instructor(dataframe: DataFrame, output_location: Path):
    instructors = dataframe.groupby('instructor', sort=True)
    for instructor, inst_df in instructors:
        pi = inst_df.pivot(index=['day', 'time', 'group'], columns='location', values='students')
        df_to_pdf(pi, name=instructor, output_location=output_location)


def generate_by_group(dataframe: DataFrame, output_location: Path):
    groups = dataframe.groupby('group', sort=True)
    for group, group_df in groups:
        pi = group_df.pivot(index=['day', 'time', 'instructor'], columns='location', values='students')
        df_to_pdf(pi, name=group, output_location=output_location)
