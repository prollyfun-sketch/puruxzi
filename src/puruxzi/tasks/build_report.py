# src/puruxzi/tasks/build_report.py
from puruxzi.task import Task
from puruxzi.task_registry import TaskRegistry

from puruxzi.task_registry import register_task

@register_task("build_report")
class BuildReportTask(Task):
    """Example Build Report task."""
    def run(self):
        print("Generating build report...")
