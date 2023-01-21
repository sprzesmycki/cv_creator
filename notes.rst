TO DO:

* check if patched response looks as expected
* hardcode user and check returned value
* check for keys and datatypes in response
* schema validation

TO READ:

* pytest parametrize



pytest raises

error handler -> json with details
404 -> json page not found "message"
500 -> json internal server error
status code stays the same - just extra message


rewrite serializers using marshmallow instead of marshmallow_sqlalchemy

return multiple types -> use Optional

add if to get_user_by_user_id when user is None