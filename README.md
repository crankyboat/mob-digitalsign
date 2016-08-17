# mob-digitalsign

## Typical Usage

    #!/usr/bin/env python

    import digitalsign

    digitalsign.createSignature("hello world")
    digitalsign.verifySignature("hello world", "hello hello")
    digitalsign.verifySignature("hello world", "27fa4c2ccc38d7069d8cccb876e462d09134ebfc")