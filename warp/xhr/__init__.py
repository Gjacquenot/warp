import flask

from . import bookings, groups, users, zone, zones

bp = flask.Blueprint("xhr", __name__)

bp.register_blueprint(bookings.bp)
bp.register_blueprint(zone.bp)
bp.register_blueprint(users.bp)
bp.register_blueprint(groups.bp)
bp.register_blueprint(zones.bp)
