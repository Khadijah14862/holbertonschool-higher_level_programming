#!/usr/bin/python3
"""Generate personalized invitation files."""

import logging
import os


def generate_invitations(template, attendees):
    """Generate an invitation file for each attendee."""

    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = [
        "name", "event_title", "event_date", "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + key + "}", str(value)
            )

        filename = "output_{}.txt".format(index)

        if os.path.exists(filename):
            logging.warning("File %s already exists.", filename)

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except OSError as error:
            logging.error("Error writing %s: %s", filename, error)
