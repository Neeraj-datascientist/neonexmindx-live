/**
 * NeoNeX MindX - Universal UTM Attribution & Lead Telemetry Tracker
 * Automatically captures first-touch and multi-touch campaign parameters
 * and seamlessly synchronizes lead submissions with the Central Counsellor CRM.
 */
(function() {
  'use strict';

  // 1. Capture UTM & Ad Click Parameters on Page Load
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid', 'msclkid'];
    utmKeys.forEach(function(key) {
      if (urlParams.has(key)) {
        const val = urlParams.get(key);
        try { sessionStorage.setItem(key, val); } catch(e) {}
        try { localStorage.setItem('neonex_last_' + key, val); } catch(e) {}
      }
    });
  } catch(e) {}

  // Helper to extract active attribution
  function getAttribution() {
    let p = null;
    try { p = new URLSearchParams(window.location.search); } catch(e) {}
    
    function getVal(key) {
      if (p && p.has(key)) return p.get(key);
      try {
        const s = sessionStorage.getItem(key);
        if (s) return s;
        const l = localStorage.getItem('neonex_last_' + key);
        if (l) return l;
      } catch(e) {}
      return null;
    }

    let defaultSource = 'direct';
    let defaultMedium = 'direct';
    if (document.referrer) {
      const ref = document.referrer.toLowerCase();
      if (ref.includes('google.')) { defaultSource = 'google'; defaultMedium = 'organic'; }
      else if (ref.includes('linkedin.')) { defaultSource = 'linkedin'; defaultMedium = 'organic_social'; }
      else if (ref.includes('youtube.')) { defaultSource = 'youtube'; defaultMedium = 'video'; }
      else if (ref.includes('instagram.')) { defaultSource = 'instagram'; defaultMedium = 'social'; }
      else if (ref.includes('facebook.') || ref.includes('meta.')) { defaultSource = 'meta'; defaultMedium = 'social'; }
      else if (ref.includes('bing.')) { defaultSource = 'bing'; defaultMedium = 'organic'; }
      else if (!ref.includes(window.location.hostname)) { defaultSource = 'referral'; defaultMedium = 'referral'; }
    }

    return {
      utm_source: getVal('utm_source') || defaultSource,
      utm_medium: getVal('utm_medium') || defaultMedium,
      utm_campaign: getVal('utm_campaign') || 'none',
      utm_content: getVal('utm_content') || '',
      utm_term: getVal('utm_term') || '',
      referrer: document.referrer || '',
      landing_page: window.location.pathname
    };
  }

  // 2. Global Lead Submission Dispatcher
  window.submitNeoNexLead = async function(leadData) {
    if (!leadData) return { success: false, error: 'Empty lead data' };
    try {
      const attr = getAttribution();
      const payload = Object.assign({}, attr, leadData, {
        timestamp: leadData.date || new Date().toISOString(),
        id: leadData.id || ('lead-' + Date.now())
      });

      // Synchronize to Central Server CRM API
      const res = await fetch('/api/submit-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      return await res.json();
    } catch(err) {
      console.warn('[NeoNex Tracker] Remote submit error (local fallback active):', err);
      return { success: false, error: err.message };
    }
  };

  // 3. Intercept localStorage.setItem to seamlessly route existing website forms
  try {
    const origSetItem = localStorage.setItem;
    localStorage.setItem = function(key, value) {
      origSetItem.apply(this, arguments);
      if (key === 'neonex_crm_leads') {
        try {
          const list = JSON.parse(value);
          if (Array.isArray(list) && list.length > 0) {
            const latestLead = list[0];
            const now = Date.now();
            window._lastLeadSentTime = window._lastLeadSentTime || 0;
            // Debounce within 3 seconds to avoid double submission
            if (now - window._lastLeadSentTime > 3000) {
              window._lastLeadSentTime = now;
              window.submitNeoNexLead(latestLead);
            }
          }
        } catch(e) {}
      }
    };
  } catch(e) {}

  // Expose global tracker
  window.NeoNexTracker = {
    getAttribution: getAttribution,
    submitLead: window.submitNeoNexLead
  };
})();
