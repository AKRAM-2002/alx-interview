#!/usr/bin/python3
"""A script that validates UTF-8 encoding."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Validates UTF-8 encoding."""
    # Number of continuation bytes needed
    continuation_bytes = 0

    for byte in data:
        # Mask the byte to get the 8 least significant bits
        byte = byte & 0xFF

        # Get binary representation of the byte, padded to 8 bits
        lead_byte_bin = bin(byte)[2:].zfill(8)

        if continuation_bytes == 0:
            # Determine the number of continuation bytes needed based on the
            # lead byte
            if lead_byte_bin[0] == '0':  # 1-byte character (ASCII)
                continue
            elif lead_byte_bin[:3] == '110':  # 2-byte character
                continuation_bytes = 1
            elif lead_byte_bin[:4] == '1110':  # 3-byte character
                continuation_bytes = 2
            elif lead_byte_bin[:5] == '11110':  # 4-byte character
                continuation_bytes = 3
            else:
                return False  # Invalid UTF-8 lead byte
        else:
            # Check if the byte is a valid continuation byte
            if lead_byte_bin[:2] != '10':
                return False
            # Decrease the continuation byte counter
            continuation_bytes -= 1

    # Ensure there are no remaining continuation bytes required
    return continuation_bytes == 0
