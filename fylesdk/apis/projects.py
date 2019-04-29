from .api_base import ApiBase
from ..utils import get_request

class Projects(ApiBase):
    """Class for Projects APIs."""

    GET_PROJECTS = '/api/tpa/v1/projects'

    def get(self, active_only=None):
        """Get the list of existing Projects.

        Parameters:
            active_only (bool): When set as false, the result will include all the Projects for the organization. (optional)

        Returns:
            List with dicts in Projects schema.
        """
        return get_request({
            'active_only': active_only
        }, Projects.GET_PROJECTS, self._access_token)