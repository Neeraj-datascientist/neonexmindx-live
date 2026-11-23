/**
 * Cloudflare Pages Function: Meta (Facebook & Instagram) Lead Ads Webhook
 * Endpoint: https://neonexmindx.com/api/webhook/meta
 */

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const mode = url.searchParams.get('hub.mode');
  const token = url.searchParams.get('hub.verify_token');
  const challenge = url.searchParams.get('hub.challenge');

  // Verify token configured for NeoNeX MindX
  const EXPECTED_TOKEN = 'neonex_meta_leads_secret_2026';

  if (mode === 'subscribe' && token === EXPECTED_TOKEN) {
    return new Response(challenge, {
      status: 200,
      headers: { 'Content-Type': 'text/plain' }
    });
  }

  return new Response('Verification failed. Invalid token.', { status: 403 });
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    
    // Check if this is a lead notification
    // Meta sends either standard leadgen notification or payload with lead details
    let lead = null;

    if (body.entry && Array.isArray(body.entry)) {
      for (const entry of body.entry) {
        if (entry.changes && Array.isArray(entry.changes)) {
          for (const change of entry.changes) {
            if (change.field === 'leadgen') {
              const value = change.value;
              lead = {
                id: 'meta-webhook-' + (value.leadgen_id || Date.now()),
                leadgen_id: value.leadgen_id,
                form_id: value.form_id,
                ad_id: value.ad_id,
                created_time: value.created_time || new Date().toISOString()
              };
            }
          }
        }
      }
    } else if (body.name || body.phone || body.phone_number) {
      // Direct lead payload from Zapier/Make or custom webhook relay
      lead = {
        id: 'meta-' + Date.now(),
        name: body.name || body.full_name || 'Prospective Learner',
        phone: body.phone || body.phone_number || body.whatsapp_number || '',
        email: body.email || '-',
        program: body.program || body.course || 'Data Science & AI Master Program',
        campaign_name: body.campaign_name || body.campaign || 'Bengaluru_DataScience_LeadGen_Sprint2',
        ad_name: body.ad_name || 'Instagram / FB Lead Ad',
        notes: body.notes || 'Instant Form Lead submission'
      };
    }

    if (!lead) {
      return new Response(JSON.stringify({ success: true, message: 'Event received, no lead data found' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Auto-classify campaign sprint: Any lead arriving now belongs to Sprint 2
    lead.sprint = 'Sprint 2 (Current)';
    lead.source = 'Meta Ads (Facebook & Instagram)';
    lead.utm_source = 'meta_ads';
    lead.utm_medium = 'paid_social';
    lead.date = new Date().toLocaleDateString('en-GB');
    lead.status = 'New';

    return new Response(JSON.stringify({
      success: true,
      message: 'Meta Lead captured and segmented into Sprint 2 (Current)',
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
