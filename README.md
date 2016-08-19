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
    digitalsign.verifySignature("hello world", "hello hello:mew")
    digitalsign.verifySignature("hello world", "458d54987fd217b86fdffb1fa9387875f6fe6e82:6d521f8728e741478bb5f59c12de2037")

## Testing

    python path/to/folder/mob-digitalsign/tests/test_sign.py