import plotly.express as px


def create_diagnostic_chart(data, output_file):
    figure = px.bar(
        data,
        x="vehicle_id",
        y="number_of_issues",
        color="diagnostic_status",
        title="Vehicle Diagnostic Issues",
    )
    figure.write_html(output_file)
