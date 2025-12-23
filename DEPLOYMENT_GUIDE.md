# Deployment Guide - Replit & GitHub

Complete step-by-step guide for deploying Velocity BI Dashboards to Replit via GitHub.

---

## 📋 Table of Contents

1. [GitHub Setup](#github-setup)
2. [Push to GitHub](#push-to-github)
3. [Import to Replit](#import-to-replit)
4. [Configure Replit](#configure-replit)
5. [Deploy to Production](#deploy-to-production)
6. [Custom Domain Setup](#custom-domain-setup)
7. [Troubleshooting](#troubleshooting)

---

## GitHub Setup

### Step 1: Create GitHub Repository

1. **Go to [GitHub](https://github.com)**
2. Click **"New repository"** (green button, top-right)
3. **Repository settings:**
   - Name: `velocity-bi-dashboards`
   - Description: `Luxury supercar-inspired BI dashboards with METHOD 3`
   - Visibility: **Public** (or Private if you have Pro)
   - ✅ **DO NOT** initialize with README (we already have one)
   - ✅ **DO NOT** add .gitignore (we already have one)
   - ✅ **DO NOT** choose a license (optional)
4. Click **"Create repository"**

### Step 2: Note Your Repository URL

After creation, you'll see a URL like:
```
https://github.com/YOUR_USERNAME/velocity-bi-dashboards.git
```

**Save this URL** - you'll need it in the next step.

---

## Push to GitHub

### Option A: Using Command Line (Recommended)

#### 1. Navigate to Package Directory

```bash
cd /path/to/replit_package
```

#### 2. Verify Git Status

```bash
git status
```

You should see all files staged and ready to commit.

#### 3. Commit Files

```bash
git commit -m "Initial commit: Velocity BI Dashboards with METHOD 3 implementation"
```

#### 4. Rename Branch to Main (Optional but Recommended)

```bash
git branch -M main
```

#### 5. Add Remote Repository

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/velocity-bi-dashboards.git
```

#### 6. Push to GitHub

```bash
git push -u origin main
```

**If prompted for credentials:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your password)

**How to create a Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (full control of private repositories)
4. Click "Generate token"
5. **Copy the token** (you won't see it again!)
6. Use this token as your password when pushing

#### 7. Verify Upload

Go to your GitHub repository URL in a browser. You should see all your files!

---

### Option B: Using GitHub Desktop (Easier for Beginners)

#### 1. Download GitHub Desktop

- Go to [desktop.github.com](https://desktop.github.com)
- Download and install

#### 2. Sign In

- Open GitHub Desktop
- Sign in with your GitHub account

#### 3. Add Repository

- File → Add Local Repository
- Choose your `replit_package` folder
- Click "Add Repository"

#### 4. Publish Repository

- Click "Publish repository" button
- Name: `velocity-bi-dashboards`
- Description: `Luxury BI dashboards`
- ✅ Keep code private (optional)
- Click "Publish repository"

Done! Your code is now on GitHub.

---

## Import to Replit

### Step 1: Go to Replit

1. **Open [Replit](https://replit.com)** in your browser
2. **Sign in** (or create account if needed)

### Step 2: Import from GitHub

1. Click **"Create Repl"** button (top-left or center)
2. Select **"Import from GitHub"** tab
3. **Paste your GitHub repository URL:**
   ```
   https://github.com/YOUR_USERNAME/velocity-bi-dashboards
   ```
4. Click **"Import from GitHub"**

### Step 3: Wait for Import

Replit will:
- ✅ Clone your repository
- ✅ Detect Python environment
- ✅ Install dependencies from `requirements.txt`
- ✅ Configure based on `.replit` file

This takes **1-2 minutes**.

### Step 4: Run the Application

1. Click the **"Run"** button (big green button at top)
2. Replit will:
   - Install Flask, Flask-CORS, gunicorn
   - Start the Flask server
   - Open a preview window
3. You should see: **"Velocity Executive Command Center"**

**Congratulations!** Your dashboards are now live on Replit.

---

## Configure Replit

### Access Your Dashboard

Your Replit will have a URL like:
```
https://velocity-bi-dashboards.YOUR_USERNAME.repl.co
```

This URL is:
- ✅ **Public** (anyone can access)
- ✅ **Always available** (as long as Repl is running)
- ✅ **Free tier** (with some limitations)

### Keep Repl Always Running (Optional)

**Free tier:** Repl sleeps after inactivity  
**Paid tier:** Can enable "Always On"

To enable Always On:
1. Click your Repl name (top-left)
2. Go to "Settings" tab
3. Find "Always On" toggle
4. Enable (requires Replit Pro subscription)

---

## Deploy to Production

### Why Deploy?

Development Repl vs. Deployed Repl:

| Feature | Development | Deployed |
|---------|------------|----------|
| URL | Changes with each session | Permanent |
| Uptime | Sleeps after inactivity | Always on |
| Performance | Shared resources | Dedicated resources |
| Custom domain | ❌ No | ✅ Yes |
| SSL/HTTPS | ✅ Yes | ✅ Yes |

### Step 1: Create Deployment

1. In your Repl, click **"Deploy"** button (top-right, rocket icon)
2. Choose deployment type:
   - **Reserved VM** (recommended for production)
   - **Autoscale** (scales automatically with traffic)
3. Click **"Deploy"**

### Step 2: Configure Deployment

**Reserved VM Settings:**
- vCPUs: 0.5 (sufficient for dashboards)
- Memory: 512 MB (sufficient for Flask)
- Region: Choose closest to your users

**Autoscale Settings:**
- Min instances: 1
- Max instances: 3
- Region: Choose closest to your users

### Step 3: Deploy

1. Review settings
2. Click **"Deploy"**
3. Wait 2-3 minutes for deployment

### Step 4: Get Production URL

After deployment, you'll get a permanent URL:
```
https://velocity-bi-dashboards-production.YOUR_USERNAME.repl.co
```

This URL:
- ✅ Never changes
- ✅ Always available
- ✅ Better performance
- ✅ Can add custom domain

---

## Custom Domain Setup

### Prerequisites

- Deployed Repl (see above)
- Custom domain (e.g., `dashboards.yourcompany.com`)
- Access to domain DNS settings

### Step 1: Add Domain in Replit

1. Go to your deployed Repl
2. Click **"Deployments"** tab
3. Click **"Add Custom Domain"**
4. Enter your domain: `dashboards.yourcompany.com`
5. Click **"Add Domain"**

### Step 2: Configure DNS

Replit will show you DNS records to add. Example:

**CNAME Record:**
```
Type: CNAME
Name: dashboards
Value: velocity-bi-dashboards-production.YOUR_USERNAME.repl.co
TTL: 3600
```

### Step 3: Add DNS Records

**For Cloudflare:**
1. Go to Cloudflare dashboard
2. Select your domain
3. Go to DNS → Records
4. Click "Add record"
5. Type: CNAME
6. Name: `dashboards`
7. Target: (paste Replit value)
8. Proxy status: Proxied (orange cloud)
9. Click "Save"

**For GoDaddy:**
1. Go to GoDaddy DNS Management
2. Click "Add" → CNAME
3. Host: `dashboards`
4. Points to: (paste Replit value)
5. TTL: 1 Hour
6. Click "Save"

**For Namecheap:**
1. Go to Domain List → Manage
2. Advanced DNS tab
3. Add New Record → CNAME
4. Host: `dashboards`
5. Value: (paste Replit value)
6. TTL: Automatic
7. Click "Save"

### Step 4: Wait for DNS Propagation

- **Typical time:** 5-30 minutes
- **Maximum time:** 24-48 hours
- **Check status:** Use [dnschecker.org](https://dnschecker.org)

### Step 5: Verify

1. Visit your custom domain: `https://dashboards.yourcompany.com`
2. You should see your Velocity dashboards
3. SSL certificate is automatically provided by Replit

---

## Troubleshooting

### Issue: "Import failed" on Replit

**Cause:** GitHub repository is private and Replit doesn't have access

**Solution:**
1. Make repository public, OR
2. Connect GitHub account to Replit:
   - Replit Settings → Connected services → GitHub → Connect

---

### Issue: "Module not found" errors

**Cause:** Dependencies not installed

**Solution:**
```bash
# In Replit Shell, run:
pip install -r requirements.txt
```

---

### Issue: Dashboard images not loading

**Cause:** Images not uploaded or wrong path

**Solution:**
1. Verify images exist: Check `dashboards/` folder in Replit file tree
2. Check image paths in HTML templates:
   ```html
   background-image: url('/dashboards/compliance_risk_generated.webp');
   ```
3. Ensure images are committed to Git:
   ```bash
   git add dashboards/*.webp
   git commit -m "Add dashboard images"
   git push
   ```

---

### Issue: "Port 5000 is already in use"

**Cause:** Multiple Flask instances running

**Solution:**
1. Stop all running processes in Replit
2. Click "Run" again
3. Or change port in `app.py`:
   ```python
   port = int(os.environ.get('PORT', 5001))  # Changed to 5001
   ```

---

### Issue: API returning 404 errors

**Cause:** Endpoint not defined or wrong path

**Solution:**
1. Check endpoint exists in `app.py`:
   ```python
   @app.route('/api/compliance/metrics')
   def get_compliance_metrics():
       # ...
   ```
2. Verify JavaScript is calling correct path:
   ```javascript
   fetch(`${API_BASE_URL}/compliance/metrics`)
   ```
3. Test endpoint directly:
   ```
   https://your-repl.repl.co/api/compliance/metrics
   ```

---

### Issue: Custom domain not working

**Cause:** DNS not propagated or misconfigured

**Solution:**
1. Wait 30 minutes for DNS propagation
2. Check DNS records with [dnschecker.org](https://dnschecker.org)
3. Verify CNAME record:
   ```
   Type: CNAME
   Name: dashboards (or @)
   Value: your-repl-production.username.repl.co
   ```
4. Disable proxy in Cloudflare temporarily (gray cloud)
5. Clear browser cache and try again

---

### Issue: Repl keeps sleeping

**Cause:** Free tier limitation

**Solutions:**
1. **Upgrade to Replit Pro** (Always On feature)
2. **Use UptimeRobot** (free service):
   - Sign up at [uptimerobot.com](https://uptimerobot.com)
   - Add monitor with your Repl URL
   - Ping interval: 5 minutes
   - This keeps your Repl awake
3. **Deploy to production** (Reserved VM never sleeps)

---

### Issue: Slow performance

**Cause:** Free tier resource limits

**Solutions:**
1. **Deploy to Reserved VM** (dedicated resources)
2. **Optimize images:**
   ```bash
   # Compress images to < 500KB each
   # Use WebP format
   # Reduce resolution if needed
   ```
3. **Enable caching:**
   ```python
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   
   @app.route('/api/compliance/metrics')
   @cache.cached(timeout=30)
   def get_compliance_metrics():
       # ...
   ```

---

## Deployment Checklist

Before deploying to production:

- [ ] All dashboard images uploaded and optimized
- [ ] All API endpoints tested and working
- [ ] All dashboards accessible from selector
- [ ] Data updates working (30-second interval)
- [ ] Back buttons navigate correctly
- [ ] No console errors in browser DevTools
- [ ] Tested on desktop and mobile
- [ ] README.md updated with project details
- [ ] Sensitive data moved to environment variables
- [ ] Git repository pushed to GitHub
- [ ] Replit import successful
- [ ] Development Repl running correctly
- [ ] Production deployment created
- [ ] Custom domain configured (if applicable)
- [ ] SSL certificate working (HTTPS)
- [ ] Performance tested under load

---

## Post-Deployment

### Monitor Your Dashboards

1. **Replit Analytics**
   - View in Deployments tab
   - Track requests, errors, uptime

2. **External Monitoring**
   - Use UptimeRobot for uptime monitoring
   - Set up alerts for downtime

3. **Error Tracking**
   - Check Replit logs regularly
   - Monitor browser console for client errors

### Update Your Dashboards

**To deploy updates:**

1. **Make changes locally**
2. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Update dashboard styling"
   git push
   ```
3. **Pull in Replit:**
   - Open Replit Shell
   - Run: `git pull origin main`
   - Restart the Repl

**Or use Replit's GitHub integration:**
- Replit automatically syncs with GitHub
- Changes appear within minutes

---

## Summary

**Quick Deployment Path:**

```
1. Create GitHub repo
   ↓
2. Push code to GitHub
   ↓
3. Import to Replit
   ↓
4. Click "Run"
   ↓
5. Test dashboards
   ↓
6. Click "Deploy"
   ↓
7. Add custom domain (optional)
   ↓
8. Share with team!
```

**Total time:** 15-30 minutes from start to production.

---

**Need help?** Check the troubleshooting section or review Replit's documentation at [docs.replit.com](https://docs.replit.com).
