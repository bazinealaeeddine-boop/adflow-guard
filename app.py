from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError
from celery import Celery

app = Flask(__name__)

# Configuration Celery (Redis local)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

class EventSchema(Schema):
    event_id = fields.Str(required=True)
    event_name = fields.Str(required=True)
    user_data = fields.Dict(required=True)
    platforms = fields.List(fields.Str(), required=True)

@app.route('/api/v1/events', methods=['POST'])
def ingest_events():
    data = request.get_json()
    if not data or 'events' not in data:
        return jsonify({"error": "Missing events"}), 400

    schema = EventSchema()
    validated = []
    for ev in data['events']:
        try:
            validated.append(schema.load(ev))
        except ValidationError as err:
            return jsonify({"error": err.messages}), 422

    for ev in validated:
        process_event.delay(ev)

    return jsonify({
        "received": True,
        "event_count": len(validated),
        "details": [{"event_id": e['event_id'], "status": "queued"} for e in validated]
    }), 202

@celery.task
def process_event(event):
    # Hna ghadi yconnecta m3a Facebook/Google moraha
    print(f"Processing event {event['event_id']} for platforms {event['platforms']}")
    return True