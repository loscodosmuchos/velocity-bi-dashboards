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

@app.route('/positioning-tool')
def positioning_tool():
    """Interactive Dashboard Positioning Tool"""
    return send_from_directory('.', 'positioning_tool.html')

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

@app.route('/api/vendor-scorecard/metrics')
def vendor_scorecard_metrics():
    """Vendor Performance Scorecard metrics"""
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'poVolume': random.randint(300, 400),
        'vendorPerformance': round(random.uniform(90, 98), 1),
        'budgetUtilization': random.randint(60, 75),
        'sowCompliance': random.randint(85, 95),
        'activeContracts': random.randint(140, 170),
        'status': 'success'
    })

@app.route('/api/workforce-hud/metrics')
def workforce_hud_metrics():
    """Workforce Holographic HUD metrics"""
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'activeContractors': random.randint(1200, 1300),
        'utilizationRate': random.randint(82, 92),
        'avgTimeToFill': random.randint(10, 15),
        'onboardingQueue': random.randint(25, 45),
        'complianceRate': random.randint(94, 98),
        'trendData': [random.randint(75, 95) for _ in range(7)],
        'status': 'success'
    })

@app.route('/api/luxury-truck/metrics')
def luxury_truck_metrics():
    """Luxury Truck Dashboard metrics"""
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'openPOs': random.randint(110, 145),
        'vendorRating': round(random.uniform(8.5, 9.2), 1),
        'spendVelocity': round(random.uniform(2.0, 2.8), 1),
        'contractCompliance': random.randint(90, 96),
        'poAverage': random.randint(17000, 20000),
        'onTimeDelivery': random.randint(88, 94),
        'invoiceAccuracy': random.randint(96, 99),
        'status': 'success'
    })

@app.route('/api/electric-car/metrics')
def electric_car_metrics():
    """Electric Car Dashboard metrics"""
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'energyEfficiency': random.randint(90, 98),
        'sustainabilityScore': random.choice(['A+', 'A', 'A-']),
        'costSavings': round(random.uniform(1.0, 1.5), 1),
        'carbonOffset': random.randint(400, 500),
        'renewableEnergy': random.randint(82, 92),
        'vendorEcoScore': round(random.uniform(8.5, 9.5), 1),
        'status': 'success'
    })

@app.route('/api/future-truck/metrics')
def future_truck_metrics():
    """Future Truck Dashboard metrics"""
    data_stream_messages = [
        'Global component demand spike',
        'Energy cost fluctuation detected',
        'Delivery delay risk assessment',
        'Smart contract execution complete',
        'Supplier credit rating change'
    ]
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'aiPredictionAccuracy': round(random.uniform(97.5, 99.2), 1),
        'autonomousSourcing': random.randint(145, 170),
        'fleetUtilization': [random.randint(75, 95) for _ in range(7)],
        'supplyChainResilience': random.randint(88, 95),
        'riskDetection': random.randint(2, 5),
        'dataStream': '... '.join(random.sample(data_stream_messages, 3)) + '...',
        'status': 'success'
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Velocity Dashboard API',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'dashboards_available': 15
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
