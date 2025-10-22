import os
import logging
from bottle import route, run, template, request, redirect, static_file
from database import init_db, get_services, create_booking

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)


# --- Time Slots Generation ---
def get_time_slots():
    """Generates a list of time slots for the booking form."""
    slots = []
    for hour in range(9, 18):
        slots.append(f'{hour:02d}:00')
        slots.append(f'{hour:02d}:30')
    return slots


@route('/static/<filepath:path>')
def server_static(filepath):
    root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    return static_file(filepath, root=root_path)


@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='static')


# --- Routes ---
@route('/')
def index():
    """Renders the main booking page."""
    logging.info('Main page accessed.')
    try:
        services = get_services()
        # return template('prenota.html', services=services, slots=get_time_slots())
        return template(
            'booking',
            title='JoyBooking - Quick Salon Booking Success',
            services=services,
            slots=get_time_slots(),
        )

    except Exception as e:
        logging.error(f'Error fetching services for index page: {e}')
        return 'Error loading page. Please try again later.'


@route('/book', method='POST')
def book():
    """Handles the booking form submission."""
    client_name = request.forms.get('client_name')
    client_phone = request.forms.get('client_phone')
    service_id = request.forms.get('service_id')
    slot = request.forms.get('slot')

    if create_booking(client_name, client_phone, service_id, slot):
        return redirect('/success')
    else:
        return 'Error creating booking. Please try again later.'


@route('/success')
def success():
    return template('success', title='JoyBooking - Quick Salon Booking Success')


# --- Main ---
if __name__ == '__main__':
    init_db()
    logging.info('Starting server at http://localhost:8080')
    run(host='localhost', port=8080, debug=True)
