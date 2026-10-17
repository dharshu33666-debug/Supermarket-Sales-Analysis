from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "supermarket_large_dataset.csv")


@app.route("/")
def home():
    try:
        df = pd.read_csv(CSV_FILE)

        # Required columns
        required_columns = [
            "sales_revenue",
            "units_sold",
            "profit_per_unit",
            "profit_margin"
        ]

        missing = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing:
            return "Missing CSV columns: " + ", ".join(missing), 500

        # Convert numeric columns safely
        for col in required_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=required_columns)

        # Summary calculations
        total_sales = round(float(df["sales_revenue"].sum()), 2)

        total_units = int(df["units_sold"].sum())

        total_profit = round(
            float((df["profit_per_unit"] * df["units_sold"]).sum()),
            2
        )

        # Number of rows / records
        total_records = int(len(df))

        # Total Orders:
        # Use order_id if available; otherwise use record count.
        if "order_id" in df.columns:
            total_orders = int(df["order_id"].nunique())
        elif "order_number" in df.columns:
            total_orders = int(df["order_number"].nunique())
        else:
            total_orders = total_records

        # Profit margin percentage
        # Overall profit divided by total sales
        if total_sales != 0:
            profit_margin = round(
                (total_profit / total_sales) * 100, 2
            )
        else:
            profit_margin = 0

        # Prepare chart data
        group_size = max(1, (len(df) + 6) // 7)
        groups = df.index // group_size

        sales_group = df.groupby(groups)["sales_revenue"].sum()

        profit_group = df.groupby(groups)["profit_per_unit"].mean()

        chart_labels = [
            f"Group {i + 1}" for i in range(len(sales_group))
        ]

        chart_values = [
            round(float(value), 2)
            for value in sales_group.values
        ]

        profit_values = [
            round(float(value), 2)
            for value in profit_group.values
        ]

        return render_template(
            "index.html",
            total_sales=total_sales,
            total_units=total_units,
            total_profit=total_profit,
            total_records=total_records,
            total_orders=total_orders,
            profit_margin=profit_margin,
            chart_labels=chart_labels,
            chart_values=chart_values,
            profit_values=profit_values
        )

    except FileNotFoundError:
        return "CSV file not found. Check the file name.", 404

    except Exception as error:
        return f"Error loading dashboard: {error}", 500


if __name__ == "__main__":
    app.run(debug=True)