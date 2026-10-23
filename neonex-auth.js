/**
 * NeoNeX MindX — Unified Authentication & Role-Based Access Control (RBAC) System
 * Centralized security gateway for CRM, CMS, and Digital Marketing Dashboard.
 */

(function (window) {
  'use strict';

  const STORAGE_USERS = 'neonex_rbac_users';
  const STORAGE_SESSION = 'neonex_active_session';

  // System Authorized Core Users (Always synced and guaranteed on all devices/browsers)
  const SEED_USERS = [
    {
      id: 'user-admin-neeraj',
      name: 'Neeraj',
      username: 'Neeraj',
      email: 'pcneeraj123@gmail.com',
      password: 'Hsc19ph0040@',
      role: 'Admin', // Admin | Editor | Viewer
      permissions: {
        crm: true,
        cms: true,
        marketing: true
      },
      createdAt: '2026-10-17T00:00:00.000Z'
    },
    {
      id: 'user-admin-puneeth',
      name: 'Puneeth',
      username: 'puneeth',
      email: 'puneeth@neonexmindx.com',
      password: 'puneeth$123',
      role: 'Admin',
      permissions: {
        crm: true,
        cms: true,
        marketing: true
      },
      createdAt: '2026-10-23T00:00:00.000Z'
    },
    {
      id: 'user-editor-mercy',
      name: 'Mercy',
      username: 'mercy',
      email: 'mercy@neonexmindx.com',
      password: 'mercy$123',
      role: 'Editor',
      permissions: {
        crm: true,
        cms: false,
        marketing: false
      },
      createdAt: '2026-10-23T00:00:00.000Z'
    }
  ];

  const DEFAULT_ADMIN = SEED_USERS[0];

  const NeonexAuth = {
    currentPortal: 'crm', // crm | cms | marketing

    init(portalKey = 'crm') {
      this.currentPortal = portalKey;
      this.ensureDefaultUsers();
      this.injectStyles();
    },

    ensureDefaultUsers() {
      let users = this.getUsers();
      if (!users || users.length === 0) {
        users = [...SEED_USERS];
        localStorage.setItem(STORAGE_USERS, JSON.stringify(users));
        return;
      }

      // Sync and guarantee all SEED_USERS exist and have correct passwords/permissions across all browsers
      SEED_USERS.forEach(seedUser => {
        const idx = users.findIndex(u => 
          (u.username && u.username.toLowerCase() === seedUser.username.toLowerCase()) ||
          (u.email && seedUser.email && u.email.toLowerCase() === seedUser.email.toLowerCase())
        );

        if (idx >= 0) {
          // Update credentials and permissions to match system definitions
          users[idx].username = seedUser.username;
          users[idx].name = seedUser.name || users[idx].name;
          users[idx].password = seedUser.password;
          users[idx].role = seedUser.role;
          users[idx].permissions = { ...seedUser.permissions };
        } else {
          users.push({ ...seedUser });
        }
      });

      localStorage.setItem(STORAGE_USERS, JSON.stringify(users));
    },

    getUsers() {
      try {
        const raw = localStorage.getItem(STORAGE_USERS);
        return raw ? JSON.parse(raw) : [];
      } catch (e) {
        return [DEFAULT_ADMIN];
      }
    },

    saveUsers(users) {
      localStorage.setItem(STORAGE_USERS, JSON.stringify(users));
    },

    getSession() {
      try {
        const raw = localStorage.getItem(STORAGE_SESSION);
        if (!raw) return null;
        const session = JSON.parse(raw);
        // Verify user still exists
        const user = this.getUsers().find(u => u.id === session.user?.id);
        if (!user) {
          this.logout();
          return null;
        }
        session.user = user; // refresh live permissions
        return session;
      } catch (e) {
        return null;
      }
    },

    login(identifier, password, portalKey) {
      this.ensureDefaultUsers();
      const users = this.getUsers();
      const cleanId = (identifier || '').trim().toLowerCase();
      const cleanPass = (password || '').trim();

      const user = users.find(u => 
        (u.username.toLowerCase() === cleanId || u.email.toLowerCase() === cleanId)
      );

      if (!user) {
        return { success: false, message: 'Invalid username or email address.' };
      }

      if (user.password !== cleanPass) {
        return { success: false, message: 'Invalid password. Please check your credentials.' };
      }

      const portal = portalKey || this.currentPortal;
      if (!user.permissions || !user.permissions[portal]) {
        const portalNames = { crm: 'CRM Portal', cms: 'CMS Blog Administration', marketing: 'Digital Marketing Dashboard' };
        return {
          success: false,
          message: `Access Denied: Your account does not have permission to access the ${portalNames[portal] || portal}. Contact administrator Neeraj for access.`
        };
      }

      const session = {
        user: {
          id: user.id,
          name: user.name,
          username: user.username,
          email: user.email,
          role: user.role,
          permissions: user.permissions
        },
        portal: portal,
        loginTime: new Date().toISOString()
      };

      localStorage.setItem(STORAGE_SESSION, JSON.stringify(session));
      return { success: true, user: session.user };
    },

    logout() {
      localStorage.removeItem(STORAGE_SESSION);
      sessionStorage.removeItem('neonex_counsellor_auth');
      sessionStorage.removeItem('neonex_cms_auth');
      location.reload();
    },

    createUser(data) {
      const session = this.getSession();
      if (!session || session.user.role !== 'Admin') {
        return { success: false, message: 'Only Administrators can create new user accounts.' };
      }

      if (!data.username || !data.password) {
        return { success: false, message: 'Username and password are required.' };
      }

      const users = this.getUsers();
      const cleanUser = data.username.trim().toLowerCase();
      const cleanEmail = (data.email || '').trim().toLowerCase();

      if (users.some(u => u.username.toLowerCase() === cleanUser)) {
        return { success: false, message: 'Username is already in use.' };
      }
      if (cleanEmail && users.some(u => u.email.toLowerCase() === cleanEmail)) {
        return { success: false, message: 'Email is already registered.' };
      }

      const newUser = {
        id: 'user-' + Date.now(),
        name: data.name || data.username,
        username: data.username.trim(),
        email: data.email ? data.email.trim() : '',
        password: data.password.trim(),
        role: data.role || 'Viewer', // Admin | Editor | Viewer
        permissions: {
          crm: !!(data.permissions && data.permissions.crm),
          cms: !!(data.permissions && data.permissions.cms),
          marketing: !!(data.permissions && data.permissions.marketing)
        },
        createdAt: new Date().toISOString()
      };

      users.push(newUser);
      this.saveUsers(users);
      return { success: true, user: newUser };
    },

    deleteUser(userId) {
      const session = this.getSession();
      if (!session || session.user.role !== 'Admin') {
        return { success: false, message: 'Only Administrators can remove users.' };
      }

      let users = this.getUsers();
      const target = users.find(u => u.id === userId);
      if (!target) return { success: false, message: 'User not found.' };

      if (target.username.toLowerCase() === 'neeraj' || target.email.toLowerCase() === 'pcneeraj123@gmail.com') {
        return { success: false, message: 'Primary Super Administrator account cannot be deleted.' };
      }

      users = users.filter(u => u.id !== userId);
      this.saveUsers(users);
      return { success: true };
    },

    // UI Helpers
    injectStyles() {
      if (document.getElementById('neonex-auth-styles')) return;
      const css = `
        /* RBAC AUTH MODAL & OVERLAY */
        #neonex-auth-overlay {
          position: fixed; inset: 0; background: rgba(7, 11, 20, 0.94);
          backdrop-filter: blur(16px); z-index: 99999;
          display: flex; align-items: center; justify-content: center;
          padding: 20px; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        }
        .neonex-auth-box {
          width: 100%; max-width: 420px; background: #0E1626; border: 1px solid rgba(255,255,255,0.12);
          border-radius: 16px; padding: 36px 32px; box-shadow: 0 25px 60px rgba(0,0,0,0.5);
          color: #F8FAFC; text-align: left; position: relative;
        }
        .neonex-auth-header { text-align: center; margin-bottom: 24px; }
        .neonex-auth-logo-badge {
          width: 44px; height: 44px; border-radius: 12px;
          background: linear-gradient(135deg, #2563EB, #06B6D4);
          display: inline-grid; place-items: center; font-weight: 800; font-size: 20px;
          color: #fff; margin-bottom: 12px; box-shadow: 0 0 20px rgba(37,99,235,0.4);
        }
        .neonex-auth-title { font-size: 20px; font-weight: 800; margin-bottom: 4px; color: #FFFFFF; }
        .neonex-auth-sub { font-size: 13px; color: #94A3B8; }
        
        .neonex-field-group { margin-bottom: 16px; }
        .neonex-field-label { display: block; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #CBD5E1; margin-bottom: 6px; }
        .neonex-field-input {
          width: 100%; height: 44px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.12);
          border-radius: 8px; padding: 0 14px; font-size: 14px; color: #FFFFFF; font-family: inherit;
          transition: all 0.2s; box-sizing: border-box;
        }
        .neonex-field-input:focus { outline: none; border-color: #3B82F6; background: rgba(59,130,246,0.08); box-shadow: 0 0 0 3px rgba(59,130,246,0.2); }
        .neonex-auth-err {
          background: rgba(244,63,94,0.12); border: 1px solid rgba(244,63,94,0.3); color: #FDA4AF;
          padding: 10px 14px; border-radius: 8px; font-size: 12.5px; font-weight: 600; margin-bottom: 16px; display: none;
        }
        .neonex-auth-btn {
          width: 100%; height: 44px; background: linear-gradient(135deg, #2563EB, #0284C7); color: #fff;
          border: none; border-radius: 8px; font-weight: 700; font-size: 14px; cursor: pointer;
          transition: all 0.2s; margin-top: 8px; display: grid; place-items: center;
        }
        .neonex-auth-btn:hover { box-shadow: 0 0 20px rgba(37,99,235,0.4); transform: translateY(-1px); }

        /* USER MGMT MODAL */
        #neonex-mgmt-modal {
          position: fixed; inset: 0; background: rgba(7, 11, 20, 0.85); backdrop-filter: blur(12px);
          z-index: 100000; display: none; align-items: center; justify-content: center; padding: 20px;
        }
        .neonex-mgmt-card {
          width: 100%; max-width: 820px; max-height: 90vh; background: #0E1626; border: 1px solid rgba(255,255,255,0.15);
          border-radius: 16px; padding: 28px; box-shadow: 0 25px 60px rgba(0,0,0,0.6); color: #F8FAFC;
          display: flex; flex-direction: column; overflow: hidden;
        }
        .neonex-mgmt-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.08); }
        .neonex-mgmt-body { overflow-y: auto; flex: 1; padding-right: 6px; }
        .neonex-badge-role { padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; font-family: monospace; }
        .neonex-role-admin { background: rgba(139,92,246,0.2); color: #C4B5FD; border: 1px solid rgba(139,92,246,0.4); }
        .neonex-role-editor { background: rgba(59,130,246,0.2); color: #93C5FD; border: 1px solid rgba(59,130,246,0.4); }
        .neonex-role-viewer { background: rgba(16,185,129,0.2); color: #6EE7B7; border: 1px solid rgba(16,185,129,0.4); }
        .neonex-chip-portal { font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; background: rgba(255,255,255,0.06); color: #94A3B8; margin-right: 4px; }
        .neonex-chip-active { background: rgba(6,182,212,0.15); color: #22D3EE; border: 1px solid rgba(6,182,212,0.3); }

        /* USER HEADER PILL */
        .neonex-user-bar {
          display: inline-flex; align-items: center; gap: 10px; background: rgba(255,255,255,0.04);
          border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 8px; font-size: 13px;
        }
        .neonex-nav-link { color: #94A3B8; text-decoration: none; font-size: 12px; font-weight: 600; padding: 4px 8px; border-radius: 6px; transition: all 0.2s; }
        .neonex-nav-link:hover { color: #FFFFFF; background: rgba(255,255,255,0.06); }
      `;
      const styleEl = document.createElement('style');
      styleEl.id = 'neonex-auth-styles';
      styleEl.textContent = css;
      document.head.appendChild(styleEl);
    },

    renderAuthGate(portalKey, titleText, onAuthenticated) {
      this.init(portalKey);
      const session = this.getSession();

      if (session && session.user && session.user.permissions && session.user.permissions[portalKey]) {
        if (typeof onAuthenticated === 'function') onAuthenticated(session.user);
        this.renderUserBar(session.user);
        return;
      }

      // Show Gate
      let overlay = document.getElementById('neonex-auth-overlay');
      if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'neonex-auth-overlay';
        document.body.appendChild(overlay);
      }

      const portalDisplayNames = {
        crm: 'Counsellor & CRM Portal',
        cms: 'Blog Publisher & CMS',
        marketing: 'Digital Marketing Intelligence Hub'
      };

      overlay.innerHTML = `
        <div class="neonex-auth-box">
          <div class="neonex-auth-header">
            <div class="neonex-auth-logo-badge">N</div>
            <h2 class="neonex-auth-title">NeoNeX MindX</h2>
            <p class="neonex-auth-sub">${titleText || portalDisplayNames[portalKey] || 'Workspace Login'}</p>
          </div>
          <div class="neonex-auth-err" id="neonex-err-banner"></div>
          <form id="neonex-login-form">
            <div class="neonex-field-group">
              <label class="neonex-field-label">Username or Email</label>
              <input type="text" id="neonex-login-user" class="neonex-field-input" placeholder="Enter your username or email" required autofocus autocomplete="username" />
            </div>
            <div class="neonex-field-group" style="position:relative;">
              <label class="neonex-field-label">Password</label>
              <input type="password" id="neonex-login-pass" class="neonex-field-input" placeholder="Enter your password" required autocomplete="current-password" style="padding-right:40px;" />
              <button type="button" id="neonex-toggle-pass" style="position:absolute; right:10px; top:32px; background:none; border:none; color:#94A3B8; cursor:pointer; font-size:16px;">👁️</button>
            </div>
            <button type="submit" class="neonex-auth-btn">Authorize & Sign In &rarr;</button>
          </form>
          <div style="font-size:11px; color:#64748B; margin-top:20px; text-align:center;">
            NeoNeX MindX Unified Security Gateway
          </div>
        </div>
      `;

      // Password toggle
      const passInput = document.getElementById('neonex-login-pass');
      const toggleBtn = document.getElementById('neonex-toggle-pass');
      toggleBtn.addEventListener('click', () => {
        passInput.type = passInput.type === 'password' ? 'text' : 'password';
        toggleBtn.textContent = passInput.type === 'password' ? '👁️' : '🔒';
      });

      // Submit
      document.getElementById('neonex-login-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const userInput = document.getElementById('neonex-login-user').value;
        const passInputVal = passInput.value;
        const errBanner = document.getElementById('neonex-err-banner');

        const result = this.login(userInput, passInputVal, portalKey);
        if (result.success) {
          overlay.remove();
          if (typeof onAuthenticated === 'function') onAuthenticated(result.user);
          this.renderUserBar(result.user);
        } else {
          errBanner.textContent = result.message;
          errBanner.style.display = 'block';
        }
      });
    },

    renderUserBar(user) {
      let bar = document.getElementById('neonex-user-bar');
      if (!bar) {
        bar = document.createElement('div');
        bar.id = 'neonex-user-bar';
        bar.style.position = 'fixed';
        bar.style.bottom = '16px';
        bar.style.right = '16px';
        bar.style.zIndex = '9999';
        document.body.appendChild(bar);
      }

      const roleClass = user.role === 'Admin' ? 'neonex-role-admin' : (user.role === 'Editor' ? 'neonex-role-editor' : 'neonex-role-viewer');
      const isAdmin = user.role === 'Admin';

      bar.innerHTML = `
        <div class="neonex-user-bar" style="background:rgba(14,22,38,0.92); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.15); box-shadow:0 10px 25px rgba(0,0,0,0.4);">
          <span style="font-size:12px; color:#F8FAFC; display:flex; align-items:center; gap:6px;">
            <span style="width:8px; height:8px; border-radius:50%; background:#10B981;"></span>
            <strong>${user.name || user.username}</strong>
            <span class="neonex-badge-role ${roleClass}">${user.role}</span>
          </span>
          <span style="color:rgba(255,255,255,0.2);">|</span>
          <a href="/crm" class="neonex-nav-link" title="Open CRM">CRM</a>
          <a href="/cms" class="neonex-nav-link" title="Open CMS">CMS</a>
          <a href="/digital-marketing" class="neonex-nav-link" title="Open Marketing Dashboard">Marketing</a>
          ${isAdmin ? `<button onclick="NeonexAuth.openUserManagement()" style="background:#2563EB; color:#fff; border:none; padding:4px 9px; border-radius:5px; font-size:11px; font-weight:700; cursor:pointer; display:flex; align-items:center; gap:4px;">👥 Team</button>` : ''}
          <button onclick="NeonexAuth.logout()" style="background:none; border:none; color:#F43F5E; font-size:11px; font-weight:700; cursor:pointer; padding:4px 6px;" title="Sign out">Logout</button>
        </div>
      `;
    },

    openUserManagement() {
      const session = this.getSession();
      if (!session || session.user.role !== 'Admin') {
        alert('Access Restricted: Only Administrators can manage team accounts.');
        return;
      }

      let modal = document.getElementById('neonex-mgmt-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'neonex-mgmt-modal';
        document.body.appendChild(modal);
      }

      const users = this.getUsers();

      modal.innerHTML = `
        <div class="neonex-mgmt-card">
          <div class="neonex-mgmt-header">
            <div>
              <h3 style="font-size:18px; font-weight:800; color:#fff;">Team & Access Management</h3>
              <p style="font-size:12px; color:#94A3B8; margin-top:2px;">Manage team members, roles (Admin/Editor/Viewer), and portal access for CRM, CMS & Marketing.</p>
            </div>
            <button onclick="document.getElementById('neonex-mgmt-modal').style.display='none'" style="background:none; border:none; color:#94A3B8; font-size:20px; cursor:pointer;">&times;</button>
          </div>
          
          <div class="neonex-mgmt-body">
            
            <!-- CREATE NEW USER ACCORDION -->
            <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:18px; margin-bottom:24px;">
              <h4 style="font-size:14px; font-weight:700; color:#38BDF8; margin-bottom:12px;">+ Add New Team Member</h4>
              <form id="neonex-create-user-form" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:12px;">
                <div>
                  <label class="neonex-field-label">Full Name</label>
                  <input type="text" id="new-user-name" class="neonex-field-input" placeholder="e.g. Venkat" required />
                </div>
                <div>
                  <label class="neonex-field-label">Username</label>
                  <input type="text" id="new-user-username" class="neonex-field-input" placeholder="e.g. venkat" required />
                </div>
                <div>
                  <label class="neonex-field-label">Email (Optional)</label>
                  <input type="email" id="new-user-email" class="neonex-field-input" placeholder="e.g. venkat@neonexmindx.com" />
                </div>
                <div>
                  <label class="neonex-field-label">Password</label>
                  <input type="password" id="new-user-password" class="neonex-field-input" placeholder="Create password..." required />
                </div>
                <div>
                  <label class="neonex-field-label">Role</label>
                  <select id="new-user-role" class="neonex-field-input">
                    <option value="Viewer">Viewer (Read Only)</option>
                    <option value="Editor">Editor (Can edit content/leads)</option>
                    <option value="Admin">Admin (Full privileges)</option>
                  </select>
                </div>
                <div>
                  <label class="neonex-field-label">Portal Access Permissions</label>
                  <div style="display:flex; gap:12px; align-items:center; height:44px; font-size:13px;">
                    <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                      <input type="checkbox" id="perm-crm" checked /> CRM
                    </label>
                    <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                      <input type="checkbox" id="perm-cms" checked /> CMS
                    </label>
                    <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                      <input type="checkbox" id="perm-marketing" checked /> Marketing
                    </label>
                  </div>
                </div>
                <div style="grid-column: 1 / -1; margin-top:4px;">
                  <button type="submit" class="neonex-auth-btn" style="height:38px; width:auto; padding:0 24px;">Create Member Credentials</button>
                  <span id="new-user-msg" style="margin-left:12px; font-size:12px; font-weight:600;"></span>
                </div>
              </form>
            </div>

            <!-- USERS LIST TABLE -->
            <h4 style="font-size:14px; font-weight:700; color:#fff; margin-bottom:12px;">Active Team Accounts (${users.length})</h4>
            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
                <thead>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.1); color:#94A3B8;">
                    <th style="padding:8px;">Member</th>
                    <th style="padding:8px;">Username</th>
                    <th style="padding:8px;">Email</th>
                    <th style="padding:8px;">Role</th>
                    <th style="padding:8px;">Portal Access</th>
                    <th style="padding:8px; text-align:right;">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  ${users.map(u => {
                    const isSuper = u.username.toLowerCase() === 'neeraj' || u.email.toLowerCase() === 'pcneeraj123@gmail.com';
                    const roleClass = u.role === 'Admin' ? 'neonex-role-admin' : (u.role === 'Editor' ? 'neonex-role-editor' : 'neonex-role-viewer');
                    return `
                      <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                        <td style="padding:10px 8px;"><strong>${u.name || u.username}</strong> ${isSuper ? '<span style="color:#F59E0B; font-size:11px;">(Primary)</span>' : ''}</td>
                        <td style="padding:10px 8px; font-family:monospace; color:#38BDF8;">${u.username}</td>
                        <td style="padding:10px 8px; color:#94A3B8;">${u.email || '—'}</td>
                        <td style="padding:10px 8px;"><span class="neonex-badge-role ${roleClass}">${u.role}</span></td>
                        <td style="padding:10px 8px;">
                          <span class="neonex-chip-portal ${u.permissions?.crm ? 'neonex-chip-active' : ''}">CRM</span>
                          <span class="neonex-chip-portal ${u.permissions?.cms ? 'neonex-chip-active' : ''}">CMS</span>
                          <span class="neonex-chip-portal ${u.permissions?.marketing ? 'neonex-chip-active' : ''}">MKT</span>
                        </td>
                        <td style="padding:10px 8px; text-align:right;">
                          ${isSuper ? '<span style="color:#64748B; font-size:11px;">Protected</span>' : `
                            <button onclick="NeonexAuth.handleDeleteUser('${u.id}')" style="background:rgba(244,63,94,0.15); border:1px solid rgba(244,63,94,0.3); color:#FDA4AF; border-radius:5px; padding:3px 8px; font-size:11px; cursor:pointer;">Delete</button>
                          `}
                        </td>
                      </tr>
                    `;
                  }).join('')}
                </tbody>
              </table>
            </div>

          </div>
        </div>
      `;

      modal.style.display = 'flex';

      // Attach create form listener
      document.getElementById('neonex-create-user-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const msgEl = document.getElementById('new-user-msg');
        const res = this.createUser({
          name: document.getElementById('new-user-name').value,
          username: document.getElementById('new-user-username').value,
          email: document.getElementById('new-user-email').value,
          password: document.getElementById('new-user-password').value,
          role: document.getElementById('new-user-role').value,
          permissions: {
            crm: document.getElementById('perm-crm').checked,
            cms: document.getElementById('perm-cms').checked,
            marketing: document.getElementById('perm-marketing').checked
          }
        });

        if (res.success) {
          msgEl.style.color = '#10B981';
          msgEl.textContent = 'User created successfully!';
          setTimeout(() => this.openUserManagement(), 600);
        } else {
          msgEl.style.color = '#F43F5E';
          msgEl.textContent = res.message;
        }
      });
    },

    handleDeleteUser(userId) {
      if (confirm('Are you sure you want to remove this user account?')) {
        const res = this.deleteUser(userId);
        if (res.success) {
          this.openUserManagement();
        } else {
          alert(res.message);
        }
      }
    }
  };

  window.NeonexAuth = NeonexAuth;

})(window);
