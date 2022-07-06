import click

from src.features.build_features import *


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def integral_model(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

    """Пример интегральной модели"""
    if 18 < get_age() <= 25:
        age_score = 5
    elif 25 < get_age() <= 75:
        age_score = 10
    else:
        age_score = 0

    if 0 < get_avg_salary() <= 50000:
        avg_salary_score = 0
    else:
        avg_salary_score = 10

    if get_act_loan_count() < 5:
        act_loan_count_score = 10
    else:
        act_loan_count_score = 3

    return age_score + avg_salary_score + act_loan_count_score


if __name__ == '__main__':
    integral_model_result = integral_model()
    print(integral_model_result)
