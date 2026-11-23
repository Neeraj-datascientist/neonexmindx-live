/**
 * Cloudflare Pages Function: Google Ads Lead Form Extension Webhook
 * Endpoint: https://neonexmindx.com/api/webhook/google-ads
 */

export async function onRequestGet(context) {
  return new Response(JSON.stringify({
    status: 'online',
    endpoint: 'Google Ads Lead Form Extension Webhook',
    customer_id: '606-542-9317'
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const EXPECTED_KEY = 'nx_gads_lead_token_2026';

    // Verify key if provided by Google Ads
    if (body.google_key && body.google_key !== EXPECTED_KEY) {
      return new Response(JSON.stringify({ error: 'Unauthorized: Invalid google_key' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Google Ads payload structure:
    // { lead_id, user_column_data: [{ column_id, column_name, string_value }] }
    let name = body.name || '';
    let phone = body.phone || '';
    let email = body.email || '';
    let course = body.course || body.program || 'Data Analytics Master Program';

    if (body.user_column_data && Array.isArray(body.user_column_data)) {
      body.user_column_data.forEach(col => {
        const cname = (col.column_name || col.column_id || '').toUpperCase();
        const val = col.string_value || '';
        if (cname.includes('FULL_NAME') || cname.includes('NAME')) name = val;
        else if (cname.includes('PHONE') || cname.includes('MOBILE')) phone = val;
        else if (cname.includes('EMAIL')) email = val;
        else if (cname.includes('COURSE') || cname.includes('PROGRAM')) course = val;
      });
    }

    if (!phone && !name && !email) {
      return new Response(JSON.stringify({ success: true, message: 'Google Ads ping test received' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const lead = {
      id: 'gads-webhook-' + (body.lead_id || Date.now()),
      name: name || 'Google Ads Applicant',
      phone: phone || '-',
      email: email || '-',
      program: course,
      date: new Date().toLocaleDateString('en-GB'),
      status: 'New',
      sprint: 'Sprint 2 (Current)',
      source: 'Google Ads (Search & PMax)',
      utm_source: 'google_ads',
      utm_medium: 'cpc',
      utm_campaign: body.campaign_id || body.campaign_name || 'Search_Data_Analytics_Course_Bengaluru',
      notes: `[Sprint 2 Active] Google Lead Form Extension Submission (Campaign: ${body.campaign_id || 'PMax'})`
    };

    return new Response(JSON.stringify({
      success: true,
      message: 'Google Ads lead captured and segmented into Sprint 2 (Current)',
      lead
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
