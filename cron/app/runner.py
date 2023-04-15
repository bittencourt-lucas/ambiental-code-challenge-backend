from workflows.process_forecast_data_workflow import ProcessForecastDataWorkflow


active_workflows = [
    ProcessForecastDataWorkflow
]

for workflow in active_workflows:
    workflow.run()
