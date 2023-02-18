TO DO:

* check for keys and datatypes in response
* schema validation

* pytest exceptions - pytest raises
* add negative paths for tests - ie. string in id


TO READ:

* pytest parametrize

TO CLARIFY:

* how to operate on models -> from User to UserDb -> TypeError: Schema.load() got an unexpected keyword argument 'session'
* better way to create swagger docs
* validation for not needed fields -> check_extra_fields method


-- notes --

* validate what came from API - routes level -> done in pydantic - is this okay?
* api serializers - validation (one/two files - what comes in and comes out) - try with pydantic

use pydantic objects ONLY to validate and serialize to inner model - models.py
