export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname.toLowerCase();

  // If visiting crm.neonexmindx.com, rewrite path internally or redirect to clean CRM
  if (host === 'crm.neonexmindx.com') {
    if (url.pathname === '/' || url.pathname === '') {
      return Response.redirect('https://neonexmindx.com/crm', 302);
    }
    return Response.redirect(`https://neonexmindx.com/crm${url.pathname}`, 302);
  }

  // If visiting cms.neonexmindx.com, redirect to clean CMS Studio
  if (host === 'cms.neonexmindx.com') {
    if (url.pathname === '/' || url.pathname === '') {
      return Response.redirect('https://neonexmindx.com/cms', 302);
    }
    return Response.redirect(`https://neonexmindx.com/cms${url.pathname}`, 302);
  }

  // If visiting sms.neonexmindx.com, redirect to clean Social Media Hub
  if (host === 'sms.neonexmindx.com' || host === 'social.neonexmindx.com') {
    if (url.pathname === '/' || url.pathname === '') {
      return Response.redirect('https://neonexmindx.com/sms', 302);
    }
    return Response.redirect(`https://neonexmindx.com/sms${url.pathname}`, 302);
  }

  return context.next();
}
