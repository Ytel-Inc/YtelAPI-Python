# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class ConferenceController(BaseController):

    """A Controller to access Endpoints in the ytelapi API."""


    def create_list_conferences(self,
                                page=None,
                                pagesize=None,
                                friendly_name=None,
                                date_created=None):
        """Does a POST request to /conferences/listconference.json.

        Retrieve a list of conference objects.

        Args:
            page (int, optional): The page count to retrieve from the total
                results in the collection. Page indexing starts at 1.
            pagesize (int, optional): Number of individual resources listed in
                the response per page
            friendly_name (string, optional): Only return conferences with the
                specified FriendlyName
            date_created (string, optional): Conference created date

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/listconference.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': page,
            'pagesize': pagesize,
            'FriendlyName': friendly_name,
            'DateCreated': date_created
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_hangup_participant(self,
                                  participant_sid,
                                  conference_sid):
        """Does a POST request to /conferences/hangupParticipant.json.

        Remove a participant from a conference.

        Args:
            participant_sid (string): The unique identifier for a participant
                object.
            conference_sid (string): The unique identifier for a conference
                object.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/hangupParticipant.json'
        _query_parameters = {
            'ParticipantSid': participant_sid
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_play_audio(self,
                          conference_sid,
                          participant_sid,
                          audio_url):
        """Does a POST request to /conferences/playAudio.json.

        Play an audio file during a conference.

        Args:
            conference_sid (string): The unique identifier for a conference
                object.
            participant_sid (string): The unique identifier for a participant
                object.
            audio_url (AudioUrlEnum): The URL for the audio file that is to be
                played during the conference. Multiple audio files can be
                chained by using a semicolon.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/playAudio.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid,
            'ParticipantSid': participant_sid,
            'AudioUrl': audio_url
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_participants(self,
                                 conference_sid,
                                 page=None,
                                 pagesize=None,
                                 muted=None,
                                 deaf=None):
        """Does a POST request to /conferences/listParticipant.json.

        Retrieve a list of participants for an in-progress conference.

        Args:
            conference_sid (string): The unique identifier for a conference.
            page (int, optional): The page count to retrieve from the total
                results in the collection. Page indexing starts at 1.
            pagesize (int, optional): The count of objects to return per
                page.
            muted (bool, optional): Specifies if participant should be muted.
            deaf (bool, optional): Specifies if the participant should hear
                audio in the conference.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/listParticipant.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid,
            'Page': page,
            'Pagesize': pagesize,
            'Muted': muted,
            'Deaf': deaf
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_conference(self,
                          url,
                          mfrom,
                          to,
                          method=None,
                          status_call_back_url=None,
                          status_call_back_method=None,
                          fallback_url=None,
                          fallback_method=None,
                          record=None,
                          record_call_back_url=None,
                          record_call_back_method=None,
                          schedule_time=None,
                          timeout=None):
        """Does a POST request to /conferences/createConference.json.

        Here you can experiment with initiating a conference call through Ytel
        and view the request response generated when doing so.

        Args:
            url (string): URL requested once the conference connects
            mfrom (string): A valid 10-digit number (E.164 format) that will
                be initiating the conference call.
            to (string): A valid 10-digit number (E.164 format) that is to
                receive the conference call.
            method (string, optional): Specifies the HTTP method used to
                request the required URL once call connects.
            status_call_back_url (string, optional): URL that can be requested
                to receive notification when call has ended. A set of default
                parameters will be sent here once the conference is finished.
            status_call_back_method (string, optional): Specifies the HTTP
                methodlinkclass used to request StatusCallbackUrl.
            fallback_url (string, optional): URL requested if the initial Url
                parameter fails or encounters an error
            fallback_method (string, optional): Specifies the HTTP method used
                to request the required FallbackUrl once call connects.
            record (bool, optional): Specifies if the conference should be
                recorded.
            record_call_back_url (string, optional): Recording parameters will
                be sent here upon completion.
            record_call_back_method (string, optional): Specifies the HTTP
                method used to request the required URL once conference
                connects.
            schedule_time (string, optional): Schedule conference in future.
                Schedule time must be greater than current time
            timeout (int, optional): The number of seconds the call stays on
                the line while waiting for an answer. The max time limit is
                999 and the default limit is 60 seconds but lower times can be
                set.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/createConference.json'
        _query_parameters = {
            'Url': url
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': mfrom,
            'To': to,
            'Method': method,
            'StatusCallBackUrl': status_call_back_url,
            'StatusCallBackMethod': status_call_back_method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'Record': record,
            'RecordCallBackUrl': record_call_back_url,
            'RecordCallBackMethod': record_call_back_method,
            'ScheduleTime': schedule_time,
            'Timeout': timeout
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_participant(self,
                                conference_sid,
                                participant_sid):
        """Does a POST request to /conferences/viewParticipant.json.

        Retrieve information about a participant by its ParticipantSid.

        Args:
            conference_sid (string): The unique identifier for a conference
                object.
            participant_sid (string): The unique identifier for a participant
                object.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/viewParticipant.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid,
            'ParticipantSid': participant_sid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_conference(self,
                               conference_sid):
        """Does a POST request to /conferences/viewconference.json.

        Retrieve information about a conference by its ConferenceSid.

        Args:
            conference_sid (string): The unique identifier of each conference
                resource

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/viewconference.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def add_participant(self,
                        conference_sid,
                        participant_number,
                        muted=None,
                        deaf=None):
        """Does a POST request to /conferences/addParticipant.json.

        Add Participant in conference 

        Args:
            conference_sid (string): The unique identifier for a conference
                object.
            participant_number (string): The phone number of the participant
                to be added.
            muted (bool, optional): Specifies if participant should be muted.
            deaf (bool, optional): Specifies if the participant should hear
                audio in the conference.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/addParticipant.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': conference_sid,
            'ParticipantNumber': participant_number,
            'Muted': muted,
            'Deaf': deaf
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_silence_participant(self,
                                   conference_sid,
                                   participant_sid,
                                   muted=None,
                                   deaf=None):
        """Does a POST request to /conferences/deafMuteParticipant.json.

        Deaf Mute Participant

        Args:
            conference_sid (string): ID of the active conference
            participant_sid (string): ID of an active participant
            muted (bool, optional): Mute a participant
            deaf (bool, optional): Make it so a participant cant hear

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/conferences/deafMuteParticipant.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferenceSid': conference_sid,
            'ParticipantSid': participant_sid,
            'Muted': muted,
            'Deaf': deaf
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
