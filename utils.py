from datetime import datetime

def format_time(timestamp):
    """Format thời gian"""
    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return dt.strftime('%H:%M - %d/%m/%Y')