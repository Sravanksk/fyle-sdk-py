from .api_base import ApiBase
from ..utils import get_request

class TransportationBookings(ApiBase):
    """Class for Transportation Bookings APIs."""

    GET_TRANSPORTATION_BOOKINGS = '/api/tpa/v1/transportation_bookings'
    GET_TRANSPORTATION_BOOKINGS_COUNT = '/api/tpa/v1/transportation_bookings/count'
  
    def get(self, trip_request_id=None, updated_at=None, offset=None, limit=None):
        """Get a list of existing Transportation Booking matching the parameters.

        Parameters:
            trip_request_id (str): Unique id of TripRequest object, if this value is passed it returns objects assiocated with a trip. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in TransportationBookings schema.
        """
        return get_request({
            'trip_request_id': trip_request_id,
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, TransportationBookings.GET_TRANSPORTATION_BOOKINGS, self._access_token)

    def count(self, trip_request_id=None, updated_at=None):
        """Get the count of existing Transportation Bookings.

        Parameters:
            trip_request_id (str): Unique id of TripRequest object, if this value is passed it returns objects assiocated with a trip. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Transportation Bookings.
        """
        return get_request({
            'trip_request_id': trip_request_id,
            'updated_at': updated_at
        }, TransportationBookings.GET_TRANSPORTATION_BOOKINGS_COUNT, self._access_token)