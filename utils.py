import json\nfrom flask import jsonify\nfrom werkzeug.exceptions import HTTPException\n\n\ndef handle_exception(e):\n    