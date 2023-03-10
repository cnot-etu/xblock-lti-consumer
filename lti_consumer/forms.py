"""
Defines a form for providing validation of LTI consumer course-specific configuration.
"""


import logging

from django import forms

from lti_consumer.models import CourseEditLTIFieldsEnabledFlag
from lti_consumer.plugin.compat import clean_course_id

log = logging.getLogger(__name__)


class CourseEditLTIFieldsEnabledAdminForm(forms.ModelForm):
    """
    Form for LTI consumer course-specific configuration to verify the course id.
    """

    class Meta:
        model = CourseEditLTIFieldsEnabledFlag
        fields = '__all__'

    def clean_course_id(self):
        """
        Validate the course id
        """
        return clean_course_id(self)
