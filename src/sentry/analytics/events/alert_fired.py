from __future__ import absolute_import

from sentry import analytics


class AlertFiredEvent(analytics.Event):
    type = "alert.fired"

    attributes = (
        analytics.Attribute("issue_id"),
        analytics.Attribute("project_id"),
        analytics.Attribute("organization_id"),
        analytics.Attribute("rule_id"),
    )


analytics.register(AlertFiredEvent)
