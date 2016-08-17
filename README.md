# mob-digitalsign

## Description

    Library has two methods
    1. createSignature(input_string) - returns hexdigest
    2. verifySignature(input_string, hexdigest) - returns True or False

## Installation

    pip install path/to/folder/mob-digitalsign/

## Typical Usage

    #!/usr/bin/env python

    import digitalsign

    digitalsign.createSignature("hello world")
    digitalsign.verifySignature("hello world", "hello hello")
    digitalsign.verifySignature("hello world", "27fa4c2ccc38d7069d8cccb876e462d09134ebfc")

## Testing

    python path/to/folder/mob-digitalsign/tests/test_sign.py