export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname.toLowerCase();
  const path = url.pathname.toLowerCase().replace(/\/$/, '');

  // 1. Permanent 301 redirects for legacy standalone courses to flagship career programs
  if (path === '/courses/sql-course' || path === '/sql-course') {
    return Response.redirect('https://neonexmindx.com/courses/data-analytics-course/', 301);
  }
  if (path === '/courses/excel-power-bi-tableau-course' || path === '/excel-power-bi-tableau-course') {
    return Response.redirect('https://neonexmindx.com/courses/data-analytics-course/', 301);
  }
  if (path === '/courses/python-programming-course' || path === '/python-programming-course') {
    return Response.redirect('https://neonexmindx.com/courses/data-science-course/', 301);
  }
  if (path === '/courses/machine-learning-course' || path === '/machine-learning-course') {
    return Response.redirect('https://neonexmindx.com/courses/ai-ml-course/', 301);
  }

  // 2. Subdomains routing
  if (host === 'crm.neonexmindx.com') {
    return Response.redirect('https://neonexmindx.com/crm' + (url.pathname === '/' ? '' : url.pathname), 302);
  }
  if (host === 'cms.neonexmindx.com') {
    return Response.redirect('https://neonexmindx.com/cms' + (url.pathname === '/' ? '' : url.pathname), 302);
  }
  if (host === 'sms.neonexmindx.com' || host === 'social.neonexmindx.com') {
    return Response.redirect('https://neonexmindx.com/sms' + (url.pathname === '/' ? '' : url.pathname), 302);
  }

  return context.next();
}
