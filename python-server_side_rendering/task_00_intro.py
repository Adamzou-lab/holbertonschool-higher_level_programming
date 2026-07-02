#!/usr/bin/python3
"""Simple templating program that generates invitation files."""
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """Generate output_X.txt invitation files from a template.

    Args:
        template (str): the invitation template with {placeholders}.
        attendees (list): list of dicts with attendee data.
    """
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        logger.error(
            "Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as output_file:
            output_file.write(content)
