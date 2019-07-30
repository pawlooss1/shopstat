import loader
import os


def save_receipt(receipt):
    root = os.getcwd()
    receipt_path = build_path_from_date(receipt.date)
    safe_dir_change(receipt_path)


def build_path_from_date(date):
    return str(date).replace('-', '/')


def safe_dir_change(path):
    pass
