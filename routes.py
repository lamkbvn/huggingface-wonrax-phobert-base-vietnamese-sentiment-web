from flask import Blueprint, render_template, request, redirect, url_for
from models import (get_all_history, get_history_by_id, add_history,
                    delete_history, clear_all_history)
from phobertbasevietnamesesentiment import predict_sentiment
from utils import format_time

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Trang chủ"""
    history = get_all_history()
    current_content = history[0] if history else None
    current_id = current_content['id'] if current_content else None

    return render_template('index.html',
                           history=history,
                           current_content=current_content,
                           current_id=current_id,
                           format_time=format_time)


@main_bp.route('/add', methods=['POST'])
def add_content():
    """Thêm nội dung mới"""
    content = request.form.get('content', '').strip()
    if content:
        sentiment =  predict_sentiment(content)
        new_id = add_history( content , sentiment)
        return redirect(url_for('main.view_content', history_id=new_id))
    return redirect(url_for('main.index'))


@main_bp.route('/view/<int:history_id>')
def view_content(history_id):
    """Xem nội dung theo ID"""
    history = get_all_history()
    current_content = get_history_by_id(history_id)

    return render_template('index.html',
                           history=history,
                           current_content=current_content,
                           current_id=history_id,
                           format_time=format_time)


@main_bp.route('/delete/<int:history_id>')
def delete_content(history_id):
    """Xóa một mục"""
    delete_history(history_id)
    return redirect(url_for('main.index'))


@main_bp.route('/clear')
def clear_history():
    """Xóa tất cả lịch sử"""
    clear_all_history()
    return redirect(url_for('main.index'))