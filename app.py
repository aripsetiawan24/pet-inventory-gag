from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import json
import os

app = Flask(__name__)

# Admin credentials
ADMIN_USERNAME = 'jawir'
ADMIN_PASSWORD = 'jawirlu'

# Trade username - dapat diubah sesuai kebutuhan
TRADE_USERNAME = 'jawir'

# File untuk menyimpan data inventory
INVENTORY_FILE = 'inventory.json'

def load_inventory():
    """Load inventory data from JSON file"""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    else:
        # Default inventory data
        default_inventory = {
            "pet_age_60": {"name": "Pet Age 60", "quantity": 0},
            "pet_age_70": {"name": "Pet Age 70", "quantity": 0},
            "pet_age_75": {"name": "Pet Age 75", "quantity": 0}
        }
        save_inventory(default_inventory)
        return default_inventory

def save_inventory(inventory):
    """Save inventory data to JSON file"""
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)

@app.route('/')
def index():
    """Main inventory display page"""
    inventory = load_inventory()
    return render_template('index.html', inventory=inventory)

@app.route('/trade')
def trade():
    """Trade offers page"""
    return render_template('trade.html', username=TRADE_USERNAME)

@app.route('/admin')
def admin():
    """Admin panel page"""
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
    inventory = load_inventory()
    return render_template('admin.html', inventory=inventory)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Login berhasil!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Username atau password salah!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    flash('Logout berhasil!', 'success')
    return redirect(url_for('index'))

@app.route('/reset_stock', methods=['POST'])
def reset_stock():
    """Reset all stock to default values"""
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    default_inventory = {
        "pet_age_60": {"name": "Pet Age 60", "quantity": 0},
        "pet_age_70": {"name": "Pet Age 70", "quantity": 0},
        "pet_age_75": {"name": "Pet Age 75", "quantity": 0}
    }
    save_inventory(default_inventory)
    flash('Stock berhasil direset!', 'success')
    return redirect(url_for('admin'))

@app.route('/update_stock', methods=['POST'])
def update_stock():
    """Update stock quantity"""
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
        
    product_id = request.form.get('product_id')
    action = request.form.get('action')
    quantity = int(request.form.get('quantity'))
    
    inventory = load_inventory()
    
    if product_id in inventory:
        if action == 'subtract':
            quantity_change = -quantity
        else:  # add
            quantity_change = quantity
            
        new_quantity = inventory[product_id]['quantity'] + quantity_change
        if new_quantity >= 0:
            inventory[product_id]['quantity'] = new_quantity
            save_inventory(inventory)
            action_text = 'dikurangi' if action == 'subtract' else 'ditambah'
            flash(f'Stock {inventory[product_id]["name"]} berhasil {action_text} {quantity}!', 'success')
        else:
            flash('Stock tidak bisa kurang dari 0!', 'error')
    else:
        flash('Produk tidak ditemukan!', 'error')
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
