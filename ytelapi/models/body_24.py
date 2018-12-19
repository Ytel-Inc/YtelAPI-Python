# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body24(object):

    """Implementation of the 'body_24' model.

    TODO: type model description here.

    Attributes:
        call_sid (string): The unique identifier for the in-progress voice
            call.
        audio_direction (AudioDirectionEnum): The direction the audio effect
            should be placed on. If IN, the effects will occur on the incoming
            audio stream. If OUT, the effects will occur on the outgoing audio
            stream.
        pitch_semi_tones (float): Set the pitch in semitone (half-step)
            intervals. Value between -14 and 14
        pitch_octaves (float): Set the pitch in octave intervals.. Value
            between -1 and 1
        pitch (float): Set the pitch (lowness/highness) of the audio. The
            higher the value, the higher the pitch. Value greater than 0
        rate (float): Set the rate for audio. The lower the value, the lower
            the rate. value greater than 0
        tempo (float): Set the tempo (speed) of the audio. A higher value
            denotes a faster tempo. Value greater than 0

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "call_sid":'CallSid',
        "audio_direction":'AudioDirection',
        "pitch_semi_tones":'PitchSemiTones',
        "pitch_octaves":'PitchOctaves',
        "pitch":'Pitch',
        "rate":'Rate',
        "tempo":'Tempo'
    }

    def __init__(self,
                 call_sid=None,
                 audio_direction=None,
                 pitch_semi_tones=None,
                 pitch_octaves=None,
                 pitch=None,
                 rate=None,
                 tempo=None):
        """Constructor for the Body24 class"""

        # Initialize members of the class
        self.call_sid = call_sid
        self.audio_direction = audio_direction
        self.pitch_semi_tones = pitch_semi_tones
        self.pitch_octaves = pitch_octaves
        self.pitch = pitch
        self.rate = rate
        self.tempo = tempo


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        call_sid = dictionary.get('CallSid')
        audio_direction = dictionary.get('AudioDirection')
        pitch_semi_tones = dictionary.get('PitchSemiTones')
        pitch_octaves = dictionary.get('PitchOctaves')
        pitch = dictionary.get('Pitch')
        rate = dictionary.get('Rate')
        tempo = dictionary.get('Tempo')

        # Return an object of this model
        return cls(call_sid,
                   audio_direction,
                   pitch_semi_tones,
                   pitch_octaves,
                   pitch,
                   rate,
                   tempo)


