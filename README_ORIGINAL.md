# Velocity BI Dashboards - Replit Deployment

Luxury supercar-inspired business intelligence dashboards with photorealistic aesthetics and real-time data updates.

## 🚀 Quick Start on Replit

### Method 1: Import from GitHub

1. **Push this repository to GitHub** (see instructions below)
2. **Go to [Replit](https://replit.com)**
3. Click **"Create Repl"** → **"Import from GitHub"**
4. Paste your GitHub repository URL
5. Click **"Import from GitHub"**
6. Replit will automatically detect the Python environment and install dependencies
7. Click **"Run"** button
8. Your dashboards will be live!

### Method 2: Upload Files Directly

1. **Go to [Replit](https://replit.com)**
2. Click **"Create Repl"** → **"Python"**
3. Upload all files from this package:
   - `app.py`
   - `requirements.txt`
   - `.replit`
   - `templates/` folder (with all HTML files)
   - `dashboards/` folder (with all .webp images)
4. Click **"Run"** button
5. Your dashboards will be live!

---

## 📁 File Structure

```
velocity-bi-dashboards/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .replit                         # Replit configuration
├── README.md                       # This file
├── templates/                      # HTML templates
│   ├── index.html                  # Dashboard selector
│   ├── compliance.html             # Compliance & Risk Monitor
│   ├── procurement.html            # Procurement Performance
│   ├── velocity.html               # Procurement Velocity Monitor
│   ├── workforce.html              # Workforce Analytics
│   └── executive.html              # Executive Summary
└── dashboards/                     # Dashboard background images
    ├── compliance_risk_generated.webp
    ├── procurement_performance_generated.webp
    ├── velocity_monitor_generated.webp
    ├── workforce_analytics_generated.webp
    └── executive_summary_generated.webp
```

---

## 🎯 Features

### 5 Luxury Dashboards

1. **Compliance & Risk Monitor**
   - 5 circular gauges with automotive-grade design
   - Real-time compliance tracking
   - Color-coded risk indicators

2. **Procurement Performance**
   - Vintage burled wood aesthetic
   - Core KPIs: PO Volume, Spend Rate, Vendor Count
   - Brass-bezeled gauges

3. **Procurement Velocity Monitor**
   - Futuristic HUD with neon accents
   - Purchase order velocity tracking
   - Budget burn rate visualization

4. **Workforce Analytics**
   - Industrial metal command center
   - Contractor utilization metrics
   - Time-to-fill and placement tracking

5. **Executive Summary**
   - Mixed premium materials (carbon fiber, wood, metal)
   - Strategic overview of all key metrics
   - High-level performance indicators

### METHOD 3 Implementation

- **Photorealistic backgrounds** - Luxury supercar instrument cluster aesthetics
- **Live data overlays** - Real-time updates every 30 seconds
- **Smooth animations** - Value changes flash with subtle effects
- **REST API backend** - Flask endpoints for all metrics
- **Responsive design** - Works on desktop, tablet, mobile

---

## 🔧 Configuration

### Environment Variables (Optional)

Replit automatically handles most configuration, but you can add custom variables in the Replit "Secrets" tab:

- `PORT` - Server port (default: 5000)
- `FLASK_ENV` - Environment (development/production)

---

## 📡 API Endpoints

All endpoints return JSON data:

- `GET /api/compliance/metrics` - Compliance & Risk Monitor data
- `GET /api/procurement/performance` - Procurement Performance data
- `GET /api/procurement/velocity` - Procurement Velocity data
- `GET /api/workforce/analytics` - Workforce Analytics data
- `GET /api/executive/summary` - Executive Summary data
- `GET /api/health` - Health check

### Example API Call

```bash
curl https://your-repl-name.your-username.repl.co/api/compliance/metrics
```

**Response:**
```json
{
  "openExceptions": 12,
  "sowViolations": 38,
  "complianceScore": 92,
  "certificationGaps": 7,
  "auditStatus": 3,
  "timestamp": "2025-01-15T10:30:00",
  "status": "success"
}
```

---

## 🎨 Customization

### Change Update Frequency

Edit the `UPDATE_INTERVAL` in each dashboard HTML file:

```javascript
const UPDATE_INTERVAL = 30000; // 30 seconds (change to desired milliseconds)
```

### Adjust Data Positioning

Fine-tune gauge value positions in the CSS:

```css
.gauge-1-value {
    top: 52%;      /* Adjust vertical position */
    left: 12%;     /* Adjust horizontal position */
    font-size: 4rem; /* Adjust size */
}
```

### Connect to Real Database

Replace mock data in `app.py` with actual database queries:

```python
import psycopg2

@app.route('/api/compliance/metrics')
def get_compliance_metrics():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM compliance_metrics ORDER BY created_at DESC LIMIT 1")
    data = cur.fetchone()
    # ... process and return data
```

---

## 🚀 Deployment

### Replit Deployment (Automatic)

1. Click the **"Deploy"** button in Replit
2. Choose deployment type (Reserved VM or Autoscale)
3. Your dashboard will get a permanent URL
4. Share with your team!

### Custom Domain

1. In Replit, go to **"Deployments"** tab
2. Click **"Add Custom Domain"**
3. Follow DNS configuration instructions
4. Your dashboards will be available at your custom domain

---

## 🔒 Security Recommendations

### For Production Use:

1. **Add Authentication**
   ```python
   from flask_httpauth import HTTPBasicAuth
   auth = HTTPBasicAuth()
   
   @app.route('/dashboard/compliance')
   @auth.login_required
   def compliance_dashboard():
       return render_template('compliance.html')
   ```

2. **Enable HTTPS**
   - Replit deployments automatically use HTTPS
   - For custom domains, ensure SSL certificate is configured

3. **Add Rate Limiting**
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app, default_limits=["200 per day", "50 per hour"])
   ```

4. **Use Environment Variables for Secrets**
   - Store API keys in Replit Secrets
   - Never commit sensitive data to Git

---

## 📊 Dashboard Images

### Important: Add Your Dashboard Images

The `dashboards/` folder should contain these files:

- `compliance_risk_generated.webp`
- `procurement_performance_generated.webp`
- `velocity_monitor_generated.webp`
- `workforce_analytics_generated.webp`
- `executive_summary_generated.webp`

**Download these from your Manus slides presentation and upload to the `dashboards/` folder in Replit.**

---

## 🐛 Troubleshooting

### Dashboard images not showing
**Solution:** Ensure all `.webp` files are uploaded to the `dashboards/` folder

### API returning errors
**Solution:** Check Replit console for error messages. Ensure Flask is running.

### Data not updating
**Solution:** Check browser console (F12) for JavaScript errors. Verify API endpoints are accessible.

### Port already in use
**Solution:** Replit handles ports automatically. If issues persist, restart the Repl.

---

## 📝 GitHub Push Instructions

### Push to GitHub

```bash
# Navigate to the package directory
cd /path/to/replit_package

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Velocity BI Dashboards"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/velocity-bi-dashboards.git

# Push to GitHub
git push -u origin master
```

### Then Import to Replit

1. Go to [Replit](https://replit.com)
2. Click "Create Repl" → "Import from GitHub"
3. Paste: `https://github.com/yourusername/velocity-bi-dashboards`
4. Click "Import from GitHub"
5. Click "Run"

---

## 🎯 Next Steps

1. **Upload dashboard images** to `dashboards/` folder
2. **Test all dashboards** by clicking through the selector
3. **Customize data sources** by connecting to your database
4. **Deploy to production** using Replit's deployment feature
5. **Share with your team** using the Replit URL

---

## 📞 Support

For issues or questions:
- Check the troubleshooting section above
- Review Flask and Replit documentation
- Inspect browser console for JavaScript errors
- Check Replit console for Python errors

---

## 📄 License

MIT License - Free to use and modify for your projects.

---

**Velocity Dashboard System v1.0.0**  
*Luxury Supercar-Inspired Business Intelligence*
