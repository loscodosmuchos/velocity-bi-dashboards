"""
Velocity BI Dashboard - Replit Deployment
Luxury Supercar-Inspired Business Intelligence Dashboards
"""

from flask import Flask, jsonify, send_from_directory, render_template
from flask_cors import CORS
from datetime import datetime
import random
import os

app = Flask(__name__)
CORS(app)

# ============================================================================
# SERVE DASHBOARD HTML PAGES
# ============================================================================

@app.route('/')
def index():
    """Home page with dashboard selector"""
    return render_template('index.html')

@app.route('/dashboard/compliance')
def compliance_dashboard():
    """Compliance & Risk Monitor Dashboard"""
    return render_template('compliance.html')

@app.route('/dashboard/procurement')
def procurement_dashboard():
    """Procurement Performance Dashboard"""
    return render_template('procurement.html')

@app.route('/dashboard/velocity')
def velocity_dashboard():
    """Procurement Velocity Monitor Dashboard"""
    return render_template('velocity.html')

@app.route('/dashboard/workforce')
def workforce_dashboard():
    """Workforce Analytics Dashboard"""
    return render_template('workforce.html')

@app.route('/dashboard/executive')
def executive_dashboard():
    """Executive Summary Dashboard"""
    return render_template('executive.html')

# ============================================================================
# SERVE DASHBOARD IMAGES
# ============================================================================

@app.route('/dashboards/<path:filename>')
def serve_dashboard_image(filename):
    """Serve dashboard background images"""
    return send_from_directory('dashboards', filename)

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/compliance/metrics')
def get_compliance_metrics():
    """Compliance & Risk Monitor metrics"""
    return jsonify({
        'openExceptions': random.randint(8, 15),
        'sowViolations': random.randint(30, 45),
        'complianceScore': random.randint(88, 95),
        'certificationGaps': random.randint(5, 10),
        'auditStatus': random.randint(2, 5),
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/procurement/performance')
def get_procurement_performance():
    """Procurement Performance metrics"""
    return jsonify({
        'poVolume': random.randint(150, 250),
        'spendRate': random.randint(80, 120),
        'vendorCount': random.randint(140, 180),
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/procurement/velocity')
def get_procurement_velocity():
    """Procurement Velocity metrics"""
    current_velocity = random.randint(115, 135)
    return jsonify({
        'purchaseOrderVelocity': {
            'current': current_velocity,
            'target': 125,
            'trend': '+15%' if current_velocity > 125 else '-5%',
            'status': 'STABLE'
        },
        'vendorComplianceRate': {
            'compliance': random.randint(90, 98),
            'complianceScore': random.randint(88, 95),
            'violations': random.randint(25000, 35000),
            'auditGrade': random.choice(['A+', 'A', 'A-'])
        },
        'budgetBurnRate': {
            'dailySpend': random.randint(140000, 160000),
            'monthlyForecast': random.randint(4200000, 4800000),
            'variance': random.randint(-8, 2),
            'status': 'ON TRACK'
        },
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/workforce/analytics')
def get_workforce_analytics():
    """Workforce Analytics metrics"""
    return jsonify({
        'contractorUtilization': {
            'percentage': round(random.uniform(75.0, 85.0), 1),
            'capacity': random.randint(80, 90)
        },
        'timeToFill': {
            'days': random.randint(18, 26),
            'average': 22,
            'target': 18,
            'trend': 'up'
        },
        'onboardingPipeline': {
            'total': random.randint(100, 140),
            'pending': random.randint(25, 35),
            'inProgress': random.randint(55, 70),
            'status': 'alert'
        },
        'activePlacements': {
            'total': random.randint(440, 470),
            'thirtyDayChange': random.randint(10, 20),
            'trend': 'up'
        },
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/executive/summary')
def get_executive_summary():
    """Executive Summary metrics"""
    return jsonify({
        'totalProcurementSpend': {
            'annual': 2040000,
            'currency': 'USD'
        },
        'activeVendors': {
            'count': random.randint(160, 170),
            'ytdChange': random.randint(10, 15)
        },
        'complianceRate': {
            'percentage': random.randint(90, 95),
            'status': 'HIGH'
        },
        'workforceUtilization': {
            'percentage': round(random.uniform(76.0, 82.0), 1)
        },
        'budgetHealth': {
            'status': random.choice(['ON TRACK', 'AT RISK', 'AHEAD']),
            'variance': random.randint(-5, 3)
        },
        'timestamp': datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Velocity Dashboard API',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error'
    }), 404

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
