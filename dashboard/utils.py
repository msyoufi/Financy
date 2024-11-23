import datetime as dt
from django.db.models import Sum
from django.db.models.functions import TruncMonth


def clean_data(row_data):
    data = dict(row_data)
    data.pop("csrfmiddlewaretoken")
    data = {k: v[0] if isinstance(v, list) else v for k, v in data.items()}
    return data


def get_chart_data(transactions):
    start_date = transactions.first().date
    end_date = dt.date.today()
    days_count = (end_date - start_date).days + 1
    timespan = (start_date + dt.timedelta(days=n) for n in range(days_count))

    value_on_date = {}
    value_chart = []
    expense_chart = {}
    cumulative_value = 0

    for tranx in transactions:
        if tranx.type == "EXP":
            expense_chart[tranx.get_category_display()] = (
                expense_chart.get(tranx.category, 0) + tranx.amount
            )

        cumulative_value += tranx.amount if tranx.type == "INC" else -tranx.amount
        value_on_date[tranx.date] = cumulative_value

    current_value = 0

    for single_date in timespan:
        current_value = value_on_date.get(single_date, current_value)

        data_point = {
            "date": single_date.strftime("%d %b %Y"),
            "value": current_value,
        }
        value_chart.append(data_point)

    savings_chart = income_vs_expenses_chart(transactions)

    return {
        "value_chart": value_chart,
        "expense_chart": expense_chart,
        "savings_chart": savings_chart,
    }


def income_vs_expenses_chart(transactions):
    six_months_ago = dt.datetime.now().date().replace(day=1) - dt.timedelta(days=1)
    six_months_ago = six_months_ago.replace(day=1)

    tranxs = (
        transactions.filter(date__gte=six_months_ago)
        .annotate(month=TruncMonth("date"))
        .values("month", "type")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )

    income_data = {}
    expense_data = {}

    for txn in tranxs:
        month = txn["month"].strftime("%m/%Y")
        if txn["type"] == "INC":
            income_data[month] = txn["total"]
        elif txn["type"] == "EXP":
            expense_data[month] = txn["total"]

    all_months = sorted(set(income_data.keys()).union(expense_data.keys()))
    income_series = [income_data.get(month, 0) for month in all_months]
    expense_series = [expense_data.get(month, 0) for month in all_months]

    return {
        "months": all_months,
        "income": income_series,
        "expenses": expense_series,
    }
